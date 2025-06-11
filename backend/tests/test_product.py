import pytest
from app import create_app
from unittest.mock import patch, Mock
import io

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        yield client

def create_test_file():
    return (io.BytesIO(b"test file content"), "test.xlsx")

# Helper para generar archivos de prueba
def generate_excel_file():
    return io.BytesIO(b'test excel content')

def generate_text_file():
    return io.BytesIO(b'test text content')

# ---------- /productos GET ----------

@patch('app.services.product_service.list_products')
def test_get_all_products_success(mock_list_products, client):
    expected_products = [
        {"codigo": "P001", "nombre": "Producto 1", "precio": 100.0, "imagen_url": "http://example.com/img1", "ultima_actualizacion": "2023-01-01"}
    ]
    mock_list_products.return_value = expected_products
    response = client.get('/api/productos')
    assert response.status_code == 200
    assert response.json == expected_products

@patch('app.services.product_service.list_products')
def test_get_all_products_empty(mock_list_products, client):
    mock_list_products.return_value = []
    response = client.get('/api/productos')
    assert response.status_code == 204

@patch('app.services.product_service.list_products')
def test_get_all_products_error(mock_list_products, client):
    mock_list_products.side_effect = Exception("Error de prueba")
    response = client.get('/api/productos')
    assert response.status_code == 500

# ---------- /productos/<codigo> GET ----------

@patch('app.services.product_service.get_product')
def test_get_product_success(mock_get_product, client):
    expected_product = {
        "codigo": "P001",
        "nombre": "Producto 1",
        "precio": 100.0,
        "imagen_url": "http://example.com/img1",
        "ultima_actualizacion": "2023-01-01"
    }
    mock_get_product.return_value = expected_product
    response = client.get('/api/productos/P001')
    assert response.status_code == 200
    assert response.json == expected_product

@patch('app.services.product_service.get_product')
def test_get_product_not_found(mock_get_product, client):
    mock_get_product.return_value = None
    response = client.get('/api/productos/P001')
    assert response.status_code == 404

@patch('app.services.product_service.get_product')
def test_get_product_error(mock_get_product, client):
    mock_get_product.side_effect = Exception("Error de prueba")
    response = client.get('/api/productos/P001')
    assert response.status_code == 500

# ---------- /admin/lista-precios POST ----------

@patch('app.services.product_service.upload_products')
def test_upload_lista_precios_success(mock_upload_products, client):
    mock_upload_products.return_value = True
    test_file = create_test_file()
    response = client.post(
        '/api/admin/lista-precios',
        data={'archivo': test_file},
        headers={'Authorization': 'Bearer test-token'}
    )
    assert response.status_code == 201

@patch('app.services.product_service.upload_products')
def test_upload_lista_precios_invalid_file(mock_upload_products, client):
    test_file = (io.BytesIO(b"test file content"), "test.txt")
    response = client.post(
        '/api/admin/lista-precios',
        data={'archivo': test_file},
        headers={'Authorization': 'Bearer test-token'}
    )
    assert response.status_code == 400

@patch('app.services.product_service.upload_products')
def test_upload_lista_precios_no_auth(mock_upload_products, client):
    test_file = create_test_file()
    response = client.post(
        '/api/admin/lista-precios',
        data={'archivo': test_file}
    )
    assert response.status_code == 401

@patch('app.services.product_service.upload_products')
def test_upload_lista_precios_server_error(mock_upload_products, client):
    mock_upload_products.side_effect = Exception("Error de prueba")
    test_file = create_test_file()
    response = client.post(
        '/api/admin/lista-precios',
        data={'archivo': test_file},
        headers={'Authorization': 'Bearer test-token'}
    )
    assert response.status_code == 500