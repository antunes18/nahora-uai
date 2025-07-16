# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient
from alembic.config import Config
from alembic import command

from api.core.database import Base, get_db
from api.core.main import app

# Usando SQLite em memória para testes
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///teste.db:memory:"

# Engine síncrono
engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session factory
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


def run_migrations():
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", SQLALCHEMY_TEST_DATABASE_URL)
    command.upgrade(alembic_cfg, "head")


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    run_migrations()
    yield
    # Optionally: drop tables after the session


@pytest.fixture(scope="function")
def db_session_for_test():
    # Cria as tabelas
    Base.metadata.create_all(bind=engine)
    run_migrations()

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session_for_test):
    def override_get_db():
        yield db_session_for_test
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides = {}
