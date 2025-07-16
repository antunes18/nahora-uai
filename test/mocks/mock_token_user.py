import pytest

from time import time
import jwt

TEST_SECRET_KEY = "chave-secreta-para-testes-nao-use-em-prod"
TEST_ALGORITHM = "HS256"
TEST_ACCESS_TOKEN_EXPIRE_MINUTES = 60


def generate_test_jwt(email: str = "teste_de_user1@example.com", username: str = "teste"):
    payload = {
        "email": email,
        "username": username,
        "role": "admin",
        "exp": time() + 3600,
    }
    token = jwt.encode(payload, TEST_SECRET_KEY, algorithm=TEST_ALGORITHM)
    return token


@pytest.fixture
def auth_header():
    """Fixture to provide a valid authorization header."""
    token = generate_test_jwt(
        email="teste_de_user1@example.com", username="teste")
    return {"Authorization": f"Bearer {token}"}
