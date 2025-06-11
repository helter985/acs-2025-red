import pytest
from unittest.mock import patch, MagicMock
from app.services.product_service import list_products, get_product, create_product, update_product, delete_product, upload_products
from app.models.product_model import Product

# Test para list_products
def test_list_products_with_nombre():
    with patch('app.repositories.product_repository.get_by_nombre') as mock_get_by_nombre:
        mock_get_by_nombre.return_value = [
            {"codigo": "P001", "nombre": "Producto 1", "precio": 100.0}
        ]
        result = list_products(nombre="Producto 1")
        assert result == [{"codigo": "P001", "nombre": "Producto 1", "precio": 100.0}]
        mock_get_by_nombre.assert_called_once_with("Producto 1")

def test_list_products_without_nombre():
    with patch('app.repositories.product_repository.get_all') as mock_get_all:
        mock_get_all.return_value = [
            {"codigo": "P001", "nombre": "Producto 1", "precio": 100.0}
        ]
        result = list_products()
        assert result == [{"codigo": "P001", "nombre": "Producto 1", "precio": 100.0}]
        mock_get_all.assert_called_once()

def test_list_products_error():
    with patch('app.repositories.product_repository.get_all') as mock_get_all:
        mock_get_all.side_effect = Exception("Error de prueba")
        with pytest.raises(Exception) as exc_info:
            list_products()
        assert str(exc_info.value) == "Error interno del servidor"

# Test para get_product
def test_get_product_success():
    with patch('app.repositories.product_repository.get_by_codigo') as mock_get_by_codigo:
        mock_get_by_codigo.return_value = {"codigo": "P001", "nombre": "Producto 1", "precio": 100.0}
        result = get_product("P001")
        assert result == {"codigo": "P001", "nombre": "Producto 1", "precio": 100.0}
        mock_get_by_codigo.assert_called_once_with("P001")

def test_get_product_error():
    with patch('app.repositories.product_repository.get_by_codigo') as mock_get_by_codigo:
        mock_get_by_codigo.side_effect = Exception("Error de prueba")
        with pytest.raises(Exception) as exc_info:
            get_product("P001")
        assert str(exc_info.value) == "Error interno del servidor"

# Test para create_product
def test_create_product_success():
    with patch('app.repositories.product_repository.save') as mock_save:
        test_data = {
            'codigo': 'P001',
            'nombre': 'Producto 1',
            'precio': 100.0,
            'imagen_url': 'http://example.com/img1',
            'ultima_actualizacion': '2023-01-01'
        }
        mock_product = Product(**test_data)
        mock_save.return_value = mock_product
        
        result = create_product(test_data)
        assert isinstance(result, Product)
        assert result.codigo == test_data['codigo']
        assert result.nombre == test_data['nombre']
        assert result.precio == test_data['precio']
        mock_save.assert_called_once()

# Test para update_product
def test_update_product_success():
    with patch('app.services.product_service.get_product') as mock_get_product:
        with patch('app.repositories.product_repository.update') as mock_update:
            existing_product = Product(
                codigo='P001',
                nombre='Producto Original',
                precio=100.0
            )
            mock_get_product.return_value = existing_product
            
            update_data = {
                'nombre': 'Producto Actualizado',
                'precio': 150.0
            }
            
            result = update_product('P001', update_data)
            assert result.nombre == update_data['nombre']
            assert result.precio == update_data['precio']
            mock_update.assert_called_once()

def test_update_product_not_found():
    with patch('app.services.product_service.get_product') as mock_get_product:
        mock_get_product.return_value = None
        result = update_product('P001', {'nombre': 'Nuevo Nombre'})
        assert result is None

# Test para delete_product
def test_delete_product_success():
    with patch('app.services.product_service.get_product') as mock_get_product:
        with patch('app.repositories.product_repository.delete') as mock_delete:
            mock_product = Product(codigo='P001', nombre='Producto 1', precio=100.0)
            mock_get_product.return_value = mock_product
            
            result = delete_product('P001')
            assert result is True
            mock_delete.assert_called_once_with(mock_product)

def test_delete_product_not_found():
    with patch('app.services.product_service.get_product') as mock_get_product:
        mock_get_product.return_value = None
        result = delete_product('P001')
        assert result is False

# Test para upload_products
def test_upload_products_success():
    mock_file = MagicMock()
    result = upload_products(mock_file)
    assert result is True

def test_upload_products_no_file():
    result = upload_products(None)
    assert result is False