from fastapi import APIRouter, Response, Request, Depends
from pydantic import BaseModel
from app.services.player_service import PlayerService
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="app/views")

router = APIRouter()


class Login(BaseModel):
    username: str
    password: str


""""
@router.middleware("http")
async def token_middleware(request: Request, call_next):
    token = request.cookies.get("access_token")
    if token:
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
            request.state.user = payload.get("name")
        except jwt.ExpiredSignatureError:
            request.state.user = None
"""


@router.get("/")
async def root(request: Request):
    user = getattr(request.state, "user", None)
    if user:
        welcome_message = f"Welcome {request.state.user} to the RPG Game API! This is a Software Development Project for the course CC3S2 from the National University of Engineering."
        return {
            "message": f"{welcome_message}",
            "options": [
                {
                    "message": "Start a combat",
                    "combat": "/combat",
                },
                {
                    "message": "Check your status",
                    "status": "/status"
                },
                {
                    "logout": "/logout"
                }
                
                
            ],
        }
    else:
        welcome_message = "Welcome to the RPG Game API! This is a Software Development Project for the course CC3S2 from the National University of Engineering."
        return {
            "message": f"{welcome_message}",
            "options": {
                "message": "To start, register if you don't have an account or login if you do.",
                "register": "/register",
                "login": "/login",
            },
        }


@router.get("/login")
async def render_login(request: Request, response: HTMLResponse):
    user = getattr(request.state, "user", None)
    if user:
        return RedirectResponse(url="/")
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def login(
    login: Login,
    response: Response,
    player_service: PlayerService = Depends(PlayerService.get_player_service),
):
    login = login.dict()
    username = login["username"]
    password = login["password"]

    try:
        player = await player_service.login(username, password)
        print(player)
        response = {"message": player["message"]}
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=player["token"], httponly=True)
        return response
    except Exception as e:
        return {"message": f"Login failed: {str(e)}"}


@router.get("/register")
async def render_register(request: Request):
    user = getattr(request.state, "user", None)
    if user:
        return RedirectResponse(url="/")
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
async def register(
    login: Login,
    response: Response,
    player_service: PlayerService = Depends(PlayerService.get_player_service),
):
    login = login.dict()
    username = login["username"]
    password = login["password"]

    try:
        player = await player_service.register(username, password)
        print(player)
        response = {"message": "Registration successful"}
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=player["token"], httponly=True)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": f"Registration failed: {str(e)}"}
        )


@router.get("/logout")
async def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "Logout successful go to home", "home": "/"}


@router.get("/health")
async def health_check():
    return {"status": "healthy"}


@router.get("/game-info")
async def game_info():
    return {
        "name": "RPG Game",
        "version": "0.3.0",
        "description": "A turn-based RPG game with FastAPI backend",
    }

@router.get("/status")
async def status(
    request: Request,
    player_service: PlayerService = Depends(PlayerService.get_player_service),
):
    user = getattr(request.state, "user", None)
    if not user:
        return RedirectResponse(url="/")

    response = await player_service.get_player_by_name(user)
    player = response["player"]

    return {
        "message": "Player status",
        "player": player,
    }