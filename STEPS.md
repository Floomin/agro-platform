cd C:\__PROJECTS__\agro-platform

# Инициализация проекта
uv init --name agro-platform --python 3.12

# Добавляем основные зависимости
uv add fastapi "uvicorn[standard]" sqlmodel alembic pydantic-settings structlog python-dotenv pyodbc pymssql

# Добавляем инструменты разработки
uv add --dev ruff pyright pytest pytest-asyncio httpx pytest-cov factory-boy

# Для авторизации (понадобится скоро)
uv add fastapi-users[sqlalchemy] fastapi-users-db-sqlalchemy

New-Item -ItemType Directory -Path src/core/auth -Force
New-Item -ItemType Directory -Path src/domains/land_bank/domain -Force
New-Item -ItemType Directory -Path src/domains/land_bank/application -Force
New-Item -ItemType Directory -Path src/domains/land_bank/infrastructure -Force
New-Item -ItemType Directory -Path src/domains/land_bank/api -Force
New-Item -ItemType Directory -Path src/domains/land_bank/features -Force
New-Item -ItemType Directory -Path tests/unit -Force
New-Item -ItemType Directory -Path tests/integration -Force
New-Item -ItemType Directory -Path tests/api -Force

New-Item -Path `
  src/main.py, `
  src/core/__init__.py, `
  src/core/config.py, `
  src/core/database.py, `
  src/core/auth/__init__.py, `
  alembic.ini, `
  .env.example, `
  README.md, `
  docker-compose.yml `
  -ItemType File -Force

  