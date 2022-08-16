import pytest
import run


#создаем фикстуру для тестов вьюшек
@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()