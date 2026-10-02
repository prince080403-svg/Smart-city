from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.dashboard import router as dashboard_router
from app.routers.traffic import router as traffic_router
from app.routers.aqi import router as aqi_router
from app.routers.flood import router as flood_router
from app.routers.emergency import router as emergency_router

from app.database.database import engine, Base

from app.models.user import User
from app.models.traffic import Traffic
from app.models.aqi import AQI
from app.models.flood import Flood
from app.models.emergency import Emergency


app = FastAPI(
    title="AI Digital Twin for Smart Cities",
    version="1.0.0"
)


# CORS - React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create database tables
Base.metadata.create_all(bind=engine)


# Routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(dashboard_router)
app.include_router(traffic_router)
app.include_router(aqi_router)
app.include_router(flood_router)
app.include_router(emergency_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Digital Twin API 🚀"
    }