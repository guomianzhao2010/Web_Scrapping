
from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"]  = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    
    info=mongo.db.mars.find_one()
    return render_template("index.html", info=info)


@app.route("/scrape")
def scraper():

    empty=mongo.db.mars
    mars_info=scrape_mars.scrape()
    empty.update({}, mars_info, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)