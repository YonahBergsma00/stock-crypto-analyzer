

def z_score(value, mean, std):
    return (value - mean) / std if std > 0 else 0

def combined_score(rsi_val, trend_val, vol_val,
                   rsi_mean, rsi_std, trend_mean, trend_std, vol_mean, vol_std,
                   weights=(0.4, 0.4, 0.2)):
    """
    Combine z-scores of RSI, trend, and volatility into a final score.
    weights = importance of each KPI
    Returns a value that can be interpreted as "buy strength"
    """
    rsi_z = z_score(rsi_val, rsi_mean, rsi_std)
    trend_z = z_score(trend_val, trend_mean, trend_std)
    vol_z = z_score(vol_val, vol_mean, vol_std)

    final = rsi_z * weights[0] + trend_z * weights[1] + vol_z * weights[2]
    return final

def convert_score(score: float) -> str:
    
    if score > 0.5:
        return "Buy"
    elif (score >= -0.5) and (score <= 0.5):
        return "Hold"
    else:
        return "Avoid"