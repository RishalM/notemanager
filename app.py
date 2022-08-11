from flask_moment import Moment
from datetime import datetime
import pymongo
import os
from flask import Flask, redirect, render_template, request
app = Flask(__name__)
moment = Moment(app)
if os.environ.get("MONGO_URI") == None: #we are running the code on our computer. If we run on our computer, os.environ.get("MONGO_URI") will be none
    file = open("connectionString.txt","r")
    content = file.read().strip()
    file.close()
else: # we are running this code on Heroku's computer. Here, os.environ.get("MONGO_URI") will not be none -- instead it will be the connection string.
    content = os.environ.get("MONGO_URI")
client = pymongo.MongoClient(content)
database = client["NoteManager"]
collection = database["Notes"]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addnote", methods = ["GET","POST"])
def addnote():
    if request.method == "GET":
        return render_template("addnote.html")
    else:
        noteinfo = request.form
        noteAuthor = noteinfo['Note Author']
        noteContent = noteinfo['Note Content']
        record1 = {"noteAuthor":noteAuthor,"noteContent":noteContent,"timeOfCreation":datetime.utcnow()}
        collection.insert_one(record1)
        return redirect ("/addnote")

@app.route("/shownotes")
def shownote():
    allnotes = collection.find()
    notes = []
    name = "Rishal"
    fruits = ["strawberry","blueberry","banana","apple"]
    for each in allnotes:
        notes.append(each)
    return render_template("shownote.html",notes = notes)

if __name__ == "__main__":
    app.run()