from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    welcome_message = "Welcome to the RPG Game API! This is a Software Development Project for the course CC3S2 from the National University of Engineering."
    return {"message": f"{welcome_message}"}

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.get("/game-info")
async def game_info():
    return {
        "name": "RPG Game",
        "version": "0.3.0",
        "description": "A turn-based RPG game with FastAPI backend"
    }