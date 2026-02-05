

def rsi_signal(rsi:float) -> str:
    if rsi >= 70:
        return "Overbought"
    elif rsi <= 30:
        return "Oversold"
    return "Neutral"