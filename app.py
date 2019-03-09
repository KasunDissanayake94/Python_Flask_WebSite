import flask
from flask import render_template
import pymysql

app = flask.Flask(__name__)
app.config["DEBUG"] = True
conn = pymysql.connect(host="localhost",
                       user="root",
                       passwd="",
                       db="myfirst_api")    

cur = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def display_home_page():
    return render_template('homepage.html')



@app.route('/register', methods=['POST', 'GET'])
def insert_user_details():

    if flask.request.method == 'POST':
        first_name = flask.request.form['fname']
        last_name = flask.request.form['lname']
        email = flask.request.form['email']
        contact_number = flask.request.form['cnumber']
        password = flask.request.form['pwd']

        if first_name and last_name and email and contact_number and password:

            cur.execute("INSERT INTO myfirst_api.user(First_name,Last_name,Email,Password,Contact_Number)"
                " VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, email,password, contact_number))
            conn.commit()
        return render_template('login.html')
    else:
        return render_template('register.html')    
@app.route('/login', methods=['POST', 'GET'])
def login():

    if flask.request.method == 'POST':
        email = flask.request.form['email']
        password = flask.request.form['password']
        if email and password:
            cur.execute("SELECT First_Name FROM myfirst_api.user where Email=%s and Password=%s", [email, password])
            data = cur.fetchall()
            print(data)
            return render_template('user_profile.html',data=data)
    else:
        return render_template('login.html')
  
app.run()