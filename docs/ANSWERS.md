## Answers for Mr. Lara.

En este archivo Markdown, nos moveremos al español.

### Gestión de combates mediante la API REST
Para la gestion de los combates se usa el endpoint `/combat` del cual se desprenden 4 endpoints:
- `/start` Que es usado para poder iniciar un combate, esta ruta asigna un enemigo al jugador, si el jugador ya tiene un enemigo asignado, el enemigo no es reasignado
- `/attack` Que es usado para atacar al enemigo actual, si el jugador no tiene un enemigo actual, retorna que no se encuentra en combate
- `/defend` Que es usado para defenserse (mitigar 30% del daño sin defenderse) del enemigo actual, si el jugador no tiene un enemigo actual, retorna que no se encuentra en combate
- `/ability` Esta ruta redirecciona al menu de habilidades del jugador en el que el jugador decide que habilidad usar 

### Sistema de subida de nivel automático

Cada que el jugador derrota un enemigo, consigue experiencia que se va acumulando hasta que llega al limite de la experiencia objetivo
Al ocurrir esto, el jugador sube de nivel, con lo cual consigue los siguientes efectos:
- Mejora la vida máxima
- Mejora el mana máximo
- Recupera toda la vida
- Recupera todo el mana gastado
- Mejora su ataque
- Mejora su defensa

Todo esto sucede de forma automatica.

### Dockerización del juego RPG


Para la dockerización de nuestro juego RPG, se crearon dos archivos principales: `Dockerfile` y `compose.yml`.

El `Dockerfile` se encarga de definir la imagen de nuestro backend:

```Dockerfile:Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV MONGO_URL=mongodb://mongodb:27017
ENV MONGO_DB_NAME=testdb

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

Este Dockerfile utiliza una imagen base de Python 3.12, instala las dependencias necesarias y configura el entorno para ejecutar nuestra aplicación FastAPI.

Por otro lado, el archivo `compose.yml` orquesta todos los servicios necesarios para nuestro juego:

```yaml:compose.yml
services:
  backend:
    build: .
    ports:
      - "8000:8000" 
    depends_on:
      - mongodb 
    environment:
      MONGO_URL: mongodb://root:password@mongodb:27017/db_test?authSource=admin
      MONGO_DB_NAME: db_test

  mongodb:
    image: mongo:5.0
    ports:
      - "27017:27017" 
    volumes:
      - mongo-data:/data/db
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: password
      MONGO_INITDB_DATABASE: db_test

  prometheus:
    image: prom/prometheus:v2.55.0-rc.0
    ports:
      - 9090:9090
    volumes:
      - ./prometheus_data/prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'

  grafana:
    image: grafana/grafana:11.0.6
    ports:
      - 3000:3000
    volumes:
      - grafana_data:/var/lib/grafana

volumes:
  prometheus_data:
    driver: local
    driver_opts:
      o: bind
      type: none
      device: ./prometheus_data
  grafana_data:
    driver: local
    driver_opts:
      o: bind
      type: none
      device: ./grafana_data
  mongo-data:
```

Este archivo `compose.yml` define cuatro servicios principales:

1. `backend`: Nuestro servicio FastAPI.
2. `mongodb`: Base de datos para almacenar la información del juego.
3. `prometheus`: Servicio para recolectar métricas.
4. `grafana`: Herramienta para visualizar las métricas recolectadas.

Además, se configuran volúmenes para persistir los datos de MongoDB, Prometheus y Grafana, no olvidar para crear la carpeta `grafana_data`.

```
mkdir -p grafana_data
```

Con esta configuración, logramos dockerizar exitosamente nuestro juego RPG, incluyendo todos los servicios necesarios para su funcionamiento y monitoreo. Esto nos permite desplegar fácilmente toda la infraestructura necesaria con un simple comando:

```
docker compose up --build -d
```

Se logró implementar correctamente la dockerización de nuestro juego RPG, lo que facilita enormemente su despliegue y escalabilidad. El siguiente paso sería mejorar las prácticas de seguridad, como por ejemplo, no exponer las credenciales de la base de datos directamente en el archivo `compose.yml`, sino utilizar variables de entorno o secretos de Docker para manejar información sensible de manera más segura.



### Monitorización de estadísticas de combates

Para la monitorización se trabajo con la librería de python `prometheus_fastapi_instrumentator` la cual nos brinda métricas prederterminadas de todo nuestro server. En específico, se tomó una que cuenta todas las peticiones individualmente en `app/main.py`.

``` Python
instrumentator.add(
    metrics.requests(
        metric_name="http_all_requests",
    )
)
```

Además nos permite añadir métricas personalizadas, con `prometheus_client`.

Para este proyecto se personalizó 3 métricas en `app/metrics.py` para instrumentar:

- `PLAYER_DAMAGE`: Daño del jugador.
- `PLAYER_DAMAGE`: Nivel del jugador.
- `COMBAT_OUTCOMES`: Resultados de combate.

Entonces, finalmente tenemos nuestras 4 métricas de interest.

Primero, consultamos en `localhost:9090` para ver si nuestro servicio de Prometheus no tuvo ningun problema



Ahora toca, ir a Grafana en `localhost:3000` para visualizar nuestras métricas. Una vez dentro, tenemos que añadir un DataSource nuevo para usar Prometheus.

![](https://i.imgur.com/N8sGUuP.png)

Una vez dentro conectarse a Prometheus con `http://prometheus:9090`, y cambiamos el método a `GET`, finalmente damos a Save.

![](https://imgur.com/IfQa9fV.png)

Ahora si creamos un dashboard

![](https://imgur.com/yRqXXc9.png)
![](https://imgur.com/I2HX9QT.png)

E importamos nuestro archivo `grafana/main-dashboard.json`

Guardamos y tendríamos que tener una vista vacía si es que no jugamos todavía, si no, nuestro dashboard tendría este aspecto:

![](https://imgur.com/QDzztLf.png)

Con las siguientes visualizaciones:

- `Visitas Home`: Un contador que muestra el número total de visitas a la página principal del juego. Esto ayuda a entender el tráfico general del sitio.

- `Combat Preferences`: Un gráfico circular que ilustra las preferencias de los jugadores en cuanto a las acciones de combate (ataque, defensa, uso de habilidades). Esto proporciona información sobre las estrategias más populares entre los jugadores.

- `Nivel de Jugadores`: Un gráfico de barras que muestra la distribución de niveles entre los jugadores. Esto permite visualizar rápidamente la progresión general de los jugadores en el juego.

- `Daño inflingido por jugador`: Un gráfico de líneas que muestra el daño total infligido por cada jugador a lo largo del tiempo. Esto ayuda a identificar a los jugadores más efectivos en combate y a observar tendencias en el rendimiento de los jugadores.

- `Victorias por jugador`: Un gráfico de barras que muestra el número de victorias de cada jugador. Esto permite identificar a los jugadores más exitosos en los combates.

- `Derrotas por jugador`: Similar al gráfico de victorias, pero mostrando el número de derrotas de cada jugador. Esto ayuda a identificar a los jugadores que pueden necesitar ayuda o mejoras en sus estrategias de juego.

Por lo que se logró implementar correctamente métricas para visualizar el rendimiento de los combates de nuestros jugadores.


### Resolución de conflictos en Git usando Git Mergetool

La resolución de conflictos casi se vuelve un cuello de botella, pero gracias a los métodos para resolver estos mismos, tales como el entorno de github, como la MergeTool de Visual Studio Code. 

Estos problemas se solucionaron rápidamente, sin embargo, aún existen limitacioes, tales como en la [Feature/RPG-11](https://github.com/A-PachecoT/console-quest-rpg/pull/26), donde se usó la herramienta de GitHub:

![](https://imgur.com/IfJIQc1.png)

No obstante, aún existen fallos en la lógica, por tal motivo no se da cierre a la pull request.

### Reflexión Final

Para nuestro proyecto se trató al inicio de implementar un flujo de trabajo de Trunk Based Development, sin embargo, la familiaridad con esta herramienta, no se nos facilitó, por lo que obtamos, seguir un enfoque de Ship, Show y Ask. La cual en principio, funciona de esta manera:

- **Ship**: Pushear de frente a main.
- **Show**: Hacer pull request, y si todo sale bien con los checks, proceder con el merge.
- **Ask**: Hacer un pull request, y esperar comentarios.

Esta estrategia, se ve claramente durante todo el flujo de nuestro proyecto, pues hay commits y ramas que se mergearon o hicieron rebase a main sin previo pull request, así como hay pull requests, donde realizamos el diálogo. 

Sin embargo, esto no hubiese sido posible, sin la integración de nuestro [GitHub Projects](https://github.com/users/A-PachecoT/projects/2/views/1) con un enfoque al framework Scrum, pues esto nos permitió conocer como ibamos avanzando cada uno, de tal manera no cruzarnos entre tareas.

Así que, en resumen, aplicar las metodologías ágiles y predefinir un flujo de ramas, permitió a este proyecto culminar con éxito. De todas maneras, a seguir mejorando, pues esto recien empieza.