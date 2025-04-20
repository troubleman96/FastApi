from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
        tittle:str
        content:str    
        published: bool = True
        rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Wagwaan World"}

@app.get("/posts")
def get_posts():
    return {"data": "post are here."}

@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}