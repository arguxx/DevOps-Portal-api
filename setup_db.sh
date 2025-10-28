#!/bin/bash

# Database setup script for PostgreSQL

echo "Setting up PostgreSQL database for Manifest Manager API"

# Check if PostgreSQL is running
if ! pg_isready > /dev/null 2>&1; then
    echo "Error: PostgreSQL is not running. Please start PostgreSQL first."
    exit 1
fi

# Database name
DB_NAME="manifest_manager_db"
DB_TEST_NAME="manifest_manager_test_db"

# Create database if it doesn't exist
echo "Creating database: $DB_NAME"
psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME'" | grep -q 1 || psql -U postgres -c "CREATE DATABASE $DB_NAME"

echo "Creating test database: $DB_TEST_NAME"
psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = '$DB_TEST_NAME'" | grep -q 1 || psql -U postgres -c "CREATE DATABASE $DB_TEST_NAME"

echo "Databases created successfully!"
echo ""
echo "Next steps:"
echo "1. Copy .env.example to .env and update with your database credentials"
echo "2. Run 'flask db init' to initialize migrations"
echo "3. Run 'flask db migrate -m \"Initial migration\"' to create migration"
echo "4. Run 'flask db upgrade' to apply migrations"
