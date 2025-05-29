from flask import Blueprint, jsonify, request
from app.services.product_service import get_all_products, get_product, create_product, update_product, delete_product

product_bp = Blueprint('product', __name__, url_prefix='/api/products')

@product_bp.route('/', methods=['GET'])
def list_products():
    products = get_all_products()
    return jsonify([product.to_dict() for product in products])

@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = get_product(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product.to_dict())

@product_bp.route('/', methods=['POST'])
def create_new_product():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    try:
        product = create_product(data)
        return jsonify(product.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_existing_product(product_id):
    product = get_product(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    try:
        updated_product = update_product(product_id, data)
        return jsonify(updated_product.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_existing_product(product_id):
    product = get_product(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    if delete_product(product_id):
        return '', 204
    return jsonify({'error': 'Failed to delete product'}), 500 