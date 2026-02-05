from fastapi import APIRouter, HTTPException
from app.services.data.market_data import get_historical_prices
from app.services.kpis.returns import calculate_returns
from app.services.kpis.volatility import calculate_volatility
from app.services.kpis.momentum import calculate_rsi
from app.services.kpis.signals import rsi_signal

router = APIRouter()

@router.get("/analyze")
def analyze(ticker:str):
    try:
        print("➡️ Analyze started")

        prices = get_historical_prices(ticker)
        print("✅ Prices fetched")

        returns = calculate_returns(prices)
        print("✅ Returns calculated")

        volatility = calculate_volatility(prices)
        print("✅ Volatility calculated")

        rsi = calculate_rsi(prices, ticker)
        print("✅ RSI calculated")
        
        rsi_status = rsi_signal(rsi)
        print("✅ RSI status calculated")
    
        return{
            "ticker":ticker,
            "returns":returns,
            "volatility":volatility,
            "rsi": {
                "value": rsi,
                "signal": rsi_status,
            }
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    