from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask import redirect
import scrapingchallenge

#setup flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#define homepage route
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#define Scrape page route that will update the content with followng function call
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scrapingchallenge.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)
   #return "Scrapping was successfull"


#tell flask to run
if __name__ == "__main__":
    app.run()