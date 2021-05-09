from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/about')
def about():
    return {"data": {"name": "Fabian Häfliger"}}


@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'blog list of {limit}'}
    else:
        return {'data': f'blog list from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished integers'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1': id}}



@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'blog is created with {blog.title} and {blog.body}'}


