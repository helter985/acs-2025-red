from flask import Blueprint, jsonify, request
from ..services import product_service
from ..mapping.product_schema import ProductSchema

product_bp = Blueprint('products', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@product_bp.route('/products', methods=['GET'])
def get_all_products():
    products = product_service.list_products()
    return jsonify(products_schema.dump(products))

@product_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product(product_id)
    return jsonify(product_schema.dump(product))

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
        return jsonify({"message": "An error occurred", "Internal Error": str(e)}), 500