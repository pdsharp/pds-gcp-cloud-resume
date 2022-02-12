import mockfirestore as fs
from counter.main import visitcount
from unittest.mock import patch

@patch('counter.main.db', fs.MockFirestore())
def test_visitcount():
    db = fs.MockFirestore()
    counter = db.collection(u'counter').document(u'counter')
    counter.set({'count': 42})
    newcount = int(counter.get().to_dict()['count'])
    response = visitcount(None)
    assert newcount == 42
    assert response[0] == '1'
    assert response[1] == 200