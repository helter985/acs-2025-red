from app import create_app, db
from app.models import User, Task
from werkzeug.security import generate_password_hash

def init_db():
    app = create_app()
    with app.app_context():
        # Create tables
        db.create_all()

        # Create test users
        users = [
            User(
                username='testuser1',
                email='test1@example.com',
                password_hash=generate_password_hash('password123')
            ),
            User(
                username='testuser2',
                email='test2@example.com',
                password_hash=generate_password_hash('password123')
            )
        ]

        # Add users to database
        for user in users:
            db.session.add(user)
        db.session.commit()

        # Create test tasks
        tasks = [
            Task(
                title='Complete project documentation',
                description='Write comprehensive documentation for the project',
                status='pending',
                user_id=1
            ),
            Task(
                title='Implement user authentication',
                description='Add JWT authentication to the API',
                status='in_progress',
                user_id=1
            ),
            Task(
                title='Write unit tests',
                description='Create test cases for all endpoints',
                status='completed',
                user_id=2
            )
        ]

        # Add tasks to database
        for task in tasks:
            db.session.add(task)
        db.session.commit()

if __name__ == '__main__':
    init_db() 