from ..repositories import product_repository
from ..models.product_model import Product

def list_products(nombre=None):
    try:
        if nombre:
            products = product_repository.get_by_nombre(nombre)
        else:
            products = product_repository.get_all()
        
        # Si los productos son diccionarios (como en los tests), los devolvemos tal cual
        if products and isinstance(products[0], dict):
            return products
        return products
    except Exception as e:
        raise Exception("Error interno del servidor")

def get_product(codigo):
    try:
        product = product_repository.get_by_codigo(codigo)
        # Si el producto es un diccionario (como en los tests), lo devolvemos tal cual
        if isinstance(product, dict):
            return product
        return product
    except Exception as e:
        raise Exception("Error interno del servidor")

def create_product(data):
    product = Product(
        codigo=data['codigo'],
        nombre=data['nombre'],
        precio=data['precio'],
        imagen_url=data.get('imagen_url'),
        ultima_actualizacion=data.get('ultima_actualizacion')
    )
    return product_repository.save(product)

def update_product(codigo, data):
    product = get_product(codigo)
    if not product:
        return None
    product.nombre = data.get('nombre', product.nombre)
    product.precio = data.get('precio', product.precio)
    product.imagen_url = data.get('imagen_url', product.imagen_url)
    product.ultima_actualizacion = data.get('ultima_actualizacion', product.ultima_actualizacion)
    product_repository.update()
    return product

def delete_product(codigo):
    product = get_product(codigo)
    if not product:
        return False
    product_repository.delete(product)
    return True

def upload_products(file):
    try:
        if not file:
            return False
        # Aquí deberías implementar la lógica para procesar el archivo Excel
        return True
    except Exception:
        return False
