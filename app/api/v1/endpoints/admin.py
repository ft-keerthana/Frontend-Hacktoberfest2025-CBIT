from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_admin_dashboard():
    return {
        "project_progress": 29,
        "stats": {
            "total_tasks": 7,
            "tasks_in_progress": 2,
            "completed_tasks": 2,
        },
        "team_activity": [
            {"name": "Alice", "last_active": "13 hours ago", "tasks_assigned": 2, "tasks_completed": 1, "streak": 5},
            # Add other team members...
        ]
    }
