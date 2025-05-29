import pytest
from app import create_app, db
from app.models import User, Task
from datetime import datetime

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_user(app):
    """Test 1: Crear un usuario y verificar sus atributos"""
    with app.app_context():
        user = User(
            username='testuser',
            email='test@example.com',
            password_hash='hashed_password'
        )
        db.session.add(user)
        db.session.commit()
        
        saved_user = User.query.filter_by(username='testuser').first()
        assert saved_user is not None
        assert saved_user.email == 'test@example.com'
        assert saved_user.username == 'testuser'

def test_create_task(app):
    """Test 2: Crear una tarea y verificar su relación con el usuario"""
    with app.app_context():
        # Crear usuario primero
        user = User(username='taskuser', email='task@example.com', password_hash='hash')
        db.session.add(user)
        db.session.commit()
        
        # Crear tarea
        task = Task(
            title='Test Task',
            description='Test Description',
            status='pending',
            user_id=user.id
        )
        db.session.add(task)
        db.session.commit()
        
        saved_task = Task.query.filter_by(title='Test Task').first()
        assert saved_task is not None
        assert saved_task.description == 'Test Description'
        assert saved_task.status == 'pending'
        assert saved_task.user_id == user.id

def test_user_task_relationship(app):
    """Test 3: Verificar la relación entre usuario y tareas"""
    with app.app_context():
        # Crear usuario
        user = User(username='reluser', email='rel@example.com', password_hash='hash')
        db.session.add(user)
        db.session.commit()
        
        # Crear múltiples tareas para el usuario
        task1 = Task(title='Task 1', user_id=user.id)
        task2 = Task(title='Task 2', user_id=user.id)
        db.session.add_all([task1, task2])
        db.session.commit()
        
        # Verificar que el usuario tiene las tareas correctas
        assert len(user.tasks) == 2
        assert any(task.title == 'Task 1' for task in user.tasks)
        assert any(task.title == 'Task 2' for task in user.tasks)

def test_task_status_update(app):
    """Test 4: Actualizar el estado de una tarea"""
    with app.app_context():
        # Crear usuario y tarea
        user = User(username='statususer', email='status@example.com', password_hash='hash')
        db.session.add(user)
        db.session.commit()
        
        task = Task(title='Status Task', user_id=user.id, status='pending')
        db.session.add(task)
        db.session.commit()
        
        # Actualizar estado
        task.status = 'completed'
        db.session.commit()
        
        # Verificar actualización
        updated_task = Task.query.filter_by(title='Status Task').first()
        assert updated_task.status == 'completed' 