# Console Quest RPG

## Descripción
Console Quest RPG es un juego de rol por turnos desarrollado como proyecto de software para el curso CC3S2 de la Universidad Nacional de Ingeniería. El juego utiliza FastAPI para el backend y está diseñado para ser jugado a través de una interfaz de consola.

### Integrantes
- Pacheco André - 20222189G
- Pezo Sergio - 
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
- Python 3.9+
- FastAPI
- Uvicorn
- Pydantic
- Pytest

### Configuración del Entorno
1. Clonar el repositorio:
   ```
   git clone https://github.com/A-PachecoT/console-quest-rpg.git
   cd console-quest-rpg
   ```

2. Crear y activar un entorno virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```

### Estructura del Proyecto
```
console-quest-rpg/
├── .github/
│   └── workflows/
│       └── ci.yml
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── character.py
│   │   │   ├── monster.py
│   │   │   └── item.py
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── character_service.py
│   │       └── dungeon_service.py
│   ├── tests/
│   │   ├── test_main.py
│   │   ├── test_models.py
│   │   ├── test_character_service.py
│   │   └── test_dungeon_service.py
│   └── requirements.txt
├── frontend/  # Futura implementación
└── README.md
```

## Frontend (Próximamente)

Se planea implementar un frontend para mejorar la experiencia de usuario del juego.

### Ejecutar la Aplicación
Para ejecutar la aplicación en modo de desarrollo:

```
uvicorn app.main:app --reload
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

## Próximos Pasos
- Implementar la lógica de combate
- Crear una interfaz de consola para interactuar con el juego
- Implementar la lógica de inventario y equipamiento
- Añadir más tipos de monstruos y objetos
- Implementar un sistema de guardado y carga de partidas
