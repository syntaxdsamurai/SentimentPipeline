import os
from dotenv import load_dotenv
from extractor import get_artist_data
from processor import process_sentiment, save_to_parquet

load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')

artists = ["Laufey", "21 Pilots", "Beabadoobee", "Mitski"]
all_data = []

for artist in artists:
    print(f"Fetching data for: {artist}...")
    artist_rows = get_artist_data(API_KEY, artist)
    all_data.extend(artist_rows)

df = process_sentiment(all_data)

print("\n--- PROCESSED DATAFRAME (First 5 Rows) ---")
print(df.head())

print("\n--- AVERAGE SENTIMENT PER ARTIST ---")
summary = df.groupby('artist').agg(
    avg_sentiment=('sentiment_score', 'mean'),
    total_comments=('comment', 'count'),
    positive=('verdict', lambda x: (x == 'positive').sum()),
    negative=('verdict', lambda x: (x == 'negative').sum()),
    neutral=('verdict', lambda x: (x == 'neutral').sum())
).reset_index()

print(summary)
save_to_parquet(df, "artist_sentiment_data.parquet")
