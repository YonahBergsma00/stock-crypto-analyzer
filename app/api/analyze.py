from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
import os

from app.services.data.market_data import get_historical_prices
from app.services.data.news_data import fetch_news

from app.services.kpis.News_sentiment import calculate_news_sentiment
from app.services.kpis.volatility import calculate_volatility
from app.services.kpis.RSI import calculate_rsi
from app.services.kpis.trend import calculate_trend
from app.services.kpis.Crossover import calculate_crossover

from app.services.kpis.returns import calculate_returns
from app.services.kpis.signals import rsi_signal, trend_signal, market_signal, crossover_signal

from app.services.decision_engine.scoring import z_score_regressors, probability_up
from app.services.decision_engine.recommendation import convert_score

router = APIRouter()

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
print("Loaded API key:", NEWS_API_KEY)

@router.get("/analyze")
def analyze(ticker:str):
    try:
        print("➡️ Analyze started")

        prices = get_historical_prices(ticker)
        print("✅ Prices fetched")

        news_data = fetch_news(ticker, NEWS_API_KEY)
        print(f"✅ News data fetched (number of headlines: {len(news_data)})")

        returns = calculate_returns(prices)
        print("✅ Returns calculated")

        volatility = calculate_volatility(prices, ticker)
        print("✅ Volatility calculated")

        rsi = calculate_rsi(prices, ticker)
        print("✅ RSI calculated")
        
        rsi_sig = rsi_signal(prices, ticker)
        print("✅ RSI signal detected")

        trend = calculate_trend(prices, ticker)
        print("✅ Trend calculated")

        trend_sig = trend_signal(prices, ticker)
        print("✅ Trend signal detected")

        market_sig = market_signal(trend_sig)
        print("✅ Market signal detected")

        news_sentiment = calculate_news_sentiment(news_data)
        print("✅ News sentiment calculated")

        crossover = calculate_crossover(prices, ticker)
        print("✅ Crossover calculated")

        crossover_sig = crossover_signal(prices, ticker)
        print("✅ Crossover signal detected")


        kpis = {
            "rsi": rsi,
            "trend": trend,
            "vol": volatility,
            "sentiment": news_sentiment,
            "crossover": crossover,
        }

        weights = {
            "rsi_w": 0.2,
            "trend_w": 0.2,
            "vol_w": 0.2,
            "sentiment_w": 0.2,
            "crossover_w": 0.2,
        }

        kpi_z_scores = z_score_regressors(kpis)
        prob_up = probability_up(kpi_z_scores, weights)
        action = convert_score(prob_up)
        print("✅ Buy/Hold/Avoid action detected")

        return{
            "ticker":ticker,
            "returns":returns,

            "kpis":{
                "rsi": rsi,
                "trend": trend,
                "volatility":volatility,
                "news sentiment": news_sentiment,
                "crossover": crossover,
            },    

            "signals":{
                "rsi status": rsi_sig,
                "trend signal": trend_sig,
                "market signal": market_sig,
                "crossover signal": crossover_sig
            },
            
            "probability up": prob_up,
            "action": action,
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    