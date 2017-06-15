#!/usr/bin/env python

import os
import subprocess


def install_drifter():
    os.system('git init .')
    os.system('curl -sS https://raw.githubusercontent.com/liip/drifter/master/install.sh | /bin/bash')
    os.system('cd virtualization/drifter && '
              ' git remote set-url origin git@github.com:krtek4/drifter.git &&'
              ' git fetch &&'
              ' git checkout master &&'
              ' git merge --ff-only origin/master ;'
              ' cd ../..')


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
    patched_lines.append('    - become:yes' + "\n")
    patched_lines.append('    - apt: pkg=gettext state=latest' + "\n")
    patched_lines.append('    - become:yes' + "\n")
    patched_lines.append('    - apt: pkg=php-gettext state=latest' + "\n")
    patched_lines.append('    - become:yes' + "\n")
    patched_lines.append('    - shell: cd /vagrant && composer.phar --no-dev --quiet install' + "\n")
    patched_lines.append('    - shell: cd /vagrant && ./vendor/bin/wp package install aaemnnosttv/wp-cli-dotenv-command' + "\n")
    patched_lines.append('    - shell: cd /vagrant && ./vendor/bin/wp dotenv salts regenerate' + "\n")
    patched_lines.append('    - shell: cd /vagrant/public_html/app/themes/{{ cookiecutter.project_slug }} && npm install' + "\n")
    patched_lines.append('    - shell: cd /home/vagrant && git clone git@github.com:wp-mirrors/wp-i18n-tools.git' + "\n")
    patched_lines.append('    - shell: cd /home/vagrant/wp-i18n-tools && ln -s /vagrant/public_html/wp/wp-includes/pomo/' + "\n")
    patched_lines.append('    - shell: curl "http://localhost/wp/wp-admin/install.php?step=2"'
                         ' --data-urlencode "weblog_title={{ cookiecutter.project_slug.replace("_", "-") }}.lo"'
                         ' --data-urlencode "user_name=admin"'
                         ' --data-urlencode "admin_email=root@test.lo"'
                         ' --data-urlencode "admin_password=admin"'
                         ' --data-urlencode "admin_password2=admin"'
                         ' --data-urlencode "pw_weak=1"' + "\n")

    with open(path, 'w') as f:
        f.write(''.join(patched_lines))


if __name__ == '__main__':
    install_drifter()
    patch_parameters('virtualization/parameters.yml')
    patch_playbook('virtualization/playbook.yml')
    os.system('git update-ref -d HEAD')
    os.system('git add .')
    os.system('git commit -am "first blood"')
