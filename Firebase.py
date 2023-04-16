import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('wizarduo-Key.json')

# Initialize the Firebase app with the service account credentials
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://wizarduo-1126f-default-rtdb.firebaseio.com/'
})

# Reference to the root node of the Firebase Realtime Database
ref = db.reference('/')

# Create a reference to the "Users" node and push new user data
users_ref = ref.child('Users')
users_ref.child('id1').set({
    'name': 'Pradeep1',
    'email': 'Pradeep@gmail.com',
    'public_key': '123tdwhdw76qewvdx628237fvq67329g'
})
users_ref.child('id2').set({
    'name': 'Pradeep2',
    'email': 'Pradeep2@gmail.com',
    'public_key': '123tdwhdw76qewvdx628237fvq67329gdtsjda6'
})

# Create a reference to the "Collections" node and push new collection data
collections_ref = ref.child('Collections')
collections_ref.child('hash').set({
    'owner_key': '13245shdsc67dewg2178ewdhjbdc89',
    'Title': 'Sample2',
    'timestamp': '31-01-03'
})

# Retrieve data from the Firebase Realtime Database
#users = ref.child('').get()
#print(users)
