from typing import Optional
from fastapi import Body, FastAPI, Response,status,HTTPException
from pydantic import BaseModel
from random import randrange
app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":"title pf post 1","content":"content of post 1","id": 1},{"title":"favorite foods","content":"I like pizza","id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
def root():
    return {"message": "My World"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED )
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

@app.get("/posts/{id}")   
def get_post(id: int,response:Response):
    print(id)
    post= find_post(id)
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"post with {id} not found" )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{"message":f"post with {id} not found"}
    return{"post_detail":post}

    


     

