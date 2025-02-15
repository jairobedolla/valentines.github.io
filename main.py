import os

from flask import Flask, request, redirect, session, url_for, render_template, flash, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/next')
def next_page():
    return render_template('next.html')

@app.route('/me')
def me():
    return render_template('me.html')

@app.route('/you')
def you():
    return render_template('you.html')

@app.route('/choice')
def choice():
    return render_template('choice.html')

@app.route('/yes')
def yes():
    return render_template('yes.html')

@app.route('/no')
def no():
    return render_template('no.html')

@app.route('/maybe')
def maybe():
    return render_template('maybe.html')




if __name__ == '__main__':
    app.run(port=8000, debug=True)