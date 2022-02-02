from google.cloud import firestore
from flask import jsonify

db = firestore.Client()

def visitcount(request):
    counter = db.collection(u'counter').document(u'counter')
    newcount = int(counter.get().to_dict()['count']) + 1
    counter.set({'count': newcount})
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    return jsonify(newcount), 200, headers