# API Documentation

## Base URL

All API endpoints are relative to: `http://localhost:8000`

## Endpoints

### General Routes

- `GET /`: Home page
  - Response: Welcome message and available options based on user authentication status

- `GET /login`: Render login page
  - Response: HTML login page

- `POST /login`: User login
  - Request Body: `{"username": "string", "password": "string"}`
  - Response: Login status message and sets access token cookie

- `GET /register`: Render registration page
  - Response: HTML registration page

- `POST /register`: User registration
  - Request Body: `{"username": "string", "password": "string"}`
  - Response: Registration status message and sets access token cookie

- `GET /logout`: User logout
  - Response: Logout confirmation message and removes access token cookie

- `GET /health`: API health check
  - Response: `{"status": "healthy"}`

- `GET /game-info`: Game information
  - Response: `{"name": "RPG Game", "version": "0.3.0", "description": "A turn-based RPG game with FastAPI backend"}`

### Player Routes

- `GET /player/`: Player home
  - Response: Welcome message and available actions

- `GET /player/all`: Get all players
  - Response: List of all players

### Combat Routes

- `GET /combat/`: Combat home
  - Response: Welcome message and available combat actions

- `GET /combat/start`: Start a combat
  - Response: Combat start confirmation message

- `GET /combat/attack`: Perform an attack
  - Response: Attack confirmation message

- `GET /combat/defend`: Perform a defense
  - Response: Defense confirmation message

- `GET /combat/ability`: View available abilities
  - Response: List of player's abilities and usage instructions

- `GET /combat/ability/{ability_id}`: Use a specific ability
  - Response: Ability usage confirmation message

## Authentication

Most endpoints require authentication. After successful login or registration, an access token is set as an HTTP-only cookie. This token is used for subsequent authenticated requests.

## Error Handling

The API uses standard HTTP status codes for error responses. Common error codes include:

- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 500: Internal Server Error

Detailed error messages are provided in the response body.

---
For detailed request/response schemas, please refer to the Swagger UI (from FastAPI) documentation at `http://localhost:8000/docs` or `http://localhost:8000/redoc` when the API is running.
