import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/Who are you')
def cloudethix():
return 'Yes, I am cloudethix, and You !!!'

if __name__ == "__main__":
    app.run()
