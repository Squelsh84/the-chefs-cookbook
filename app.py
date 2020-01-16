import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime


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


# Insert Recipe
@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    today = datetime.now().strftime("%m-%d-%Y")
    recipes = mongo.db.recipes
    new_recipe = {
        "recipe_name": request.form.get("recipe_name"),
        "recipe_description": request.form.get("recipe_description"),
        "recipe_prep": request.form.get("recipe_prep"),
        "recipe_cook": request.form.get("recipe_cook"),
        "recipe_serving": request.form.get("recipe_serving"),
        "recipe_image": request.form.get("recipe_image"),
        "recipe_ingredients": request.form.getlist("recipe_ingredients"),
        "recipe_method": request.form.getlist("recipe_method"),
        "recipe_category": request.form.get("recipe_category"),
        "recipe_difficulty": request.form.get("recipe_difficulty"),
        "recipe_author": request.form.get("recipe_author")
    }
    recipes.insert_one(new_recipe)
    flash('You have added a new recipe successfully!', 'success')
    return redirect(url_for('index'))


# Edit and Update Recipe
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
      recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    difficulties = mongo.db.difficulties.find()
    return render_template('editrecipe.html', 
                           title='Edit Recipe', 
                           recipe=recipe, 
                           categories=categories, 
                           difficulty=difficulty)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
