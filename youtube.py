from datetime import datetime, timezone
import requests
from models import db, Video
from config import Config
from flask import Flask, current_app

current_app = Flask(__name__)
current_app.config.from_object(Config)

current_api_key = 0

def get_next_api_key():
    global current_api_key
    current_api_key = (current_api_key + 1) % len(Config.API_KEYS)
    return Config.API_KEYS[current_api_key]



def fetch_and_store_videos(search_query):
    try:
        api_key = get_next_api_key()
        published_after = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat() + 'Z'
        url = f'https://www.googleapis.com/youtube/v3/search?type=video&order=date&publishedAfter={published_after}&q={search_query}&key={api_key}'
        print("YouTube API Request URL:", url)
        response = requests.get(url)
        data = response.json()
        with current_app.app_context():
            for item in data.get('items', []):
                video = Video(
                    title=item['snippet']['title'],
                    description=item['snippet']['description'],
                    publish_datetime=datetime.strptime(item['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
                    thumbnail_url=item['snippet']['thumbnails']['default']['url']
                )
                db.session.add(video)
            db.session.commit()
    except Exception as e:
        print("Error during YouTube API request:", str(e))

