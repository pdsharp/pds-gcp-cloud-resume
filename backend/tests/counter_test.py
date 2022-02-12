import mockfirestore as fs
from counter.main import visitcount
from unittest.mock import patch



@patch('counter.main.db', fs.MockFirestore())
def test_visitcount():
#    db = fs.MockFirestore()
#    counter = db.collection(u'counter').document(u'counter')
#    counter.set({'count': 3})
    response = visitcount(None)
    print(response)
    assert response[0] == '1'
    assert response[1] == 200