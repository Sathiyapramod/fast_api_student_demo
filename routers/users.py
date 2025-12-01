from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def get_users():
    return {"message": ""}

@router.get("/{id}")
def get_users_by_id(id: int):
    return {"message": ""}


@router.post("/")
def create_user():
    return {"message": ""}
