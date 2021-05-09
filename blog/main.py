from fastapi import FastAPI
from . import models, database
from database import engine
from .routers import blog, users, authentication

get_db = database.get_db()

app = FastAPI(
)

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(users.router)
app.include_router(authentication.router)