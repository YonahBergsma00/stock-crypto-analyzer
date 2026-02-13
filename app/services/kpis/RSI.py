import pandas as pd

def calculate_rsi(prices: pd.Series, ticker: str, period: int = 14) -> dict:
    """
    Calculate the Relative Strength Index (RSI)
    Returns the latest RSI value
    """

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
    rsi_centered = rsi +- 50

    rsi_val = float(round(rsi_centered[ticker].iloc[-1], 2))
    rsi_mean = float(round(rsi_centered[ticker].mean(), 2))
    rsi_std = float(round(rsi_centered[ticker].std(), 2))

    return {
        "rsi_val": rsi_val,
        "rsi_mean": rsi_mean,
        "rsi_std": rsi_std,
    }

