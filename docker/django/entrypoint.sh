#!/bin/bash
set -e
cmd="$@"

#django-admin startproject customapp .

if [ "$RUN_MIGRATE" != "" ];
then
    python manage.py migrate --noinput
fi

if [ "$RUN_COLLECTSTATIC" != "" ];
then
    python manage.py collectstatic --noinput
fi

if [ "$SYNC_PERMISSIONS" != "" ];
then
    ./manage.py fix_permissions
    ./manage.py sync_permissions
fi

exec $cmd