
from fastapi import FastAPI
#from passlib.context import CryptContext
#from random import randrange
#from sqlalchemy.orm import Session
from . import models
from .database import engine
from .routers import posts, users, auth, votes
from fastapi.middleware.cors import CORSMiddleware


#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#models.Base.metadata.create_all(bind=engine)      #we dont have need to this when we use Alembic

app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],       #allow get post request and ..... requests
    allow_headers=["*"],
)







# def find_post(id): 
#     for p in my_posts: 
#         if p["id"] == id :
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
#     return None

app.include_router(posts.router) 
app.include_router(users.router) 
app.include_router(auth.router) 
app.include_router(votes.router) 

@app.get("/")
def root():
    return {"message": "Hello World"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session=Depends(get_db) ):  #it make dependency''' 
#     posts = db.query(models.Post).all()   #.all run method as query in db and return it
#     print(posts)
#     return {"status":posts}



