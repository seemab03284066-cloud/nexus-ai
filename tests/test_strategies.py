import pandas as pd
from backend.services.strategy_engine import StrategyEngine

def test_strategy_engine_evaluation():
    engine = StrategyEngine()
    
    # Create mock price data (25 periods)
    data = {
        'close': [100 + i for i in range(25)],
        'high': [102 + i for i in range(25)],
        'low': [98 + i for i in range(25)],
        'volume': [1000 for _ in range(25)]
    }
    df = pd.DataFrame(data)

    result = engine.evaluate_all(df)
    
    assert "score" in result
    assert "signal" in result
    assert result["strategies_evaluated"] == 10
    assert result["signal"] in ["LONG", "SHORT", "NEUTRAL"]
  
