from ..repositories import product_repository
from ..models.product_model import Product

def list_products():
    return product_repository.get_all()

def get_product(product_id):
    return product_repository.get_by_id(product_id)

def create_product(data):
    product = Product(name=data['name'], price=data['price'])
    return product_repository.save(product)

def update_product(product_id, data):
    product = get_product(product_id)
    product.name = data['name']
    product.price = data['price']
    product_repository.update()
    return product

def delete_product(product_id):
    product = get_product(product_id)
    product_repository.delete(product)
    return True
