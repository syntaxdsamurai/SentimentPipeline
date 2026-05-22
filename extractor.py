from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')

def get_artist_data(api_key, artist_name):
    youtube = build('youtube', 'v3', developerKey=api_key)
    rows = []

    search_res = youtube.search().list(
        q=artist_name,
        part='snippet',
        maxResults=50,
        type='video'
    ).execute()

    for item in search_res.get('items', []):
        if item['id'].get('videoId') is None:
            continue
        v_id = item['id']['videoId']
        try:
            comment_res = youtube.commentThreads().list(
                part='snippet',
                videoId=v_id,
                maxResults=10,
                textFormat='plainText'
            ).execute()

            for c in comment_res.get('items', []):
                text = c['snippet']['topLevelComment']['snippet']['textDisplay']

                rows.append({
                    "artist": artist_name,
                    "comment": text
                })
        except:
            continue

    return rows
