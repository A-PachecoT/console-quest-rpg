from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    welcome_message = "Welcome to the RPG Game API! This is a Software Development Project for the course CC3S2 from the National University of Engineering."
    return {"message": f"{welcome_message}"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)