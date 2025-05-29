from ..repositories import product_repository
from ..models.product_model import Product

def list_products(nombre=None):
    if nombre:
        return product_repository.get_by_nombre(nombre)
    return product_repository.get_all()

def get_product(codigo):
    return product_repository.get_by_codigo(codigo)

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
