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
├── app/
│ ├── main.py
│ ├── api/
│ ├── models/
│ │ ├── init.py
│ │ ├── character.py
│ │ ├── monster.py
│ │ └── item.py
│ └── services/
├── tests/
│ └── test_main.py
├── requirements.txt
└── README.md
```

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

## Próximos Pasos
- Implementar servicios básicos para Character, Monster e Item
- Desarrollar la lógica de combate
- Crear una interfaz de consola para interactuar con el juego
- Implementar la lógica de inventario
- Implementar la lógica de equipamiento
- Implementar la lógica de consumibles
- Implementar la lógica de experiencia y niveles
- Implementar la lógica de críticos
- Implementar la lógica de derrotas y victorias
- Implementar la lógica de guardado y carga de partida
- Implementar la lógica de personajes
- Implementar la lógica de monstruos