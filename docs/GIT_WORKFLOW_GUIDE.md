# Git Workflow Guide

## Branching Strategy

We use a simplified Git flow with the following branches:

- `main`: Production-ready code
- `develop`: Integration branch for features
- Feature branches: For new features or bug fixes

## Workflow

1. Create a new branch from `develop` for your feature or bug fix:
```
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

2. Make your changes and commit them using [conventional commits](https://www.conventionalcommits.org):
```
git add .
git commit -m "feat: add new feature"
```

3. Push your branch to the remote repository:
```
git push origin feature/your-feature-name
```

4. Create a pull request to merge your feature branch into `develop`.

5. After review and approval, merge the pull request.

6. Delete the feature branch after merging.

## Conventional Commits

We use conventional commits to standardize commit messages. The format is:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types include:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

Example:
```
feat(api): add endpoint for user registration

- Implement user registration logic
- Add input validation
- Create database schema for users

Closes #123
```

## Versioning

We use semantic versioning (SemVer) for release versions. To create a new version:

```
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

Remember to update the CHANGELOG.md file with each new version.