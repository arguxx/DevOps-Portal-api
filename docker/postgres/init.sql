-- PostgreSQL initialization script
-- This script runs automatically when the container is first created

-- Create test database
CREATE DATABASE manifest_manager_test_db;

-- Create extensions if needed
\c manifest_manager_db;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

\c manifest_manager_test_db;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE manifest_manager_db TO postgres;
GRANT ALL PRIVILEGES ON DATABASE manifest_manager_test_db TO postgres;
