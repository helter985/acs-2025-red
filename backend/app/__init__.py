from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Import config here to avoid circular imports
    from app.config.config import Config, TestConfig
    
    # Select configuration based on environment
    if config_name == 'testing':
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models
    from app.models import User, Task, Product

    # Register blueprints
    from app.resources.user_resource import user_bp
    from app.resources.task_resource import task_bp
    from app.resources.product_resource import product_bp
    
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(task_bp, url_prefix="/api/tasks")
    app.register_blueprint(product_bp)  # Sin url_prefix, rutas como /products

    return app 