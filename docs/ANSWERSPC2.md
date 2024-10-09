# Answers for Mr. Lara - PC2

Nuevamente volvemos al español.

#### Repositorio GitHub actualizado

Para esta PC, hemos decidido trabajar, con Git Flow, para el manejo de las ramas, creando nuestra rama [develop](https://github.com/A-PachecoT/console-quest-rpg/tree/develop).

#### Documentación de Sprints (planes, burndown charts, revisiones)

Nuestro GitHub Project.

![](https://imgur.com/kbU83LZ.png)

La agendación de citas

![](https://imgur.com/5aa8got.png)

Calculando nuestros story points

![](https://i.imgur.com/Vyw1CqM.jpeg)


#### Pruebas automatizadas 

![](https://i.imgur.com/eTVm2q1.png)


#### Prueba unitarias

En la computadora de Mr. Sergio Pezo
![](https://imgur.com/aAmDd15.png)


En la computadora de Mr. André Pacheco
![](https://i.imgur.com/xgn6380.png)


#### Configuración de CI/CD y DevSecOps

Se usó la librería `safety-check` para el análisis de seguridad de nuestros módulos externos.

Por lo que se agregó un Job nuevo en nuestro workflow de GitHub Actions `.github/workflows/ci.yml`

``` yml
  security-check:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Run safety check
        run: |
          pip install safety
          safety check

```


#### Dashboards de Prometheus y Grafana

Se desarrolló un nuevo Dashboard para la visualización del estado de respuestas de nuestro servidor.

![](https://imgur.com/ZjcMN7y.png)

Este dashboard se puede importar con el archivo `grafana/dashboards/server-stats-dashboard.json`.

Así también como se crearon tres alertas las cuales envían un correo a `sergiopezoj@gmail.com`. Estas pueden ser importadas en `grafana/alerts`.

- `grafana/alerts/alert-2.5-sec.json`: Alerta configurada cuando la latencia de una petición es mayor a 2.5 segundos.

``` Prometheus
sum(http_all_request_duration_seconds_count) by (handler) - sum(http_all_request_duration_seconds_bucket{le="2.5"}) by (handler)
```

- `grafana/alerts/alert-505.json`: Alerta configurada cuando el servidor retorna un código 500.

``` Prometheus
sum(http_all_requests_total{status="5xx"}) by (handler)
```

- `/home/sergio/Documents/sixth/sd/console-quest-rpg/grafana/alerts/alert-login-register.json`: Alerta configurada cuando un usuario hace login o se registra.
``` Prometheus
increase(http_all_requests_total{handler=~"/(login|register)", method="POST", status="2xx"}[5m])

```
 
#### Documentación de uso avanzado de Git

Realmente usamos demasiados `git reset -- mixed HEAD~1`, `git bisect` para el ticket RPG-11 que al final nunca se pusheó a `main`. 

Al inicio al tratar de usar TBD, Óscar no dejaba de usar `git rebase` a lo loco.

Pero por lo general `git merge -ff` fue lo que más usamos.

Para unir la rama `feature/RPG-

![](https://imgur.com/DwGlBV8.png)

Compañero André Pacheco resolviendo 14 merge conflict de Git ocasionado por realizar un rebase; con git mergetool

![Merge Conflict](https://i.imgur.com/NqiQLcp.jpeg)

Se usó el git rebase interactivo para limpiar el historial de commits y mantener un historial limpio y organizado.

![Git Rebase](https://i.imgur.com/PZfiLRG.png)

#### Reflexión final

Realmente desarrollar console-quest fue un reto desafiente a nivel técnico y de colaboración. Aprender a usar práticas y herramientas para el desarrollo de software profesional. 

Para la realización de sprint 2, se decidió usar Git Flow como flujo de trabajo, trabajando con la rama develop, sim embargo, como duro simplemente dos días, al final nos arrenpentimos, pero fue una buena experiencia de aprendizaje para proyectos futuros.

Esta fue mi primera experiencia con herramientas de monitoreo como Prometheus y Grafana fue grata experiencia, y amplia mi visión de como crear mejores soluciones de software.+

En conclusión, se aprendió bastante y se sufrió bastante, valga la redundancia. Podemos decir que una comunicación efectiva y eficaz es lo clave para el correcto desenvolvimiento de un proyecto, pues esto permite que el entorno de desarrollo con la ayuda de las metodologías ágilas fluya de manera correcta y productiva.