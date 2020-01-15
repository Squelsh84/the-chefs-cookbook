import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
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


# View All Recipes
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())


# Show Individual Recipe
@app.route('/viewrecipe/<recipe_id>')
def recipes(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('viewrecipe.html', title=recipe['recipe_name'], recipe=recipe)


# Add Recipe
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', title='Add Recipe', categories=mongo.db.categories.find(),
                           difficulty=mongo.db.difficulty.find())


@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    flash('You have added a new recipe successfully!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
