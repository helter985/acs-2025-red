import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from werkzeug.security import generate_password_hash

def create_and_init_db():
    """Create and initialize the database with tables and test data"""
    conn = None
    try:
        # First connect to postgres database to create our database
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Check if our database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname='acs_db'")
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute('CREATE DATABASE acs_db')
            print("Database created successfully!")
        else:
            print("Database already exists.")

        # Close connection to postgres database
        cursor.close()
        conn.close()

        # Connect to our database
        conn = psycopg2.connect(
            dbname='acs_db',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(80) UNIQUE NOT NULL,
                email VARCHAR(120) UNIQUE NOT NULL,
                password_hash VARCHAR(128),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                description TEXT,
                status VARCHAR(20) NOT NULL,
                user_id INTEGER REFERENCES users(id),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT,
                price FLOAT NOT NULL,
                stock INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("Tables created successfully!")

        # Insert test data
        # Test users
        cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES 
                ('testuser1', 'test1@example.com', %s),
                ('testuser2', 'test2@example.com', %s)
            ON CONFLICT (username) DO NOTHING
        """, (
            generate_password_hash('password123'),
            generate_password_hash('password123')
        ))

        # Test tasks
        cursor.execute("""
            INSERT INTO tasks (title, description, status, user_id)
            VALUES 
                ('Complete project documentation', 'Write comprehensive documentation for the project', 'pending', 1),
                ('Implement user authentication', 'Add JWT authentication to the API', 'in_progress', 1),
                ('Write unit tests', 'Create test cases for all endpoints', 'completed', 2)
            ON CONFLICT DO NOTHING
        """)

        # Test products
        cursor.execute("""
            INSERT INTO products (name, description, price, stock)
            VALUES 
                ('Test Product 1', 'First test product', 99.99, 10),
                ('Test Product 2', 'Second test product', 149.99, 5)
            ON CONFLICT DO NOTHING
        """)
        print("Test data created successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    create_and_init_db() 