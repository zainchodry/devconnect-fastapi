from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, deps, models

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=schemas.ProjectOut)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
    return crud.create_project(db, project, current_user.id)


