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
        lines = f.readlines()

    for line in lines:
        if line.startswith('{}:'.format(key)):
            line = '{key}: "{value}"\n'.format(key=key, value=value)
            parameter_exists = True
        patched_lines.append(line)

    if not parameter_exists:
        patched_lines.append('{key}: "{value}"\n'.format(key=key, value=value))

    with open(path, 'w') as f:
        f.write(''.join(patched_lines))


def patch_parameters(path):
    set_parameter(path, 'project_name', '{{ cookiecutter.project_slug }}')
    set_parameter(path, 'database_name', '{{ cookiecutter.project_slug }}')
    set_parameter(path, 'hostname', '{{ cookiecutter.project_slug.replace("_", "-") }}.lo')
    set_parameter(path, 'root_directory', '/vagrant/public_html')


def patch_playbook(path):
    patched_lines = []

    with open(path) as f:
        lines = f.readlines()

    for line in lines:
        if 'role: php-fpm' in line or \
           'role: composer' in line or \
           'role: mysql' in line:
            line = line.replace('# -', '-')

        patched_lines.append(line)

    patched_lines.append('    - { role: nodejs }' + "\n\n")
    patched_lines.append('  tasks:' + "\n")
    patched_lines.append('    - apt: pkg=lftp state=latest' + "\n")
    patched_lines.append('      become: yes' + "\n")
    patched_lines.append('    - apt: pkg=gettext state=latest' + "\n")
    patched_lines.append('      become: yes' + "\n")
    patched_lines.append('    - apt: pkg=php-gettext state=latest' + "\n")
    patched_lines.append('      become: yes' + "\n")
    patched_lines.append('    - command: /usr/local/bin/composer.phar --no-dev --quiet install' + "\n")
    patched_lines.append('      args:' + "\n")
    patched_lines.append('          chdir: /vagrant' + "\n")
    patched_lines.append('    - command: ./vendor/bin/wp package install aaemnnosttv/wp-cli-dotenv-command' + "\n")
    patched_lines.append('      args:' + "\n")
    patched_lines.append('          chdir: /vagrant' + "\n")
    patched_lines.append('    - command: ./vendor/bin/wp dotenv salts regenerate' + "\n")
    patched_lines.append('      args:' + "\n")
    patched_lines.append('          chdir: /vagrant' + "\n")
    patched_lines.append('    - command: git clone git@github.com:wp-mirrors/wp-i18n-tools.git' + "\n")
    patched_lines.append('      args:' + "\n")
    patched_lines.append('          chdir: /home/vagrant' + "\n")
    patched_lines.append('          creates: /home/vagrant/wp-i18n-tools' + "\n")
    patched_lines.append('    - file:' + "\n")
    patched_lines.append('          src: /vagrant/public_html/wp/wp-includes/pomo/' + "\n")
    patched_lines.append('          dest: /home/vagrant/wp-i18n-tools/pomo' + "\n")
    patched_lines.append('          state: link' + "\n")
    patched_lines.append('    - shell: curl "http://localhost/wp/wp-admin/install.php?step=2"'
                         ' --data-urlencode "weblog_title={{ cookiecutter.project_slug.replace("_", "-") }}.lo"'
                         ' --data-urlencode "user_name=admin"'
                         ' --data-urlencode "admin_email=root@test.lo"'
                         ' --data-urlencode "admin_password=admin"'
                         ' --data-urlencode "admin_password2=admin"'
                         ' --data-urlencode "pw_weak=1"' + "\n")
    patched_lines.append('    - command: npm install' + "\n")
    patched_lines.append('      args:' + "\n")
    patched_lines.append('          chdir: /vagrant/public_html/app/themes/{{ cookiecutter.project_slug }}' + "\n")
    patched_lines.append('    - command: node node_modules/kanbasu/scripts/scaffold.js assets/scss/' + "\n")
    patched_lines.append('      args:' + "\n")
    patched_lines.append('          chdir: /vagrant/public_html/app/themes/{{ cookiecutter.project_slug }}' + "\n")

    with open(path, 'w') as f:
        f.write(''.join(patched_lines))


def patch_vagrantfile(path):
    with open(path) as f:
        lines = f.readlines()

    lines.append('Vagrant.configure("2") do |config|' + "\n")
    lines.append('    if Vagrant.has_plugin?("vagrant-bindfs")' + "\n")
    lines.append('        config.bindfs.bind_folder "/vagrant", "/vagrant"' + "\n")
    lines.append('    end' + "\n")
    lines.append('end' + "\n")

    with open(path, 'w') as f:
        f.write(''.join(lines))


if __name__ == '__main__':
    install_drifter()
    patch_parameters('virtualization/parameters.yml')
    patch_playbook('virtualization/playbook.yml')
    patch_vagrantfile('Vagrantfile')
    os.system('git update-ref -d HEAD')
    os.system('git add .')
    os.system('git commit -am "first blood"')
