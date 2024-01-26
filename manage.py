from app import app, db
from models import Video

def initialize_database():
    with app.app_context():
        db.create_all()

        if not hasattr(Video, 'video_id'):
            db.session.execute('ALTER TABLE video ADD COLUMN video_id VARCHAR(255)')
            db.session.commit()

if __name__ == "__main__":
    initialize_database()
