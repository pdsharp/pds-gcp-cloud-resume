from google.cloud import firestore


db = firestore.Client()

def visitcount(request, db):
    counter = db.collection(u'counter').document(u'counter')
    try:
        newcount = int(counter.get().to_dict()['count']) + 1
        counter.set({'count': newcount})
    except (TypeError):
        newcount = 1
        counter.set({'count': newcount})
    return {
	    'body': newcount,
	    'statusCode': 200,
	    'headers': {'Access-Control-Allow-Origin': '*'}
    }