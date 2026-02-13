from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np

def calculate_news_sentiment(headlines:list) -> dict:

    analyzer = SentimentIntensityAnalyzer()
    scores = [analyzer.polarity_scores(h)["compound"] for h in headlines]

    latest_sentiment = float(np.mean(scores))
    mean_sentiment = float(np.mean(scores))
    std_sentiment = float(np.std(scores))

    return {
        "latest": latest_sentiment,
        "mean": mean_sentiment,
        "std": std_sentiment
    }