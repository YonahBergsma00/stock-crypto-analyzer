import numpy as np
import pandas as pd

def calculate_volatility(prices: pd.Series) -> float:
    """
    Annualized volatility based on daily returns.
    """

    daily_returns = prices.pct_change().dropna()
    volatility = daily_returns.std() * np.sqrt(252) #approximately 252 tradingdays annually

    return round(volatility, 4)