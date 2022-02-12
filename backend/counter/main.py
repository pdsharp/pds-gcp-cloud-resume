from google.cloud import firestore


db = firestore.Client()

def visitcount(request):
    counter = db.collection(u'counter').document(u'counter')
    try:
        newcount = int(counter.get().to_dict()['count']) + 1
        counter.set({'count': newcount})
    except (TypeError, KeyError):
        newcount = 1
        counter.set({'count': newcount})
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
        }
    return (f"{newcount}", 200, headers)