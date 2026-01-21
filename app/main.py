from fastapi import FastAPI
from app.core.database import init_db
from app.api.v1.api import api_router

app=FastAPI(title="Todo app")

@app.on_event("startup")
async def startup():
    init_db()
    
app.include_router(api_router, prefix="/api/v1")