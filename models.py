from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Video(db.Model):
    __tablename__ = 'video'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    publish_datetime = db.Column(db.DateTime, nullable=False)
    thumbnail_url = db.Column(db.String(255))
    video_id = db.Column(db.String(255))

    def __repr__(self):
        return f"<Video {self.title}>"
