import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database import Base
from backend.models import VirtualAccount, Position
from backend.services.paper_engine import PaperExecutionEngine

@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_paper_account_creation(db_session):
    engine = PaperExecutionEngine(db_session)
    account = engine.get_or_create_account()
    
    assert account.balance == 100.0
    assert account.equity == 100.0

def test_open_position(db_session):
    engine = PaperExecutionEngine(db_session)
    result = engine.open_position(
        symbol="BTC-USDT",
        direction="LONG",
        entry_price=60000.0,
        quantity=0.001,
        stop_loss=59000.0,
        take_profit=62000.0,
        strategy="EMA_Trend_Filter"
    )

    assert result["success"] is True
    assert "position_id" in result
    
    position = db_session.query(Position).first()
    assert position.symbol == "BTC-USDT"
    assert position.direction == "LONG"
  
