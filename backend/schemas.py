from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AccountOverview(BaseModel):
    balance: float
    equity: float
    reserved_margin: float
    realized_pnl: float
    unrealized_pnl: float
    total_fees: float
    win_rate: float
    drawdown: float
    open_positions_count: int

    class Config:
        from_attributes = True

class PositionResponse(BaseModel):
    id: int
    symbol: str
    direction: str
    entry_price: float
    current_price: float
    quantity: float
    margin: float
    stop_loss: float
    take_profit: float
    unrealized_pnl: float
    status: str
    strategy_attribution: str
    opened_at: datetime

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    symbol: str
    direction: str
    quantity: float
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None
    strategy_attribution: str = "Manual/Signal"
  
