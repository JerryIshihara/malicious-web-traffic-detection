import pytest
import tempfile
import numpy as np
import os
import sys
sys.path.append('../model')
import model


@pytest.fixture
def client():
    # db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    model.app.config['TESTING'] = True
    with model.app.test_client() as client:
        # with model.app.app_context():
        #     model.init_db()
        yield client
    # os.close(db_fd)
    # os.unlink(flaskr.app.config['DATABASE']


def test_forward(client):
    """[summary: test baseline model forward pass]

    Args:
        client ([type: class]): [description: Flask test client]
    """
    # generate random int
    for state in np.random.randint(999, size=10):
        URL = f'/predict/{state}'
        response = client.get(URL)
        assert response.status_code == 200
        assert response.get_data().decode('utf-8') == str(state)
    # should fail on string input
    URL = '/predict/string'
    response = client.get(URL)
    assert response.status_code == 404