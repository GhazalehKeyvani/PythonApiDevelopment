from fastapi import FastAPI, Response ,status, HTTPException, Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from .. import models, schema,utils,oauth2
from ..database import get_db

router =APIRouter(
    prefix="/votes",
    tags=['Votes']
)


@router.post("/" , status_code=status.HTTP_201_CREATED)
def vote(vote:schema.Vote, db: Session=Depends(get_db), current_user:int = Depends(oauth2.current_user)):
    post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not post:
        raise HTTPException (status_code = status.HTTP_404_NOT_FOUND, 
                detail=f"post with id {vote.post_id}  does not exist")
    query_vote=db.query(models.Vote).filter(models.Vote.post_id==vote.post_id, models.Vote.user_id==current_user.id)
    found_vote=query_vote.first()
    if (vote.dir==1):
        if found_vote:
            raise HTTPException (status_code = status.HTTP_409_CONFLICT, 
                        detail=f"user {vote.user_id} has already voted for {vote.post_id}")
        new_vote=models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)  #add to db
        db.commit()       #conn.commit
        return {"message":"success vote added"}
    else:
        if not found_vote:
            raise HTTPException (status_code = status.HTTP_404_NOT_FOUND, 
                        detail=f"vote does not exist")
        vote_query.delete(synchronized=False)
        db.commit()
        return {"message":"successfuly delete vote"}


