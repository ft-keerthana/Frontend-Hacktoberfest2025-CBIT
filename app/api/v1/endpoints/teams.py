from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/")
def get_teams(q: str = Query(None, title="Search query")):
    teams = [
        {"name": "Alice", "streak": 5},
        {"name": "Bob", "streak": 3},
        {"name": "Charlie", "streak": 7}
    ]
    if q:
        teams = [team for team in teams if q.lower() in team["name"].lower()]
    return {"teams": teams}

