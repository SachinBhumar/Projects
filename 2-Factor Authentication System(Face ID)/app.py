from flask import Flask, render_template, request, redirect, url_for
import json
from face_verify import verify_face

app = Flask(__name__)

USERS_FILE = "users.json"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    with open(USERS_FILE, "r") as f:
        users = json.load(f)

    if username in users and users[username] == password:
        return redirect(url_for('face_auth', username=username))
    else:
        return render_template('failure.html', message="Invalid credentials")

@app.route('/face_auth/<username>')
def face_auth(username):
    success = verify_face(username)
    if success:
        return render_template('success.html', username=username)
    else:
        return render_template('failure.html', message="Face verification failed")

if __name__ == '__main__':
    app.run(debug=True)














