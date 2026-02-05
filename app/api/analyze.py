from fastapi import APIRouter, HTTPException
from app.services.data.market_data import get_historical_prices
from app.services.kpis.returns import calculate_returns
from app.services.kpis.volatility import calculate_volatility
from app.services.kpis.momentum import calculate_rsi
from app.services.kpis.signals import rsi_signal, trend_signal, sma_crossover
from app.services.kpis.trend import detect_trend
from app.services.kpis.scoring import z_score_regressors, probability_up, convert_score

router = APIRouter()

@router.get("/analyze")
def analyze(ticker:str):
    try:
        print("➡️ Analyze started")

        prices = get_historical_prices(ticker)
        print("✅ Prices fetched")

        returns = calculate_returns(prices)
        print("✅ Returns calculated")

        volatility = calculate_volatility(prices, ticker)
        print("✅ Volatility calculated")

        rsi = calculate_rsi(prices, ticker)
        print("✅ RSI calculated")
        
        rsi_status = rsi_signal(rsi["rsi_val"])
        print("✅ RSI status detected")

        trend = detect_trend(prices, ticker)
        print("✅ Trend detected")

        trend_sig = trend_signal(trend)
        print("✅ Trend status detected")

        sma_crossover_signal = sma_crossover(prices, ticker)
        print("✅ SMA crossover detected")

        action_score = z_score_regressors(rsi["rsi_val"], trend["trend_val"], volatility["vol_val"],
                   rsi["rsi_mean"], rsi["rsi_std"], trend["trend_mean"], trend["trend_std"], volatility["vol_mean"], volatility["vol_std"])
        prob_up = probability_up(action_score["rsi_z"], action_score["trend_z"], action_score["val_z"])
        action = convert_score(prob_up)
        print("✅ Buy/Hold/Avoid action detected")

        return{
            "ticker":ticker,
            "returns":returns,
            "volatility":volatility,
            "rsi": rsi,
            "rsi status": rsi_status,
            "trend": trend,
            "trend_signal": trend_sig,
            "sma crossover signal": sma_crossover_signal,
            "probability up": prob_up,
            "action": action,
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    