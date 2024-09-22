from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    welcome_message = "Welcome to the RPG Game API! This is a Software Development Project for the course CC3S2 from the National University of Engineering."
    return {"message": f"{welcome_message}"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/game-info")
async def game_info():
    return {
        "name": "RPG Game",
        "version": "0.1.0",
        "description": "A turn-based RPG game with FastAPI backend"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)