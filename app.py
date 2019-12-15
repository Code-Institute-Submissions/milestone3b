import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from env import MONGO_URI

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'suburbanDictionary'
app.config["MONGO_URI"] = (MONGO_URI)

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_puns')
def get_puns():
    return render_template("index.html", puns=mongo.db.tasks.find())


if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "8080")), debug=True)