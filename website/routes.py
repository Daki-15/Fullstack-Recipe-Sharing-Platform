# routes.py
from flask import render_template, request, redirect, url_for
from main import app, db


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    # Add your logic here
    return render_template('home.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Add your logic here
        pass
    return render_template('submit.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Add your logic here
        pass
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Add your logic here
        pass
    return render_template('login.html')
