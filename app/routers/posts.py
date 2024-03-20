from fastapi import FastAPI, Response ,status, HTTPException, Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List,Optional
from .. import models, schema,utils,oauth2
from ..schema import PostCreate, Post, UserOut, PostOut
from ..database import get_db
#mport pdb; pdb.set_trace()

router =APIRouter(
    prefix="/posts",
    tags=['Posts']
)

#@router.get("/", response_model=List[schema.Post])  
@router.get("/",response_model=PostOut)  
def get_posts(db: Session=Depends(get_db), current_user:int = Depends(oauth2.current_user),limit:int = 10, skip:int =0, search:Optional[str] = None):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()

   # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()   #.all run method as query in db and return it
    posts = db.query(models.Post, func.count(models.Post.id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()   #.all run method as query in db and return it
    
    return posts   

@router.post("/" , status_code=status.HTTP_201_CREATED,response_model=schema.Post)
def create_posts(post:schema.PostCreate, db: Session=Depends(get_db),
 current_user:int = Depends(oauth2.current_user)):                             
    # cursor.execute("""INSERT INTO posts (title, content, published ) VALUES
    #  (%s , %s , %s ) RETURNING *""",(post.title ,post.content, post.published))
    # new_post= cursor.fetchone()

    # conn.commit()         ##for save changes to db 
    # print(post)
    # print(post.dict())
    # post_dict = post.dict()
    # post_dict['id'] = randrange(0,10000000)
    # my_posts.append(post_dict)


    # new_post =models.Post(
    #     # title=post.title,
    #     #  content=post.content,
    #     #  published=post.published   

    #      )


    new_post = models.Post(**post.dict())    # do automatically 3 code above)
    db.add(new_post)  #add to db
    db.commit()       #conn.commit
    db.refresh(new_post)     #RETURN * on sql
    return new_post
    #return {"post":f"title: {payload['title']} content: {payload['content']} "}
    #return {"data": new_post}    ?


@router.get("/{id}", response_model=schema.PostOut)
def get_post(id:int, db: Session=Depends(get_db),current_user:int = Depends(oauth2.current_user)):    #validation with fastapi
    # cursor.execute("""SELECT * FROM posts WHERE id=%s""",str((id)))
    # post=cursor.fetchone()
    # #print(post)
    # #post= find_post(id)
    # #print(post)
    #post=db.query(models.Post).filter(models.Post.id==id).first()
    post = db.query(models.Post, func.count(models.Post.id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()  

    if not post:
        raise HTTPException (status_code = status.HTTP_404_NOT_FOUND , 
                        detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'massage: f"post with id {id} was not found'}
    return post


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session=Depends(get_db),current_user:int = Depends(oauth2.current_user)):
    # cursor.execute("""DELETE  FROM posts WHERE id=%s RETURNING *""",str((id),))
    # post_delete=cursor.fetchone()
    # conn.commit()    
    # #index = find_index_post(id)
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} does not exist")
    # if post.owner_id != oauth2.current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                     detail=f"not authorized to perform requested action")
    post_query.delete(synchronize_session=False)

    db.commit()
    #my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)




@router.put("/{id}", response_model=schema.Post)
def update_post(id:int, update_post:PostCreate, db: Session=Depends(get_db)
,current_user:int = Depends(oauth2.current_user)):

    # cursor.execute("""UPDATE posts SET title = %s , content= %s ,
    # published=%s WHERE id = %s RETURNING *""",
    # (post.title ,post.content, post.published, str(id)))
    # updated_post=cursor.fetchone()
    # conn.commit()
    # #print(updated_post)
    # #index=find_index_post(id)

    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} does not exist")
    # if post.owner_id != oauth2.current_user.id:
    #         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail=f"not authorized to perform requested action")
    
    # post_dict=post.dict()
    # post_dict['id']=id
    # my_posts[index]=post_dict


    post_query.update(update_post.dict(), synchronize_session=False)

    db.commit()
    #print(post) 

    # return {'data':post_dict}
    return post_query.first()



# @app.get("/posts/latest")    #it's not validate in fastapi
# def get_latast_post(id: int, response: Response):
#     post = my_posts[len(my_posts)-1]
#     return {"detail": post}