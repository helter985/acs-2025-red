from flask import Flask
from app.config.config import Config
from app.models.product_model import db
from app.resources.product_resource import product_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(product_bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)