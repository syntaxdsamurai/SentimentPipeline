# Sentiment Analyzer 

A Python data pipeline that fetches real YouTube comments and analyzes sentiment across music artist fanbases.

## What it does
- Fetches ~500 YouTube comments per artist using YouTube Data API v3
- Runs sentiment analysis using VADER (optimized for social media language)
- Aggregates results per artist — avg sentiment, positive/negative/neutral breakdown
- Saves full results as Parquet

## Results

| Artist | Avg Sentiment | Positive | Negative | Neutral |
|--------|--------------|----------|----------|---------|
| Laufey | 0.271 | 253 | 71 | 156 |
| Beabadoobee | 0.223 | 212 | 68 | 162 |
| 21 Pilots | 0.183 | 207 | 81 | 212 |
| Mitski | 0.097 | 181 | 125 | 184 |

**Key insight:** Mitski fans show significantly higher negative sentiment — likely reflecting the emotional weight of her music attracting a more melancholic audience.

## Project Structure

    ├── extractor.py       # YouTube API calls, comment fetching
    ├── processor.py       # VADER sentiment scoring + Parquet save
    ├── main.py            # Pipeline orchestration + summary
    ├── .env               # API keys (not committed)
    └── requirements.txt   # Dependencies

## Tech Stack
- Python 3.14
- Pandas
- VADER Sentiment
- YouTube Data API v3
- PyArrow (Parquet)
- python-dotenv

## Setup

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file and add: `YOUTUBE_API_KEY=your_key_here`
4. Run: `python main.py`

## Limitations
- VADER struggles with non-English comments (Spanish, Korean etc.)
- YouTube API quota limits daily comment fetching
- Short comments like emojis often score as neutral
