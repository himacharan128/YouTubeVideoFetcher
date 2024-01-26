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
        published_after = datetime.utcnow().replace(tzinfo=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        url = f'https://www.googleapis.com/youtube/v3/search?type=video&order=date&publishedAfter={published_after}&q={search_query}&key={api_key}'
        print("YouTube API Request URL:", url)
        response = requests.get(url)
        data = response.json()
        print("YouTube API Response:", data)

        if 'items' not in data:
            print("No 'items' field found in the YouTube API response.")
            return

        items = data['items']
        if not items:
            print("No items found in the YouTube API response.")
            return

        with current_app.app_context():
            for item in items:
                video_id = item['id']['videoId']
                snippet = item.get('snippet', {})
                if not snippet:
                    print("No 'snippet' field found in an item.")
                    continue

                video = Video(
                    title=snippet.get('title', ''),
                    description=snippet.get('description', ''),
                    publish_datetime=datetime.strptime(snippet.get('publishedAt', ''), '%Y-%m-%dT%H:%M:%SZ'),
                    thumbnail_url=snippet.get('thumbnails', {}).get('default', {}).get('url', ''),
                    video_id=video_id
                )
                db.session.add(video)

            db.session.commit()
    except Exception as e:
        print("Error during YouTube API request:", str(e))
