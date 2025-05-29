from werkzeug.security import generate_password_hash
from app.models import User, Task, Product

def create_test_data(db):
    """Create test data for the test database"""
    
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

    # Create test products
    products = [
        Product(
            name='Test Product 1',
            description='First test product',
            price=99.99,
            stock=10
        ),
        Product(
            name='Test Product 2',
            description='Second test product',
            price=149.99,
            stock=5
        )
    ]

    # Add products to database
    for product in products:
        db.session.add(product)

    db.session.commit() 