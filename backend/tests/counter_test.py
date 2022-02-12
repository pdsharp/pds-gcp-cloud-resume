import mockfirestore as fs
from counter.main import visitcount
from unittest.mock import patch


def test_get_db():
    db = fs.MockFirestore()
    counter = db.collection(u'counter').document(u'counter')
    counter.set({'count': 42})
    newcount = int(counter.get().to_dict()['count'])
    assert newcount == 42

@patch('counter.main.db', fs.MockFirestore())
def test_insert_db():
    response = visitcount(None)
    assert response[0] == '1'

def test_http_response():
    response = visitcount(None)
    assert response[1] == 200
