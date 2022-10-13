import pytest
import io
from data_engineering_prj.app import app


@pytest.fixture
def client():
    return app.test_client()


def test_index_renders(client):
    result = client.get('/')
    assert b'form' in result.data


def test_process_works(client):
    result = client.post(
        '/process',
        data={"input_csv": (io.BytesIO(b'bone1,muscle1,10.0\n'), 'input_csv')}
    )
    assert result.data == b'[10.0]'
