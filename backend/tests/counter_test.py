import mockfirestore as fs
from counter.main import visitcount
from unittest.mock import patch

@patch('counter.main.db', fs.MockFirestore())
def test_visitcount():
    response = visitcount(None)
    assert response[0] == '1'
    assert response[1] == 200