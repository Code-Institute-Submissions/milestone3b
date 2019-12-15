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
    return render_template("index.html", puns=mongo.db.puns.find())

@app.route('/add_pun') #opens up the page for submitting a pun
def add_pun():
    return render_template("addpun.html")

@app.route('/submit_pun', methods=['POST']) #posts data collected on the submit.html form to mongodb, then redirects to index.html
def submit_pun():
    puns=mongo.db.puns
    puns.insert_one(request.form.to_dict())
    return redirect(url_for('get_puns'))

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "8080")), debug=True)