from flask import Blueprint, jsonify, request
from ..services import product_service
from ..mapping.product_schema import ProductSchema

product_bp = Blueprint('products', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@product_bp.route('/products', methods=['GET'])
def get_all_products():
    try:
        products = product_service.list_products()
        if not products:
            return '', 204 
        return jsonify(products_schema.dump(products)), 200
    except Exception as e:
        return jsonify({"message": "An internal error occurred", "Internal Error": str(e)}), 500

@product_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = product_service.get_product(product_id)
        if not product:
            return jsonify({"message": "Product not found"}), 404
        return jsonify(product_schema.dump(product)), 200
    except Exception as e:
        return jsonify({"message": "An internal error occurred", "Internal Error": str(e)}), 500

@product_bp.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "No input data provided"}), 400

        # Validate required fields
        required_fields = ['name', 'price']
        for field in required_fields:
            if field not in data:
                return jsonify({"message": f"Missing required field: {field}"}), 400

        product = product_service.create_product(data)
        return jsonify(product_schema.dump(product)), 201
    except Exception as e:
        return jsonify({"message": "An internal error occurred", "Internal Error": str(e)}), 500

@product_bp.route('/admin/products-list', methods=['POST'])
def upload_products():
    try:
        if not request.headers.get('Authorization'):
            return jsonify({"message": "Unauthorized"}), 401

        file = request.files.get('file')
        if not file:
            return jsonify({"message": "No file uploaded"}), 400

        success = product_service.upload_products(file)
        if success:
            return jsonify({"message": "Products uploaded successfully"}), 201
        else:
            return jsonify({"message": "Invalid file format"}), 400

    except Exception as e:
        return jsonify({"message": "An internal error occurred", "Internal Error": str(e)}), 500
    
