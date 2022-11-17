import pyrebase
firebaseConfig = {"apiKey": "AIzaSyC9v4B0zfcYAK6hh904xn9psE5sY1i57vA","authDomain": "hand-sign-detection-fc226.firebaseapp.com","databaseURL": "https://hand-sign-detection-fc226-default-rtdb.firebaseio.com",
  "projectId": "hand-sign-detection-fc226","storageBucket": "hand-sign-detection-fc226.appspot.com","messagingSenderId": "176249768824","appId": "1:176249768824:web:fc35567133b83dfb79d68d","measurementId": "G-RWZQXTTFZ8"
};
firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()
def pyrebase_sign(sign):
    database.child("hand sign").update({"hand sign":sign})