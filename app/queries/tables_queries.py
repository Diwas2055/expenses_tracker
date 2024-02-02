default = """
-- Create the uuid-ossp extension if it doesn't exist
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create the roletype ENUM type if it doesn't exist
-- CREATE TYPE roletype AS ENUM ('user', 'admin');

-- Create the givetaketype enum type if it doesn't exist
-- CREATE TYPE givetaketype AS ENUM ('give', 'take');
"""

users = """
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(120) UNIQUE,
    password VARCHAR(255),
    first_name VARCHAR(30),
    last_name VARCHAR(50),
    role roletype DEFAULT 'user' NOT NULL,
    banned BOOLEAN DEFAULT FALSE,
    verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT null
);
"""

expenses = """
CREATE TABLE IF NOT EXISTS expenses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    amount DECIMAL(10, 2),
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT null
);
"""

incomes = """
CREATE TABLE IF NOT EXISTS incomes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    amount DECIMAL(10, 2),
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT null
);
"""

shared_amount = """
CREATE TABLE IF NOT EXISTS shared_amount (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    amount DECIMAL(10, 2),
    share_user VARCHAR(255),
    give_take givetaketype DEFAULT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT null
);
"""
list_tables_queries = []

# Split the statements by semicolons and execute them one by one
tables = [default, users, expenses, incomes, shared_amount]
for sql_query in tables:
    statements = sql_query.split(";")
    for statement in statements:
        if statement.strip():
            list_tables_queries.append(statement.strip())
