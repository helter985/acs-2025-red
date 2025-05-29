import json
import pytest
from app.models import Product, db

def test_get_products(client, sample_product):
    response = client.get('/api/products')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert len(data) == 1
    assert data[0]['name'] == "Test Product"

def test_get_product(client, sample_product):
    response = client.get(f'/api/products/{sample_product.id}')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data['name'] == "Test Product"
    assert data['price'] == 99.99

def test_create_product(client, init_database):
    product_data = {
        'name': 'New Product',
        'description': 'A new test product',
        'price': 199.99,
        'stock': 5
    }
    response = client.post('/api/products',
                          data=json.dumps(product_data).encode('utf-8'),
                          content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data.decode('utf-8'))
    assert data['name'] == 'New Product'
    assert data['price'] == 199.99

def test_update_product(client, sample_product):
    update_data = {
        'name': 'Updated Product',
        'price': 149.99
    }
    response = client.put(f'/api/products/{sample_product.id}',
                         data=json.dumps(update_data).encode('utf-8'),
                         content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data['name'] == 'Updated Product'
    assert data['price'] == 149.99

def test_delete_product(client, sample_product):
    response = client.delete(f'/api/products/{sample_product.id}')
    assert response.status_code == 204
    
    # Verify product was deleted
    response = client.get(f'/api/products/{sample_product.id}')
    assert response.status_code == 404

def test_get_nonexistent_product(client, init_database):
    # Limpiar la base de datos antes del test
    db.session.query(Product).delete()
    db.session.commit()
    response = client.get('/api/products/999')
    assert response.status_code == 404

def test_create_invalid_product(client):
    invalid_product = {
        'name': 'Invalid Product',
        'price': -10.0,
        'stock': 1
    }
    response = client.post('/api/products',
                          data=json.dumps(invalid_product).encode('utf-8'),
                          content_type='application/json')
    assert response.status_code == 400 