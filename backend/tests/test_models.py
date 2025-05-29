import pytest
from app.models import Product

def test_create_product(init_database):
    product = Product(
        name="New Product",
        description="A new test product",
        price=199.99,
        stock=5
    )
    init_database.session.add(product)
    init_database.session.commit()

    saved_product = Product.query.filter_by(name="New Product").first()
    assert saved_product is not None
    assert saved_product.name == "New Product"
    assert saved_product.description == "A new test product"
    assert saved_product.price == 199.99
    assert saved_product.stock == 5

def test_update_product(sample_product):
    sample_product.name = "Updated Product"
    sample_product.price = 149.99
    db = sample_product.query.session
    db.commit()

    updated_product = Product.query.get(sample_product.id)
    assert updated_product.name == "Updated Product"
    assert updated_product.price == 149.99

def test_delete_product(sample_product):
    db = sample_product.query.session
    db.delete(sample_product)
    db.commit()

    deleted_product = Product.query.get(sample_product.id)
    assert deleted_product is None

def test_product_price_validation():
    with pytest.raises(ValueError):
        Product(
            name="Invalid Product",
            description="Product with invalid price",
            price=-10.0,
            stock=1
        )

def test_product_stock_validation():
    with pytest.raises(ValueError):
        Product(
            name="Invalid Product",
            description="Product with invalid stock",
            price=10.0,
            stock=-1
        ) 