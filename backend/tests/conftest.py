import pytest
from app import create_app, db
from app.config.config import TestConfig
from app.models import Product

@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def init_database(app):
    """Fixture que crea una base de datos en memoria para cada test"""
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        
        yield db
        
        # Limpiar después de cada test
        db.session.remove()
        db.drop_all()

@pytest.fixture
def sample_product(init_database):
    """Fixture que crea un producto de prueba"""
    product = Product(
        name="Test Product",
        description="This is a test product",
        price=99.99,
        stock=10
    )
    db.session.add(product)
    db.session.commit()
    return product 