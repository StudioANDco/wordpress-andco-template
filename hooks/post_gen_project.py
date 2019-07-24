#!/usr/bin/env python

import os
import subprocess


def install_drifter():
    os.system('git init .')
    os.system('curl -sS https://raw.githubusercontent.com/liip/drifter/master/install.sh | /bin/bash')


def set_parameter(path, key, value):
    patched_lines = []
    parameter_exists = False

    with open(path) as f:
        lines = [l.rstrip() for l in f.readlines()]

    for line in lines:
        if line.startswith('{}:'.format(key)):
            line = '{key}: "{value}"'.format(key=key, value=value)
            parameter_exists = True
        patched_lines.append(line)

    if not parameter_exists:
        patched_lines.append('{key}: "{value}"'.format(key=key, value=value))

    with open(path, 'w') as f:
        f.write("\n".join(patched_lines))


def patch_parameters(path):
    set_parameter(path, 'project_name', '{{ cookiecutter.project_slug }}')
    set_parameter(path, 'database_name', '{{ cookiecutter.project_slug }}')
    set_parameter(path, 'hostname', '{{ cookiecutter.project_slug.replace("_", "-") }}.lo')
    set_parameter(path, 'root_directory', '/vagrant/public_html')
    set_parameter(path, 'nodejs_install_package_json', 'false')
    set_parameter(path, 'webpack_create_config', 'false')
    set_parameter(path, 'php_version', '7.2')


def patch_playbook(path):
    patched_lines = []

    with open(path) as f:
        lines = [l.rstrip() for l in f.readlines()]

    for line in lines:
        if 'role: php-fpm' in line or \
           'role: composer' in line or \
           'role: mysql' in line:
            line = line.replace('# -', '-')

        patched_lines.append(line)

    patched_lines.append('    - { role: webpack }')
    patched_lines.append('')
    patched_lines.append('  tasks:')
    patched_lines.append('    - apt: pkg=lftp state=latest')
    patched_lines.append('      become: yes')
    patched_lines.append('    - apt: pkg=gettext state=latest')
    patched_lines.append('      become: yes')
    patched_lines.append('    - apt: pkg=php-gettext state=latest')
    patched_lines.append('      become: yes')
    patched_lines.append('    - apt: pkg=php7.2-xml state=latest')
    patched_lines.append('      become: yes')
    patched_lines.append('    - apt: pkg=php7.2-mbstring state=latest')
    patched_lines.append('      become: yes')
    patched_lines.append('    - blockinfile:')
    patched_lines.append('          dest: /etc/nginx/sites-available/{{ cookiecutter.project_slug.replace("_", "-") }}.lo')
    patched_lines.append('          insertafter: "index index.php;"')
    patched_lines.append('          content: |')
    patched_lines.append('            location / {')
    patched_lines.append('                try_files $uri $uri/ /index.php?$args;')
    patched_lines.append('            }')
    patched_lines.append('      become: yes')
    patched_lines.append('    - command: /usr/local/bin/composer.phar --no-dev --quiet install')
    patched_lines.append('      args:')
    patched_lines.append('          chdir: /vagrant')
    patched_lines.append('    - command: ./vendor/bin/wp package install aaemnnosttv/wp-cli-dotenv-command')
    patched_lines.append('      args:')
    patched_lines.append('          chdir: /vagrant')
    patched_lines.append('    - command: ./vendor/bin/wp dotenv salts regenerate')
    patched_lines.append('      args:')
    patched_lines.append('          chdir: /vagrant')
    patched_lines.append('    - shell: curl "http://localhost/wp/wp-admin/install.php?step=2"'
                         ' --data-urlencode "weblog_title={{ cookiecutter.project_slug.replace("_", "-") }}.lo"'
                         ' --data-urlencode "user_name=admin"'
                         ' --data-urlencode "admin_email=root@test.lo"'
                         ' --data-urlencode "admin_password=admin"'
                         ' --data-urlencode "admin_password2=admin"'
                         ' --data-urlencode "pw_weak=1"')
    patched_lines.append('    - command: yarn')
    patched_lines.append('      args:')
    patched_lines.append('          chdir: /vagrant/public_html/app/themes/{{ cookiecutter.project_slug }}')

    with open(path, 'w') as f:
        f.write("\n".join(patched_lines))


def patch_vagrantfile(path):
    with open(path) as f:
        lines = [l.rstrip() for l in f.readlines()]

    lines.append('Vagrant.configure("2") do |config|')
    lines.append('    if Vagrant.has_plugin?("vagrant-bindfs")')
    lines.append('        config.bindfs.bind_folder "/vagrant", "/vagrant"')
    lines.append('    end')
    lines.append('end')

    with open(path, 'w') as f:
        f.write("\n".join(lines))


if __name__ == '__main__':
    install_drifter()
    patch_parameters('virtualization/parameters.yml')
    patch_playbook('virtualization/playbook.yml')
    patch_vagrantfile('Vagrantfile')
    os.system('git update-ref -d HEAD')
    os.system('git add .')
    os.system('pre-commit install')
    os.system('git commit -am "first blood"')
