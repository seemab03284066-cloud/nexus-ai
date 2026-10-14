from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import engine, Base
from backend.config import settings

# Create database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NEXUS AI Paper Trading Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "platform": "NEXUS AI",
        "mode": "PAPER_TRADING_ONLY",
        "status": "Operational",
        "starting_virtual_balance": settings.PAPER_STARTING_BALANCE
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected"}
  
