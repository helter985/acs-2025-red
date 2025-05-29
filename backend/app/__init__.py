from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config.config import Config

# Configurar SQLAlchemy sin opciones de pool para SQLite
db = SQLAlchemy(engine_options={})
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    
    # Import config here to avoid circular imports
    app.config.from_object(config_class)
    
    # Configure JSON responses
    app.config['JSON_AS_ASCII'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models
    from app.models import Product

    # Register blueprints
    from app.resources.product_resource import product_bp
    app.register_blueprint(product_bp)  # Removed url_prefix as it's already in the routes

    # Ensure database connection is working
    with app.app_context():
        try:
            db.engine.connect()
        except Exception as e:
            print(f"Error connecting to database: {str(e)}")
            raise

    return app 