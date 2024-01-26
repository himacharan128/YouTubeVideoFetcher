from app import app, db

def initialize_database():
    with app.app_context():
        db.create_all()
        db.session.commit()

if __name__ == "__main__":
    initialize_database()
