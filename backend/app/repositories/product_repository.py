from ..models.product_model import Product, db

def get_all():
    return Product.query.all()

def get_by_codigo(codigo):
    return Product.query.filter_by(codigo=codigo).first()

def get_by_nombre(nombre):
    return Product.query.filter(Product.nombre.ilike(f"%{nombre}%")).all()

def save(product):
    db.session.add(product)
    db.session.commit()
    return product

def update():
    db.session.commit()

def delete(product):
    db.session.delete(product)
    db.session.commit()
