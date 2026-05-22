import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def process_sentiment(comment_list):
    df = pd.DataFrame(comment_list)

    analyzer = SentimentIntensityAnalyzer()

    df['sentiment_score'] = df['comment'].apply(
        lambda x: analyzer.polarity_scores(str(x))['compound']
    )

    df['verdict'] = df['sentiment_score'].apply(
        lambda s: "positive" if s >= 0.05 else ("negative" if s <= -0.05 else "neutral")
    )

    return df


def save_to_parquet(df, filename="artist_comments.parquet"):
    df.to_parquet(filename, index=False)
    print(f"Successfully saved to {filename}")
