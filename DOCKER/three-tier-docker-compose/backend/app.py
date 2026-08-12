from flask import Flask
import mysql.connector
import os
import time

app = Flask(__name__)

db = None

# Retry until MySQL is ready
while db is None:
    try:
        db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        print("Connected to MySQL")
    except Exception:
        print("Waiting for MySQL...")
        time.sleep(5)


@app.route("/")
def home():
    return "Backend API is Running"


@app.route("/database")
def database():
    cursor = db.cursor()
    cursor.execute("SELECT DATABASE();")
    return cursor.fetchone()[0]


app.run(host="0.0.0.0", port=5000)
