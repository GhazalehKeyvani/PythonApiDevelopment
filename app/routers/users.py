from fastapi import FastAPI, Response ,status, HTTPException, Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from .. import models, schema,utils
from ..database import get_db

router =APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/" , status_code=status.HTTP_201_CREATED, response_model=schema.UserOut)
def create_users(user:schema.UserCreate, db: Session=Depends(get_db)):
    #hash the password
    #hash_password = pwd_context.hash(**user.dict())
    
    print(user.password)
    hash_password = utils.hash_password(user.password)
    user.password = hash_password
    
    new_user = models.User(**user.dict())    # do automatically 3 code above)
    db.add(new_user)  #add to db
    db.commit()       #conn.commit
    db.refresh(new_user)     #RETURN * on sql
    return new_user


@router.get("/{id}", response_model=schema.UserOut)
def get_user(id:int, db: Session=Depends(get_db)):    #validation with fastapi

    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException (status_code = status.HTTP_404_NOT_FOUND , 
                        detail=f"post with id: {id} was not found")

    return user