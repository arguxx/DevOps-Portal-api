#!/bin/bash

# Docker Database Management Script

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
CONTAINER_NAME="manifest-manager-postgres"
DB_NAME="manifest_manager_db"
DB_USER="postgres"

echo -e "${GREEN}=== PostgreSQL Docker Management ===${NC}\n"

# Function to check if Docker is running
check_docker() {
    if ! docker info > /dev/null 2>&1; then
        echo -e "${RED}Error: Docker is not running. Please start Docker first.${NC}"
        exit 1
    fi
}

# Function to start database
start_db() {
    echo -e "${GREEN}Starting PostgreSQL container...${NC}"
    docker-compose up -d postgres
    echo -e "${GREEN}Waiting for PostgreSQL to be ready...${NC}"
    sleep 5
    docker-compose exec postgres pg_isready -U ${DB_USER}
    echo -e "${GREEN}PostgreSQL is ready!${NC}"
}

# Function to stop database
stop_db() {
    echo -e "${YELLOW}Stopping PostgreSQL container...${NC}"
    docker-compose stop postgres
    echo -e "${GREEN}PostgreSQL stopped.${NC}"
}

# Function to restart database
restart_db() {
    echo -e "${YELLOW}Restarting PostgreSQL container...${NC}"
    docker-compose restart postgres
    echo -e "${GREEN}PostgreSQL restarted.${NC}"
}

# Function to show logs
show_logs() {
    echo -e "${GREEN}Showing PostgreSQL logs (Ctrl+C to exit)...${NC}"
    docker-compose logs -f postgres
}

# Function to access psql
psql_access() {
    echo -e "${GREEN}Accessing PostgreSQL shell...${NC}"
    docker-compose exec postgres psql -U ${DB_USER} -d ${DB_NAME}
}

# Function to backup database
backup_db() {
    BACKUP_FILE="backup_${DB_NAME}_$(date +%Y%m%d_%H%M%S).sql"
    echo -e "${GREEN}Creating backup: ${BACKUP_FILE}${NC}"
    docker-compose exec -T postgres pg_dump -U ${DB_USER} ${DB_NAME} > ./backups/${BACKUP_FILE}
    echo -e "${GREEN}Backup created successfully!${NC}"
}

# Function to restore database
restore_db() {
    if [ -z "$1" ]; then
        echo -e "${RED}Error: Please provide backup file path${NC}"
        echo "Usage: ./manage_docker_db.sh restore <backup_file>"
        exit 1
    fi
    echo -e "${YELLOW}Restoring database from: $1${NC}"
    docker-compose exec -T postgres psql -U ${DB_USER} ${DB_NAME} < "$1"
    echo -e "${GREEN}Database restored successfully!${NC}"
}

# Function to clean volumes
clean_volumes() {
    echo -e "${RED}WARNING: This will delete all database data!${NC}"
    read -p "Are you sure? (yes/no): " confirm
    if [ "$confirm" == "yes" ]; then
        docker-compose down -v
        echo -e "${GREEN}Volumes cleaned successfully!${NC}"
    else
        echo -e "${YELLOW}Operation cancelled.${NC}"
    fi
}

# Function to show status
show_status() {
    echo -e "${GREEN}PostgreSQL Container Status:${NC}"
    docker-compose ps postgres
    echo -e "\n${GREEN}Volume Information:${NC}"
    docker volume ls | grep postgres_data
}

# Main menu
check_docker

case "$1" in
    start)
        start_db
        ;;
    stop)
        stop_db
        ;;
    restart)
        restart_db
        ;;
    logs)
        show_logs
        ;;
    psql)
        psql_access
        ;;
    backup)
        mkdir -p backups
        backup_db
        ;;
    restore)
        restore_db "$2"
        ;;
    clean)
        clean_volumes
        ;;
    status)
        show_status
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|logs|psql|backup|restore|clean|status}"
        echo ""
        echo "Commands:"
        echo "  start   - Start PostgreSQL container"
        echo "  stop    - Stop PostgreSQL container"
        echo "  restart - Restart PostgreSQL container"
        echo "  logs    - Show PostgreSQL logs"
        echo "  psql    - Access PostgreSQL shell"
        echo "  backup  - Create database backup"
        echo "  restore - Restore database from backup file"
        echo "  clean   - Remove all volumes (WARNING: deletes data)"
        echo "  status  - Show container and volume status"
        exit 1
        ;;
esac
