from flask import Flask, request, jsonify, render_template, redirect
from .db import database
from bson import ObjectId

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/shorten")

@app.route("/shorten", methods=["GET", "POST"])
def shorten():
    if request.method == "GET":
        return render_template("home.html")

    elif request.method == "POST":
        data = request.form.to_dict()
        exist = database.find_one(data)
        if exist:
            _id = exist["_id"]
            url = request.origin + "/" + str(_id)
            return render_template("shorten.html", code=url)
        _id = database.insert_one(data).inserted_id
        url = request.origin + "/" + str(_id)
        return render_template("shorten.html", code=url)

@app.route("/<code>")
def trimmed(code):
    doc = database.find_one({"_id": ObjectId(code)})
    if not doc:
        return "URL doesn't exist"
    return redirect(doc["url"])