#!/bin/sh
# wait-for-postgres.sh

set -e
  
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U "$POSTGRES_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
  
>&2 echo "Postgres is up - executing command"
python manage.py migrate
python manage.py runserver 0.0.0.0:5000
