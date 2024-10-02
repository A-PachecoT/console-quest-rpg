# Developer Guide

## Local Development Setup

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Git](https://git-scm.com/downloads)

### Setting Up the Project

1. Clone the repository:
```
git clone https://github.com/A-PachecoT/console-quest-rpg.git
cd console-quest-rpg
```

2. Build and start the Docker container:
```
docker compose up --build -d
```

### Using Black Formatter

We use Black Formatter to maintain consistent code formatting. To set it up:

1. Install Black Formatter: Install it from the VSC extension marketplace.
2. Now when you save the file, it will be automatically formatted. Ensure the parameter for length is set to 88, with the following configuration in VSC (File > Preferences > Settings > Select "Preferences: Open Settings (JSON)"):

```json
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length", "88"]
}
```

3. Install pre-commit:
```
pip install pre-commit
```

4. Run the following command to install the pre-commit hook in the local repository:
```
pre-commit install
```

1. Now when you commit the changes, the pre-commit hook will run and format the code. If you want to run it manually, you can use the following command:
```
pre-commit run --all-files
```

### Useful Docker Commands
- Start all services:
```
docker compose up -d
```

- View real-time logs of the backend:
```
docker compose logs -f backend
```

- Stop all services:
```
docker compose down
```
- Rebuild and restart a specific service (e.g., backend) **after code changes**:
```
docker compose up -d --build
```

- After a code change, a single command to rebuild and restart the backend and follow the logs:
```
docker compose up -d --build backend && docker compose logs -f backend
```

## Monitoring

The project includes monitoring with Prometheus and Grafana. Access Grafana at `http://localhost:3000` after starting the Docker containers.