from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

@app.route("/")
def home():
    return "Backend Connected Successfully!"

@app.route("/db")
def dbcheck():
    cursor = db.cursor()
    cursor.execute("SELECT DATABASE();")
    return cursor.fetchone()[0]

app.run(host="0.0.0.0", port=5000)
