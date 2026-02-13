import pandas as pd

def rsi_signal(prices: pd.Series, ticker: str, UpperBound: float = 70.0, LowerBound: float = 30.0, period: int = 14) -> str:
    
    # Daily price changes
    delta = prices.diff()

    # Gains & losses
    gains = delta.clip(lower = 0)
    losses = -delta.clip(upper=0)

    # Rolling averages
    avg_gain = gains.rolling(window=period).mean()
    avg_loss = losses.rolling(window=period).mean()

    # Avoid division by 0
    rs = avg_gain / avg_loss.replace(0, 1e-10)

    rsi = 100 - (100/ (1 + rs))
    
    if rsi[ticker].iloc[-1] >= UpperBound:
        return "Overbought"
    elif rsi[ticker].iloc[-1] <= LowerBound:
        return "Oversold"
    return "Neutral"


def trend_signal(prices: pd.Series, ticker: str, short_window: int = 20, long_window: int= 50) -> dict:
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

    return {
        "trend": trend, 
        "trend_val": latest_strength
    }


def market_signal(trend_dict: dict, Threshold: float = 2.0) -> str:
    """
    Convert SMA trend into a simple signal.
    """
    trend = trend_dict["trend"]
    strength = trend_dict["trend_val"]

    if trend == "Uptrend" and strength > Threshold:
        return "Bullish"
    elif trend == "Uptrend" and strength <= Threshold:
        return "Neutral/Bullish"
    elif trend == "Downtrend" and strength < -Threshold:
        return "Bearish"
    else:
        return "Neutral"


def crossover_signal(prices:pd.Series, ticker: str, short_window: int = 20, long_window: int = 50) -> str:
    
    sma_short = prices.rolling(window=short_window).mean()
    sma_long = prices.rolling(window=long_window).mean()

    # yesterday vs today
    if sma_short[ticker].iloc[-2] < sma_long[ticker].iloc[-2] and sma_short[ticker].iloc[-1] > sma_long[ticker].iloc[-1]:
        return "Golden Cross"
    elif sma_short[ticker].iloc[-2] > sma_long[ticker].iloc[-2] and sma_short[ticker].iloc[-1] < sma_long[ticker].iloc[-1]:
        return "Death Cross"
    else:
        return "None"