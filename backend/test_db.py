from app import create_app, db
from app.models import Product

def test_database():
    app = create_app()
    with app.app_context():
        # Create a test product
        product = Product(
            name="Test Product",
            description="This is a test product",
            price=99.99,
            stock=10
        )
        
        try:
            # Add and commit the product
            db.session.add(product)
            db.session.commit()
            print("✅ Product created successfully!")
            
            # Query the product
            saved_product = Product.query.first()
            print(f"✅ Product retrieved: {saved_product.name}")
            
            # Clean up
            db.session.delete(saved_product)
            db.session.commit()
            print("✅ Test cleanup completed")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            db.session.rollback()

if __name__ == "__main__":
    test_database() 