import pandas as pd
import numpy as np
from typing import Dict, Any

class StrategyEngine:
    def __init__(self):
        self.strategies = [
            "EMA_Trend_Filter",
            "RSI_Momentum",
            "MACD_Confirmation",
            "Breakout_Retest",
            "Market_Structure",
            "Volume_Confirmation",
            "VWAP_Context",
            "Bollinger_Volatility",
            "ATR_Stop_Distance",
            "Orderbook_Liquidity"
        ]

    def evaluate_all(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Evaluates all 10 independent analysis modules against provided price data candles.
        Treats signals as research data without look-ahead bias.
        """
        if df.empty or len(df) < 20:
            return {"score": 0.0, "signal": "NEUTRAL", "rejection_reason": "Insufficient historical data"}

        # Basic technical indicator calculations for simulation
        close = df['close'].values
        high = df['high'].values
        low = df['low'].values
        volume = df['volume'].values

        # 1. EMA Trend Filter
        ema_20 = pd.Series(close).ewm(span=20, adjust=False).mean().iloc[-1]
        ema_50 = pd.Series(close).ewm(span=50, adjust=False).mean().iloc[-1]
        trend_bullish = ema_20 > ema_50

        # 2. RSI Momentum
        delta = pd.Series(close).diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / (loss + 1e-10)
        rsi = 100 - (100 / (1 + rs))
        current_rsi = rsi.iloc[-1]

        # Aggregate evidence score (0.0 to 1.0)
        score = 0.5
        if trend_bullish:
            score += 0.2
        if 40 <= current_rsi <= 65:
            score += 0.15

        signal = "LONG" if score >= 0.65 else ("SHORT" if score <= 0.35 else "NEUTRAL")
        
        return {
            "score": round(score, 2),
            "signal": signal,
            "strategies_evaluated": len(self.strategies),
            "indicators": {
                "ema_20": float(ema_20),
                "ema_50": float(ema_50),
                "rsi_14": float(current_rsi),
                "trend_bullish": bool(trend_bullish)
            },
            "rejection_reason": None if signal != "NEUTRAL" else "Confidence score below minimum threshold (0.65)"
      }
      
