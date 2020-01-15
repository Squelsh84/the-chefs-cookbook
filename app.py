import os
from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


# Home
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='home')


# Add Recipe
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', title='Add Recipe')


@app.route('/insert_recipe')
    def insert_recipe():
        recipes=mongo.db.recipes
        return render_template('recipes.html')






@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
