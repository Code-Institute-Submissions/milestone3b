import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
#from env import MONGO_URI #uncomment this line, and comment out lines 7-9 if using gitpod
if path.exists("env.py"):
    from env import MONGO_URI
MONGO_URI = os.environ.get('MONGO_URI')

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

@app.route('/submit_pun', methods=['POST']) #posts data collected on the addpun.html form to mongodb, then redirects to index.html
def submit_pun():
    puns=mongo.db.puns
    puns.insert_one(request.form.to_dict())
    return redirect(url_for('get_puns'))

@app.route('/profile/<pun_id>') #generates an individual page for each individual pun
def profile(pun_id):
    the_pun =  mongo.db.puns.find_one({"_id": ObjectId(pun_id)})
    return render_template('profile.html', pun=the_pun)

@app.route('/edit_pun/<pun_id>') #brings user to a form similar to addpun.html, but with the values already filled in for the respective pun to be edited
def edit_pun(pun_id):
    the_pun =  mongo.db.puns.find_one({"_id": ObjectId(pun_id)}) 
    return render_template('editpun.html', pun=the_pun)

@app.route('/update_pun/<pun_id>', methods=['POST']) #updates the pun with the data entered at editpun.html
def update_pun(pun_id):
    puns = mongo.db.puns
    puns.update({'_id': ObjectId(pun_id)},
    {
        'expression': request.form.get('expression'),
        'definition': request.form.get('definition'),
        'example': request.form.get('example'),
        'category': request.form.get('category')
    })
    return redirect(url_for('get_puns'))

@app.route('/delete_pun/<pun_id>') #deletes the selected pun
def delete_pun(pun_id):
    mongo.db.puns.remove({'_id': ObjectId(pun_id)})
    return redirect(url_for('get_puns'))

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "8080")), debug=True)