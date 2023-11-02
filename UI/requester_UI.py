from flask import Flask, render_template, session, redirect, request
import requests
import json
from utils.authentication import Authentication

app = Flask(__name__)
authenticate = Authentication().authenticate
app.secret_key = "41!$bn"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


        url = 'http://127.0.0.1:5000/authentication'
        
        payload = {
                    'username':username,
                    'password':password
                   }
        
        response = requests.post(url, data=payload)
        print('response', response)
        data = response.json()  # This will parse the JSON content of the response
        status = data.get('status')
        message = data.get('message')
        print(status)
        print(message)
        if status:
            session["username"] = username
            return redirect('/')
        else:
            return render_template("login.html", error=message)
    return render_template("login.html")


@app.route('/', methods=['GET'])
def index():
    if 'username' not in session:
        return redirect('/login')
    
    url = 'http://127.0.0.1:5000/get_table/User'
    response = requests.get(url)
    data = response.json()  # This will parse the JSON content of the response
    data_value = data.get('data')
    

    
    # return render_template('dormant.html')
    return str(data_value)


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True,port=8000,host='0.0.0.0')