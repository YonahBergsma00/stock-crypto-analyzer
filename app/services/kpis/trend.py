import pandas as pd

def calculate_trend(prices: pd.Series, ticker: str, short_window: int = 20, long_window: int= 50) -> dict:
    """
    Detect the trend of a ticker using Simple Moving Average short/long window.
    """
    
    # Calculate SMAs
    sma_short = prices.rolling(window=short_window).mean()
    sma_long = prices.rolling(window=long_window).mean()

    # Calculate trend strength series
    strength_series = (sma_short[ticker] - sma_long[ticker]) / sma_long[ticker] * 100
    
    # Latest values
    latest_sma_short = float(round(sma_short[ticker].iloc[-1], 2))
    latest_sma_long = float(round(sma_long[ticker].iloc[-1], 2))
    latest_strength = float(round(strength_series.iloc[-1], 2))
 
    # Trend direction
    if latest_sma_short > latest_sma_long:
        trend = "Uptrend"
    elif latest_sma_short < latest_sma_long:
        trend = "Downtrend"
    else:
        trend = "Sideways"

    # Mean & std over the priod (ignoring NaNs)
    mean_strength = float(round(strength_series.mean(), 2))
    std_strength = float(round(strength_series.std(), 2))

    return{
        "trend_val": latest_strength,
        "trend_mean": mean_strength,
        "trend_std": std_strength,
    }