from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Import config here to avoid circular imports
    from app.config.config import Config
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models
    from app.models import Product

    # Register blueprints
    from app.resources.product_resource import product_bp
    app.register_blueprint(product_bp, url_prefix="/api")

    return app 