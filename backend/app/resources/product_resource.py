from flask import Blueprint, jsonify, request
from ..services import product_service
from ..mapping.product_schema import ProductSchema
from flask_restful import Resource
from ..utils.auth import token_required

product_bp = Blueprint('products', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class ProductResource(Resource):
    def get(self):
        try:
            nombre = request.args.get('nombre')
            products = product_service.list_products(nombre)
            
            if not products:
                return '', 204
            
            # Serializar la lista de productos
            result = product_schema.dump_many(products)
            return result, 200
        except Exception as e:
            return {'error': str(e)}, 500

class ProductByCodeResource(Resource):
    def get(self, codigo):
        try:
            product = product_service.get_product(codigo)
            if not product:
                return {'error': 'Producto no encontrado'}, 404
            
            result = product_schema.dump(product)
            return result, 200
        except Exception as e:
            return {'error': str(e)}, 500

class ListaPreciosResource(Resource):
    @token_required
    def post(self):
        try:
            if 'archivo' not in request.files:
                return {'error': 'No se proporcionó ningún archivo'}, 400
            
            file = request.files['archivo']
            if not file.filename.endswith('.xlsx'):
                return {'error': 'El archivo debe ser de tipo Excel (.xlsx)'}, 400
            
            if product_service.upload_products(file):
                return {'message': 'Lista de precios actualizada correctamente'}, 201
            return {'error': 'Error al procesar el archivo'}, 500
        except Exception as e:
            return {'error': str(e)}, 500
    
