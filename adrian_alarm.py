import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate('admin.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://makentu-c3a48.firebaseio.com'
})

sleep = db.reference()
sleep.update({'sleep': 1})
