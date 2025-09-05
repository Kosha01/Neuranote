import firebase_admin
from firebase_admin import credentials, firestore, storage, messaging
import os

cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
firebase_admin.initialize_app(cred, {
    'storageBucket': f"{os.getenv('FIREBASE_PROJECT_ID')}.appspot.com"
})

db = firestore.client()
bucket = storage.bucket()

