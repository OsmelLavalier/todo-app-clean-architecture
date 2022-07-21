# Todo-app-fastapi-clean-architecture

> It implements a clean repository-service architecture in FastAPI.

## Installing / Getting started

A quick introduction of the minimal setup you need to get a hello world up &
running.

```shell
git clone https://github.com/OsmelLavalier/todo-api-clean-architecture.git
cd todo-api-clean-architecture
docker-compose up --build
navigate to http://127.0.0.1:8000/docs
```

## Tests

For testing we are using pytest. The tests consist of create a fake database with same structure are original and overriding `get_db()` from `configs.base`.

```shell
docker-compose run api bash
pytest -v
```

## Git-Hooks

Support for git hooks using [pre-commit](https://pre-commit.com/). It uses [black](https://github.com/psf/black) for formatting for formatting and linting found at root dir in `.pre-commit-config.yaml`

## Migrations

It uses alembic for database migrations. Inside `versions` folder you can find all migrations.

### Generate a migration (no migrations)

```shell
alembic init alembic
alembic revision --autogenerate -m "name-of-your-migration"
```

### Generate a migration (from existing)

If you decided to alter the schema you will need to change add those changes to the database models in `models` folder

```
alembic upgrade head
or
alembic downgrade head
```

## Contributing

This project was solely develop to enhance my design pattern skills. If you have any ideas for future development feel free to open an issue and tell me what you think.

If you'd like to contribute, please fork the repository and make changes as
you'd like. Pull requests are warmly welcome.
