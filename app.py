from chatbot import chatbot  # Ensure chatbot loads trained responses
from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
from flask_recaptcha import ReCaptcha
from markupsafe import Markup
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.static_folder = 'static'

# ReCaptcha Configuration
app.config.update(
    RECAPTCHA_ENABLED=True,
    RECAPTCHA_SITE_KEY="6LdbAx0aAAAAAANl04WHtDbraFMufACHccHbn09L",
    RECAPTCHA_SECRET_KEY="6LdbAx0aAAAAAMmkgBKJ2Z9xsQjMD5YutoXC6Wee"
)
recaptcha = ReCaptcha(app=app)

# Database Connection
conn = mysql.connector.connect(host="localhost", user="root", password="", database="register")
cur = conn.cursor()

@app.route("/index")
def home():
    if 'id' in session:
        return render_template('index.html')
    return redirect('/')

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/forgot')
def forgot():
    return render_template('forgot.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    
    cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    users = cur.fetchall()
    
    if users:
        session['id'] = users[0][0]
        flash('You were successfully logged in')
        return redirect('/index')
    
    flash('Invalid credentials!')
    return redirect('/')

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('uemail')
    password = request.form.get('upassword')
    
    cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    conn.commit()
    
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    myuser = cur.fetchone()
    
    flash('You have successfully registered!')
    session['id'] = myuser[0]
    return redirect('/index')

@app.route('/suggestion', methods=['POST'])
def suggestion():
    email = request.form.get('uemail')
    suggesMess = request.form.get('message')
    
    cur.execute("INSERT INTO suggestion (email, message) VALUES (%s, %s)", (email, suggesMess))
    conn.commit()
    
    flash('Your suggestion has been successfully sent!')
    return redirect('/index')

@app.route('/verify_recaptcha', methods=['POST'])
def verify_recaptcha():
    if recaptcha.verify():
        flash('Recaptcha verified successfully!')
        return redirect('/register')
    
    flash('Recaptcha verification failed!')
    return redirect('/register')

@app.route('/logout')
def logout():
    session.pop('id', None)
    return redirect('/')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')  
    return str(chatbot.get_response(userText))  # Fetch response from trained model

if __name__ == "__main__":
    app.run(debug=True)
