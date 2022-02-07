from google.cloud import firestore
from flask import jsonify

db = firestore.Client()

def visitcount(request):
    counter = db.collection(u'counter').document(u'counter')
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    try:
        newcount = int(counter.get().to_dict()['count']) + 1
        counter.set({'count': newcount})
    except (TypeError):
        newcount = 1
        counter.set({'count': newcount})
    return jsonify(newcount), 200, headers