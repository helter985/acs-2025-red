from ..models.product_model import Product, db

def get_all():
    return Product.query.all()

def get_by_id(product_id):
    return Product.query.get_or_404(product_id)

def save(product):
    db.session.add(product)
    db.session.commit()
    return product

def update():
    db.session.commit()

def delete(product):
    db.session.delete(product)
    db.session.commit()
