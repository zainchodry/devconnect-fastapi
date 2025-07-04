from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, deps, models

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/", response_model=schemas.ApplicationOut)
def apply(application: schemas.ApplicationCreate, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
    return crud.apply_to_project(db, application, current_user.id)
