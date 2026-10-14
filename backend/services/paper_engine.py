from sqlalchemy.orm import Session
from backend.models import VirtualAccount, Position, TradeHistory
from backend.config import settings

class PaperExecutionEngine:
    def __init__(self, db: Session):
        self.db = db

    def get_or_create_account(self) -> VirtualAccount:
        account = self.db.query(VirtualAccount).first()
        if not account:
            account = VirtualAccount(
                balance=settings.PAPER_STARTING_BALANCE,
                equity=settings.PAPER_STARTING_BALANCE,
                reserved_margin=0.0,
                realized_pnl=0.0,
                unrealized_pnl=0.0,
                total_fees=0.0
            )
            self.db.add(account)
            self.db.commit()
            self.db.refresh(account)
        return account

    def open_position(self, symbol: str, direction: str, entry_price: int, quantity: float, stop_loss: float, take_profit: float, strategy: str) -> dict:
        account = self.get_or_create_account()

        # Check maximum open positions limit (Max 5)
        open_count = self.db.query(Position).filter(Position.status == "OPEN").count()
        if open_count >= 5:
            return {"success": False, "error": "Maximum open positions limit (5) reached."}

        # Calculate conservative margin and fees (0.05% fee)
        notional_value = entry_price * quantity
        fee = notional_value * 0.0005

        if account.balance < (notional_value * 0.2 + fee):  # Assuming 5x simulated margin model or cash buffer
            return {"success": False, "error": "Insufficient virtual capital or margin."}

        # Deduct fee and reserve funds
        account.balance -= fee
        account.total_fees += fee

        position = Position(
            symbol=symbol,
            direction=direction,
            entry_price=entry_price,
            current_price=entry_price,
            quantity=quantity,
            margin=notional_value * 0.2,
            stop_loss=stop_loss,
            take_profit=take_profit,
            unrealized_pnl=0.0,
            status="OPEN",
            strategy_attribution=strategy
        )

        self.db.add(position)
        self.db.commit()
        self.db.refresh(position)

        return {"success": True, "position_id": position.id, "fee_charged": fee}
          
