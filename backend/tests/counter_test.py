import mockfirestore as fs
from counter.main import visitcount


def test_counter():
    db = fs.MockFirestore()
    counter = db.collection(u'counter').document(u'counter')
    counter.set({'count': 1})
    response = visitcount(None, db)
    assert response['body'] == 2
    assert response['statusCode'] == 200