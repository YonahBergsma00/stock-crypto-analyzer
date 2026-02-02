import pandas as pd

def calculate_returns(prices: pd.Series) -> dict:
    return{
        "7d": prices.pct_change(7).iloc[-1],
        "30d": prices.pct_change(30).iloc[-1],
        "90d": prices.pct_change(90).iloc[-1]
    }


