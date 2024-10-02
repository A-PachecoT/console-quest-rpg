# Console Quest RPG

## Description
Console Quest RPG is a turn-based role-playing game developed as a software project for the CC3S2 course at the National University of Engineering. The game uses FastAPI for the backend and is designed to be played through a console interface.

### Team Members
- Pacheco André - 20222189G
- Pezo Sergio - 20224087G
- Torres Oscar - 

## Documentation

For detailed information, please refer to the following documentation:

- [Developer Guide](./docs/DEVELOPER_GUIDE.md): Instructions for setting up the development environment, including Black formatter usage and Docker commands.
- [API Documentation](./docs/API_DOCUMENTATION.md): Detailed information about the API endpoints and how to use them.
- [Git Workflow Guide](./docs/GIT_WORKFLOW_GUIDE.md): Guidelines for contributing to the project using Git.
- [Changelog](./CHANGELOG.md): A detailed list of changes for each version of the project.

- [Answers](./docs/ANSWERS.md): The first test's answers.

## Project Structure
```
console-quest-rpg/
├── .github/
│   └── workflows/
│       └── ci.yml
├── backend/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── tests/
├── compose.yml
├── frontend/
│   ├── app/
│   ├── Dockerfile
│   └── main.py
├── grafana
│   └── main-dashboard.json
├── prometheus_data/
│   └── prometheus.yml
├── CHANGELOG.md
└── README.md
```

## Versions

[Version history moved to CHANGELOG.md](./CHANGELOG.md)

## Quick Start

1. Clone the repository:
```
git clone https://github.com/A-PachecoT/console-quest-rpg.git
cd console-quest-rpg
```
2. Create the directory for grafana volume:
```
mkdir -p grafana_data
```

3. Start the application:
```
docker compose up --build -d
```

4. Enjoy the game.

See the tutorial game in [Answers](./docs/ANSWERS.md).


For more detailed instructions of the code, please refer to the [Developer Guide](./docs/DEVELOPER_GUIDE.md).


## Database

The project uses MongoDB as its database. The connection to MongoDB is made using Motor, an asynchronous driver for MongoDB.

More information in [Answers](./docs/ANSWERS.md).

## Monitoring

The project includes monitoring with Prometheus and Grafana.

More information in [Answers](./docs/ANSWERS.md).
