# PostgreSQL Database Setup Guide

## Prerequisites

-   PostgreSQL installed and running
-   Python 3.8+ with virtual environment

## Setup Steps

### 1. Install PostgreSQL

```bash
# macOS
brew install postgresql@15
brew services start postgresql@15

# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib
sudo systemctl start postgresql
```

### 2. Create Database

```bash
# Using the setup script
./setup_db.sh

# Or manually
psql -U postgres
CREATE DATABASE manifest_manager_db;
CREATE DATABASE manifest_manager_test_db;
\q
```

### 3. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your database credentials
# DATABASE_URL=postgresql://username:password@localhost:5432/manifest_manager_db
```

### 4. Install Dependencies

```bash
# Activate virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install packages
pip install -r requirements.txt
```

### 5. Initialize Database Migrations

```bash
# Initialize Flask-Migrate
flask db init

# Create initial migration
flask db migrate -m "Initial migration with User, Deployment, and Service models"

# Apply migration
flask db upgrade
```

### 6. Create Admin User (Optional)

```bash
flask create-admin
# Follow prompts to enter email, password, and name
```

## Database Models

### User Model

-   `id`: Primary key
-   `email`: Unique email address
-   `password_hash`: Hashed password
-   `name`: User's full name
-   `is_active`: Account status
-   `created_at`: Timestamp
-   `updated_at`: Timestamp

### Deployment Model

-   `id`: Primary key
-   `name`: Deployment name
-   `image`: Container image
-   `namespace`: Kubernetes namespace
-   `tier`: Deployment tier
-   `ports`: Container ports (comma-separated)
-   `yaml_content`: Generated YAML
-   `created_by`: Foreign key to User
-   `created_at`: Timestamp
-   `updated_at`: Timestamp

### Service Model

-   `id`: Primary key
-   `name`: Service name
-   `namespace`: Kubernetes namespace
-   `tier`: Service tier
-   `port`: Service port
-   `target_port`: Target port
-   `node_port`: NodePort
-   `service_type`: Type of service
-   `yaml_content`: Generated YAML
-   `created_by`: Foreign key to User
-   `created_at`: Timestamp
-   `updated_at`: Timestamp

## Common Commands

```bash
# Run migrations
flask db migrate -m "Description of changes"
flask db upgrade

# Rollback migration
flask db downgrade

# Initialize database
flask init-db

# Create admin user
flask create-admin

# Run the application
python run.py
```

## Troubleshooting

### Connection Error

-   Ensure PostgreSQL is running: `pg_isready`
-   Check DATABASE_URL in .env file
-   Verify PostgreSQL credentials

### Migration Issues

```bash
# Remove migrations folder and reinitialize
rm -rf migrations
flask db init
flask db migrate -m "Fresh start"
flask db upgrade
```

### Reset Database

```bash
# Drop and recreate database
psql -U postgres -c "DROP DATABASE manifest_manager_db;"
psql -U postgres -c "CREATE DATABASE manifest_manager_db;"
flask db upgrade
```
