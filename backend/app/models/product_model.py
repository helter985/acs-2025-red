from datetime import date
from app import db

class Product(db.Model):
    __tablename__ = 'products'

    codigo = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    imagen_url = db.Column(db.String)
    ultima_actualizacion = db.Column(db.Date, default=date.today)

    def __repr__(self):
        return f'<Product {self.nombre}>'