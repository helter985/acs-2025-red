from flask import Blueprint
from flask_restful import Api
from .resources.product_resource import ProductResource, ProductByCodeResource, ListaPreciosResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Rutas de productos
api.add_resource(ProductResource, '/productos')
api.add_resource(ProductByCodeResource, '/productos/<string:codigo>')
api.add_resource(ListaPreciosResource, '/admin/lista-precios') 