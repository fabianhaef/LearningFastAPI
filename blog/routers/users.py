from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from . import schemas, models, database
from sqlalchemy import Session
from ..hashing import Hash


router = APIRouter(
    prefix='/user',
    tags=['user']
)

get_db = database.get_db()


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with the id {id} is not available')

    return user