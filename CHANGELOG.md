# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2024-09-29

### Changed
- Deprecated frontend system; repository is now purely backend
- Eliminated dungeon and character services
- Monster and player models now inherit from new Entity parent class

### Added
- Implemented player service
- Added Prometheus and Grafana for monitoring
- Integrated Docker and Docker Compose for containerization
- Created comprehensive documentation

## [0.3.1] - 2024-09-22

### Changed
- Updated Character and Monster models to include XP
- Changed HP system to include current_hp and max_hp instead of a single hp field
- Updated corresponding test files to reflect these changes

## [0.3.0] - 2024-09-22

### Added
- Implemented services for Character and Dungeon
- Created endpoints for character and dungeon management
- Expanded unit tests to cover new services and endpoints

### Changed
- Updated API to include new services and endpoints

## [0.2.0] - 2024-09-22

### Added
- Implemented data models for Character, Monster, and Item
- Utilized Pydantic for data validation
- Configured examples for automatic documentation (SwaggerUI)
- Started using semantic versioning for project versions

### Changed
- To access the documentation, use `/redoc`

### Notes
- Used the following command for versioning:
  ```
  git tag -a v0.2.0 -m "v0.2.0 - Basic data models"
  ```

## [0.1.0] - 2024-09-21

### Added
- Initial project setup
- Basic project structure implementation
- FastAPI configuration with test endpoints
- Basic CI implementation with GitHub Actions

[Unreleased]: https://github.com/A-PachecoT/console-quest-rpg/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/A-PachecoT/console-quest-rpg/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/A-PachecoT/console-quest-rpg/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/A-PachecoT/console-quest-rpg/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/A-PachecoT/console-quest-rpg/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/A-PachecoT/console-quest-rpg/releases/tag/v0.1.0