from fastapi import FastAPI
from .database import engine, Base
from .routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI CRUD Example")

app.include_router(users.router)
