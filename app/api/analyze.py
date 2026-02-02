from fastapi import APIRouter, HTTPException
from app.services.data.market_data import get_historical_prices
from app.services.kpis.returns import calculate_returns
from app.services.kpis.volatility import calculate_volatility

router = APIRouter()

@router.get("/analyze")
def analyze(ticker:str):
    try:
        prices = get_historical_prices(ticker)
        returns = calculate_returns(prices)
        volatility = calculate_volatility(prices)
    
        return{
            "ticker":ticker,
            "returns":returns,
            "volatility":volatility,
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    