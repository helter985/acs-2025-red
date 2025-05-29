from app.models import Product, db
from sqlalchemy.exc import NoResultFound

def get_product(product_id):
    try:
        product = db.session.get(Product, product_id)
        if product is None:
            return None
        return product
    except Exception as e:
        db.session.rollback()
        raise e

def get_all_products():
    return Product.query.all()

def create_product(data):
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return product

def update_product(product_id, data):
    product = get_product(product_id)
    if product:
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
    return product

def delete_product(product_id):
    product = get_product(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return True
    return False
