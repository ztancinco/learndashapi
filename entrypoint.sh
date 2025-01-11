#!/bin/bash

# Check if required environment variables are set
: "${POSTGRES_USER:?POSTGRES_USER is required}"
: "${POSTGRES_PASSWORD:?POSTGRES_PASSWORD is required}"
: "${POSTGRES_DB:?POSTGRES_DB is required}"
: "${POSTGRES_HOST:?POSTGRES_HOST is required}"
: "${POSTGRES_PORT:?POSTGRES_PORT is required}"

# Wait for PostgreSQL to be available
until pg_isready -h db -p 5432; do
  echo "Waiting for database..."
  sleep 2
done

# Set password for root user
export PGPASSWORD='secret'

# Create the root role if it doesn't exist
echo "Creating root role if it doesn't exist..."
psql -h db -U root -d postgres -tc "SELECT 1 FROM pg_roles WHERE rolname = '$POSTGRES_USER'" | grep -q 1 || \
  psql -h db -U root -d postgres -c "CREATE ROLE root WITH LOGIN SUPERUSER CREATEDB CREATEROLE INHERIT NOREPLICATION CONNECTION LIMIT -1 ENCRYPTED PASSWORD '$POSTGRES_PASSWORD';"

# Create the database if it doesn't exist
echo "Creating database if it doesn't exist..."
psql -h db -U root -d postgres -tc "SELECT 1 FROM pg_database WHERE datname = '$POSTGRES_DB'" | grep -q 1 || \
  psql -h db -U root -d postgres -c "CREATE DATABASE $POSTGRES_DB;"

# Run Django migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run the application (or your desired command)
exec "$@"
