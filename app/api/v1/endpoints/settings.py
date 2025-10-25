from fastapi import APIRouter

router = APIRouter()

@router.get("/settings")
def get_settings():
    return {"theme": "light", "notifications": True}

@router.post("/settings")
def update_settings(settings: dict):
    return {"updated": True, "settings": settings}
