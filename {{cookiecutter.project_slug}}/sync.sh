#!/bin/bash


LCD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
RCD="/demo"

cd $LCD

source .env
mysqldump -u root "$DB_NAME" > dump.sql
WP_HOME_LOCAL="$WP_HOME"

source .env-tizoo
sed -ri "s#$WP_HOME_LOCAL#$WP_HOME#g" dump.sql

source .ftpconfig
FTPURL="ftp://$USER:$PASS@$HOST"

lftp -c "set ftp:ssl-allow no;set ftp:list-options -a;
open '$FTPURL';
lcd $LCD;
cd $RCD;
mirror --reverse --only-newer --parallel=5 --dereference \
       --verbose \
       --exclude-glob .idea/ \
       --exclude-glob .vagrant/ \
       --exclude-glob virtualization/ \
       --exclude-glob node_modules/ \
       --exclude-glob .git/ \
       --exclude-glob .gitignore \
       --exclude-glob .gitmodules \
       --exclude-glob .editorconfig \
       --exclude-glob composer.json \
       --exclude-glob composer.lock \
       --exclude-glob wp-cli.yml \
       --exclude-glob dump.sql \
       --exclude-glob sync.sh \
       --exclude-glob Vagrantfile \
       --exclude-glob ansible.cfg \
       --exclude-glob .env \
       ;
mv .env-tizoo .env;
"

