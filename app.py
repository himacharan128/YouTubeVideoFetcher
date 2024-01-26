from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from gevent.pywsgi import WSGIServer
import atexit
from models import db, Video
from youtube import fetch_and_store_videos
from config import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate= Migrate(app,db)

scheduler = BackgroundScheduler()
scheduler.start()

def scheduled_job():
    search_query = 'latest news'
    fetch_and_store_videos(search_query)

scheduler.add_job(
    func=scheduled_job,
    trigger=IntervalTrigger(seconds=10),
    id='fetch_and_store_videos',
    name='Fetch and Store Videos',
    replace_existing=True,
)
atexit.register(lambda: scheduler.shutdown())

@app.route('/videos', methods=['GET'])
def get_videos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    videos = Video.query.order_by(Video.publish_datetime.desc()).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'videos': [
            {
                'title': video.title,
                'description': video.description,
                'publish_datetime': video.publish_datetime.isoformat(),
                'thumbnail_url': video.thumbnail_url
            } for video in videos.items
        ],
        'page': videos.page,
        'per_page': videos.per_page,
        'total_pages': videos.pages,
        'total_items': videos.total
    })

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()