import pytest
from app import create_app, db
from app.models import User, Task

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        # Create all tables
        db.create_all()
        yield app
        # Clean up after tests
        db.session.remove()
        #db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_user(app):
    with app.app_context():
        # Create a test user
        user = User(
            username='testuser',
            email='test@example.com',
            password_hash='hashed_password'
        )
        db.session.add(user)
        db.session.commit()

        # Query the user
        saved_user = User.query.filter_by(username='testuser').first()
        assert saved_user is not None
        assert saved_user.email == 'test@example.com'
        assert saved_user.username == 'testuser'

def test_create_task(app):
    with app.app_context():
        # Create a test user first
        user = User(
            username='taskuser',
            email='task@example.com',
            password_hash='hashed_password'
        )
        db.session.add(user)
        db.session.commit()

        # Create a task for the user
        task = Task(
            title='Test Task',
            description='This is a test task',
            status='pending',
            user_id=user.id
        )
        db.session.add(task)
        db.session.commit()

        # Query the task
        saved_task = Task.query.filter_by(title='Test Task').first()
        assert saved_task is not None
        assert saved_task.description == 'This is a test task'
        assert saved_task.status == 'pending'
        assert saved_task.user_id == user.id

def test_user_task_relationship(app):
    with app.app_context():
        # Create a test user
        user = User(
            username='reluser',
            email='rel@example.com',
            password_hash='hashed_password'
        )
        db.session.add(user)
        db.session.commit()

        # Create multiple tasks for the user
        task1 = Task(title='Task 1', user_id=user.id)
        task2 = Task(title='Task 2', user_id=user.id)
        db.session.add_all([task1, task2])
        db.session.commit()

        # Test the relationship
        assert len(user.tasks) == 2
        assert user.tasks[0].title == 'Task 1'
        assert user.tasks[1].title == 'Task 2'
        assert task1.user.username == 'reluser'
        assert task2.user.username == 'reluser' 