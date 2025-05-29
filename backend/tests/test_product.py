import pytest
from app import create_app, db
from app.models import Product

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_product(app, client):
    # Test POST /products para crear un producto
    payload = {
        "codigo": "P001",
        "nombre": "Producto Test",
        "precio": 99.99,
        "imagen_url": "http://example.com/img.png",
        "ultima_actualizacion": "2024-05-29"
    }
    response = client.post('/products', json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data['codigo'] == "P001"
    assert data['nombre'] == "Producto Test"

def test_get_product(app, client):
    # Primero, crear el producto directamente en la base de datos
    with app.app_context():
        product = Product(
            codigo='P001',
            nombre='Producto Test',
            precio=99.99,
            imagen_url='http://example.com/img.png',
            ultima_actualizacion='2024-05-29'
        )
        db.session.add(product)
        db.session.commit()

    # Test GET /products
    response = client.get('/products')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert any(p['codigo'] == 'P001' for p in data)

    # Test GET /products/P001
    response = client.get('/products/P001')
    assert response.status_code == 200
    data = response.get_json()
    assert data['codigo'] == 'P001'
    assert data['nombre'] == 'Producto Test'

def test_get_product_empty(client):
    # Si no hay productos, debe devolver 204
    response = client.get('/products')
    assert response.status_code == 204
