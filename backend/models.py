from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from backend.database import Base

class VirtualAccount(Base):
    __tablename__ = "virtual_accounts"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Float, default=100.0)
    equity = Column(Float, default=100.0)
    reserved_margin = Column(Float, default=0.0)
    realized_pnl = Column(Float, default=0.0)
    unrealized_pnl = Column(Float, default=0.0)
    total_fees = Column(Float, default=0.0)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    direction = Column(String)  # LONG or SHORT
    entry_price = Column(Float)
    current_price = Column(Float)
    quantity = Column(Float)
    margin = Column(Float)
    stop_loss = Column(Float)
    take_profit = Column(Float)
    unrealized_pnl = Column(Float, default=0.0)
    status = Column(String, default="OPEN")  # OPEN, CLOSED
    strategy_attribution = Column(String)
    opened_at = Column(DateTime, default=datetime.utcnow)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    direction = Column(String)  # BUY or SELL
    order_type = Column(String, default="MARKET")
    price = Column(Float)
    quantity = Column(Float)
    status = Column(String, default="FILLED")  # PENDING, FILLED, CANCELLED
    created_at = Column(DateTime, default=datetime.utcnow)

class TradeHistory(Base):
    __tablename__ = "trade_history"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    direction = Column(String)
    entry_price = Column(Float)
    exit_price = Column(Float)
    quantity = Column(Float)
    net_pnl = Column(Float)
    fee = Column(Float)
    holding_time_seconds = Column(Integer)
    strategy_attribution = Column(String)
    closed_at = Column(DateTime, default=datetime.utcnow)
  
