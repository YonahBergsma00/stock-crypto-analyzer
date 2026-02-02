import pandas as pd

def calculate_returns(prices: pd.Series) -> dict:
    return{
        "7d": round(prices.pct_change(7).iloc[-1], 4),
        "30d": round(prices.pct_change(30).iloc[-1], 4),
        "90d": round(prices.pct_change(90).iloc[-1], 4),
    }


