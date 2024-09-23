# Console Quest RPG

## Descripción
Console Quest RPG es un juego de rol por turnos desarrollado como proyecto de software para el curso CC3S2 de la Universidad Nacional de Ingeniería. El juego utiliza FastAPI para el backend y está diseñado para ser jugado a través de una interfaz de consola.

### Integrantes
- Pacheco André - 20222189G
- Pezo Sergio - 20224087G
- Torres Oscar - 

## Versiones

### v0.1.0 - Configuración inicial y estructura básica
- Configuración del entorno de desarrollo
- Implementación de la estructura básica del proyecto
- Configuración de FastAPI con endpoints de prueba
- Implementación de CI básico con GitHub Actions

### v0.2.0 - Modelos de datos básicos
- Implementación de modelos de datos para Character, Monster e Item
- Utilización de Pydantic para la validación de datos
- Configuración de ejemplos para documentación automática (SwaggerUI). Para acceder a la documentación, usar `/redoc`.
- Se empezó a usar versionamiento semántico para las versiones del proyecto. Para ello se usó el comando:
```
git tag -a v0.2.0 -m "v0.2.0 - Basic data models"
```

### v0.3.0 - Servicios básicos e implementación de API
- Implementación de servicios para Character y Dungeon
- Creación de endpoints para la gestión de personajes y mazmorras
- Actualización de la API para incluir nuevos servicios y endpoints
- Ampliación de las pruebas unitarias para cubrir nuevos servicios y endpoints

## Guía de Desarrollo

### Requisitos

All you will need to run this project is [Docker](https://docs.docker.com).

### Commands
1. Clonar el repositorio:

```
git clone https://github.com/A-PachecoT/console-quest-rpg.git

cd console-quest-rpg
```

2. Para ejecutar la aplicación, primero necesitaremos ejecutar nuestro `compose.yml`, pues necesitaremos de la imagen de [MongoDB](https://www.mongodb.com).

```
docker compose up --build -d
```

Una vez generado todos los contenedores, podemos ejecutar nuestro RPG con:

```
docker compose run -it frontend python main.py
```

Y listo, disfruta la experiencia.



### Estructura del Proyecto
```
console-quest-rpg/
├── .github/
│   └── workflows/
│       └── ci.yml
├── backend
│   ├── app
│   │   ├── config.py
│   │   ├── database
│   │   │   ├── __init__.py
│   │   │   └── mongo
│   │   │       ├── connection.py
│   │   │       ├── _init_.py
│   │   │       └── queries
│   │   │           ├── __init__.py
│   │   │           └── player.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── character.py
│   │   │   ├── __init__.py
│   │   │   ├── item.py
│   │   │   ├── monster.py
│   │   │   └── player.py
│   │   ├── routes
│   │   │   ├── endpoints
│   │   │   │   ├── character_routes.py
│   │   │   │   ├── dungeon_routes.py
│   │   │   │   ├── general_routes.py
│   │   │   │   └── player_routes.py
│   │   │   └── __init__.py
│   │   └── services
│   │       ├── character_service.py
│   │       ├── dungeon_service.py
│   │       ├── __init__.py
│   │       └── player_service.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── tests
│       ├── conftest.py
│       ├── test_character_service.py
│       ├── test_dungeon_service.py
│       ├── test_main.py
│       └── test_models.py
├── compose.yml
├── frontend
│   ├── app
│   │   ├── app.py
│   │   ├── controllers
│   │   │   └── __init__.py
│   │   ├── data.py
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── AbstractCharacter.py
│   │   │   ├── Enemy.py
│   │   │   ├── __init__.py
│   │   │   └── Player.py
│   │   └── views
│   │       ├── AbstractView.py
│   │       ├── CombatView.py
│   │       ├── EnterDungeonView.py
│   │       ├── __init__.py
│   │       ├── MainMenuView.py
│   │       └── NewPlayerView.py
│   ├── Dockerfile
│   └── main.py
└── README.md
```


### Pruebas
Para ejecutar las pruebas:

```
pytest
```
## API Endpoints

- `GET /`: Mensaje de bienvenida
- `GET /health`: Verificación de salud de la API
- `GET /game-info`: Información del juego
- `POST /characters`: Crear un nuevo personaje
- `GET /characters/{character_id}`: Obtener información de un personaje
- `PUT /characters/{character_id}`: Actualizar un personaje
- `DELETE /characters/{character_id}`: Eliminar un personaje
- `POST /characters/{character_id}/level-up`: Subir de nivel a un personaje
- `POST /dungeon/generate`: Generar una nueva mazmorra
- `POST /dungeon/move/{direction}`: Mover al jugador en la mazmorra
- `POST /players`: Crear un nuevo jugador
- `GET /players/{player_id}`: Obtener información de un jugador
- `GET /players`: Obtener todos los jugadores
- `PUT /players/{player_id}`: Actualizar un jugador
- `DELETE /players/{player_id}`: Eliminar un jugador

## Base de Datos

El proyecto utiliza MongoDB como base de datos. La conexión a MongoDB se realiza utilizando Motor, un controlador asíncrono para MongoDB.