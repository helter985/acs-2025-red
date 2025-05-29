from flask import Blueprint, jsonify, request
from ..services import product_service
from ..mapping.product_schema import ProductSchema
from ..models import Product

product_bp = Blueprint('products', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@product_bp.route('/api/products', methods=['GET'])
def get_all_products():
    try:
        products = product_service.get_all_products()
        return jsonify(products_schema.dump(products)), 200
    except Exception as e:
        return jsonify({"message": "An internal error occurred", "error": str(e)}), 500

@product_bp.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = product_service.get_product(product_id)
        if product is None:
            return jsonify({"message": "Product not found"}), 404
        return jsonify(product_schema.dump(product)), 200
    except Exception as e:
        return jsonify({"message": "An internal error occurred", "error": str(e)}), 500

@product_bp.route('/api/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "No input data provided"}), 400

        # Validate required fields and data types
        required_fields = ['name', 'price', 'stock']
        for field in required_fields:
            if field not in data:
                return jsonify({"message": f"Missing required field: {field}"}), 400

        # Validate price and stock
        try:
            if float(data['price']) < 0:
                return jsonify({"message": "Price cannot be negative"}), 400
            if int(data.get('stock', 0)) < 0:
                return jsonify({"message": "Stock cannot be negative"}), 400
        except ValueError:
            return jsonify({"message": "Invalid price or stock value"}), 400

        product = product_service.create_product(data)
        return jsonify(product_schema.dump(product)), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": "An internal error occurred", "error": str(e)}), 500

@product_bp.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "No input data provided"}), 400

        # Validate price if present
        if 'price' in data and float(data['price']) < 0:
            return jsonify({"message": "Price cannot be negative"}), 400
        
        # Validate stock if present
        if 'stock' in data and int(data['stock']) < 0:
            return jsonify({"message": "Stock cannot be negative"}), 400

        product = product_service.update_product(product_id, data)
        if product is None:
            return jsonify({"message": "Product not found"}), 404
        return jsonify(product_schema.dump(product)), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": "An internal error occurred", "error": str(e)}), 500

@product_bp.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        if product_service.delete_product(product_id):
            return '', 204
        return jsonify({"message": "Product not found"}), 404
    except Exception as e:
        return jsonify({"message": "An internal error occurred", "error": str(e)}), 500

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
    
