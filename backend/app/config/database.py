from app import create_app, db

def init_db():
    """Initialize the database with tables"""
    app = create_app()
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    init_db() 