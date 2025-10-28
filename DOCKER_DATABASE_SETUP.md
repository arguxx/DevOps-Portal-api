# Docker PostgreSQL Setup Guide

## 🐳 Quick Start

### 1. Start PostgreSQL in Docker

```bash
# Start only PostgreSQL
docker-compose up -d postgres

# Or start with pgAdmin (web-based database management)
docker-compose up -d
```

### 2. Verify Database is Running

```bash
# Using the management script
./manage_docker_db.sh status

# Or manually check
docker-compose ps
```

### 3. Create .env File

```bash
cp .env.example .env
# The default DATABASE_URL is already configured for Docker
```

### 4. Run Migrations

```bash
# Initialize migrations
flask db init

# Create migration
flask db migrate -m "Initial migration"

# Apply migration
flask db upgrade
```

### 5. Create Admin User

```bash
flask create-admin
```

## 📦 What's Included

### Docker Services

1. **PostgreSQL Container**

    - Image: `postgres:15-alpine`
    - Port: `5432`
    - Volume: `postgres_data` (persistent storage)
    - Health checks enabled

2. **pgAdmin (Optional)**
    - Access: http://localhost:5050
    - Email: `admin@admin.com`
    - Password: `admin`
    - Web-based database management

### Files Created

-   `Dockerfile.postgres` - PostgreSQL container configuration
-   `Dockerfile` - Flask application container
-   `docker-compose.yml` - PostgreSQL + pgAdmin setup
-   `docker-compose.dev.yml` - Full development stack (app + database)
-   `docker/postgres/init.sql` - Database initialization script
-   `manage_docker_db.sh` - Database management helper script

## 🛠️ Management Script Usage

The `manage_docker_db.sh` script provides easy database management:

```bash
# Start database
./manage_docker_db.sh start

# Stop database
./manage_docker_db.sh stop

# Restart database
./manage_docker_db.sh restart

# View logs
./manage_docker_db.sh logs

# Access PostgreSQL shell
./manage_docker_db.sh psql

# Backup database
./manage_docker_db.sh backup

# Restore from backup
./manage_docker_db.sh restore backups/backup_file.sql

# Show status
./manage_docker_db.sh status

# Clean volumes (WARNING: deletes all data)
./manage_docker_db.sh clean
```

## 📊 Data Persistence

Data is stored in Docker named volumes:

```bash
# List volumes
docker volume ls | grep postgres

# Inspect volume
docker volume inspect manifest-manager-api_postgres_data

# Volume location (on host)
# Linux: /var/lib/docker/volumes/manifest-manager-api_postgres_data/_data
# macOS: In Docker Desktop VM
```

### Backup and Restore

**Create Backup:**

```bash
# Using script
./manage_docker_db.sh backup

# Manual
docker-compose exec postgres pg_dump -U postgres manifest_manager_db > backup.sql
```

**Restore Backup:**

```bash
# Using script
./manage_docker_db.sh restore backups/backup.sql

# Manual
docker-compose exec -T postgres psql -U postgres manifest_manager_db < backup.sql
```

## 🚀 Development Workflows

### Option 1: Database Only in Docker

Run PostgreSQL in Docker, Flask app locally:

```bash
# Start database
docker-compose up -d postgres

# Run Flask app locally
source .venv/bin/activate
python run.py
```

### Option 2: Full Stack in Docker

Run both PostgreSQL and Flask app in Docker:

```bash
# Start all services
docker-compose -f docker-compose.dev.yml up -d

# View logs
docker-compose -f docker-compose.dev.yml logs -f

# Access app at http://localhost:5001
```

### Option 3: Database + pgAdmin

Run PostgreSQL with web-based management:

```bash
# Start both services
docker-compose up -d

# Access pgAdmin at http://localhost:5050
# Add server in pgAdmin:
#   Host: postgres
#   Port: 5432
#   Username: postgres
#   Password: postgres
```

## 🔧 Troubleshooting

### Container Won't Start

```bash
# Check logs
docker-compose logs postgres

# Check if port is already in use
lsof -i :5432

# Remove and recreate
docker-compose down
docker-compose up -d
```

### Reset Everything

```bash
# Stop and remove containers and volumes
docker-compose down -v

# Remove all related images
docker rmi $(docker images | grep manifest-manager)

# Start fresh
docker-compose up -d
```

### Connection Issues

```bash
# Verify container is healthy
docker-compose ps

# Test connection from host
psql -h localhost -U postgres -d manifest_manager_db

# Test from within container
docker-compose exec postgres psql -U postgres -d manifest_manager_db
```

### Migrations Not Working

```bash
# Ensure database is running
./manage_docker_db.sh status

# Check DATABASE_URL in .env
cat .env | grep DATABASE_URL

# Recreate migrations
rm -rf migrations
flask db init
flask db migrate -m "Fresh start"
flask db upgrade
```

## 📝 Environment Variables

Key variables in `.env`:

```bash
# For Docker (service name as host)
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/manifest_manager_db

# For local development (localhost as host)
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/manifest_manager_db
```

## 🔐 Security Notes

**For Development:**

-   Default credentials are fine
-   Port 5432 exposed to localhost only

**For Production:**

-   Change default passwords
-   Use secrets management
-   Don't expose ports directly
-   Use private networks
-   Enable SSL/TLS
-   Regular backups

## 📦 Volume Management

```bash
# List all volumes
docker volume ls

# Inspect volume details
docker volume inspect manifest-manager-api_postgres_data

# Backup volume to tar file
docker run --rm -v manifest-manager-api_postgres_data:/data -v $(pwd):/backup \
  alpine tar czf /backup/postgres_data_backup.tar.gz -C /data .

# Restore volume from tar file
docker run --rm -v manifest-manager-api_postgres_data:/data -v $(pwd):/backup \
  alpine sh -c "cd /data && tar xzf /backup/postgres_data_backup.tar.gz"
```

## 🎯 Common Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f postgres

# Execute commands in container
docker-compose exec postgres psql -U postgres

# Restart services
docker-compose restart

# Remove everything (including volumes)
docker-compose down -v
```
