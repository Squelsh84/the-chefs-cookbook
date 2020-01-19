
# [The Chefs Cookbook](https://the-chefs-diary.herokuapp.com/index)

# UX

The Chefs Cookbook is a website created to help people like me to keep all their recipes in one place and also maybe find some new ones shared by others. I lived with chefs for many years and most of my recipes were written on pieces of paper or on the  back of envelopes and have disapeared over time. So after loosing so many recipes, I decided enough was enough and created the chefs cookbook for my chef friends to share all thier recipes with me again.

## User Stories

### User Story 1 - Find A Recipe

I'm tired of the same old food and want to try something different. I want to see new recipes with different skill levels.

### User Story 2 - Add A New Recipe

I've found a great recipe in a magazine but dont want to buy it just for the recipe.

### User Story 3 - Share A Recipe

My friend ask me for the recipe for the dish I cooked the other night at our dinner party.

### User Story 4 - Print The Recipe

I'm heading into town and dont have any battery left in my phone. I want to print it out to bring with me for the ingredients.

## Design



### Navigation



### Colours & Fonts



# Wireframe

I decided to use balsamiq to create my mock-ups because it is easy to use and gave me a real visual of what I wanted to implement. These can be found [here]() 

# Pages

## Home Page


## Register New Account Page

- Any user can join the commnity by creating a new account. Before the account is created the username is check to     ensure that it hasn't been created before. Users passwords are hashed for security purposes and once all criteria    is met they are redirected to the home page. If a user has an account already then they can click the link to the    login page.

## Login User Page

- Users can easily log into their accounts by providing their username and password. The password will be cross        checked with the password in the database. If the username or password are incorrect a message will flash saying     "Username of password are incorrect". When the user enters in their username and password correctly they are         redirected to the home page and a message flashes saying "You're Logged in."
  
## View Recipes Page

- All recipes are displayed on the recipes page. Each recipe displays a little bit of information about the recipe.    If a user wants to see more they can click on the image and will be redirected to that recipes page. If a user       wants to see a specific category they can click on the recipes tab on the navbar and select the specific category.

## Add Recipe Page

- 

## Edit Recipe Page

-

## Future Features

There are alot of features that could be added in the future. Some that I would like to implement are -

- If the view recipe page is refreshed, then the ingredients marked as already got are still marked and not reset.
- Create a Search bar to make navigation faster towards a specific recipe.
- To have a users page which shows all their information such as added recipes, most liked recipe and comments on      their recipes.  
- A password reset for users who have forgotten their passwords.
- A pop-up to easily convert measurements.
- To have it it multiply languages so it can be used worldwide.

# Database Design

Please find below the structure I used for my database using MongoDB.

**Collection name:** `users`

```{
    "_id": <ObjectId>,
    "user_name": <string>,
    "email": <string>,
    "password": <string>
}
```

**Collection name:** `categories`

```{
    "_id": <ObjectId>,
    "category": <string>
}
```

**Collection name:** `difficulty`

```{
    "_id": <ObjectId>,
    "difficulty": <string>
}
```

**Collection name:** `recipes`

```{
    "_id": <ObjectId>,
    "recipe_name": <String>,
    "recipe_description": <String>,
    "recipe_time": <String>,
    "recipe_image": <String>,
    "Recipe_ingredients": <Array>,
    "Recipe_method": <Array>,
    "recipe_author": <String>,
}
```

# Technologies & Programmes Used

## Languages

- [HTML](https://www.w3.org/)
- [CSS](https://www.w3.org/)
- [JavaScript](http://www.ecma-international.org/)
- [Python](https://www.python.org/)

## Development Tools

- [Visual Studio Code](https://code.visualstudio.com/) IDE used.
- [Git](https://git-scm.com/) Used to track changes during development.
- [GitHub](https://github.com/) Used to host the version control system and website content before deployment to Heroku.

## Hosting Platforms & Database

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) Cloud based database service used.
- [Heroku](https://www.heroku.com/) Cloud based hosting service used.

## Frontend Resources

- [Google Fonts](https://fonts.google.com/) Used for all fonts.
- [Font Awesome](https://fontawesome.com/) Used for all icons.
- [Bootstrap](https://getbootstrap.com/) Used for responsive layout and styling.


## Design Tools

- [Balsamiq](https://balsamiq.com/) Used to develop wireframes for the website.


# Testing



# Deployment

The website was developed in Visual Studio Code using a virtual environment and deployed to Heroku via GitHub.

The following instructions to clone and deploy assume the user has:

- IDE
- Python 3
- Pip
- Virtual Environment
- GitHub Account
- MongoDB Atlas Account
- Heroku Account

## Clone in GitHub

The following instructions were taken from [GitHib Help]( https://help.github.com/en/articles/cloning-a-repository).

1. Open the [The Chefs Cookbook](https://github.com/Squelsh84/the-cookbook) repository.
2. Click the **clone or download** button.
3. In the **clone with HTTPs** pop-up, click the **copy icon**.
4. Open **git bash**.
5. Change the current working directory to where you want the cloned directory to be made.
6. Type **git clone** and paste the URL copied earlier.
7. Press **enter**.

## Create MongoDB Atlas Database

1. On the [MongoDB](https://cloud.mongodb.com/user#/atlas/login) website log into your Atlas account.
2. Under **cluster/ collections** click **create database** and enter a **database name** and **collection name**.
3. Click **create collection** to add more collections as per the database design above.
4. Under **cluster/ overview** click **connect**.
5. Click **connect your application**.
6. Select **Python** as the **driver** and select the **version**.
7. Copy the connection string `mongodb+srv://root:<password>@myfirstcluster-fgb6v.azure.mongodb.net/test?retryWrites=true&w=majority`.

## IDE Development Setup

1. Add the `MONGO_URI` to your environment file for local deployment. Replace `<password>` with your **password** and `test` with your **database name**.
2. Add a `SECRET_KEY` to your environment file.
3. Use `pip install -r requirements.txt` to install requirements.

## Deploy to Heroku

1. On the [Heroku](https://id.heroku.com/login) website log into your account.
2. Click **new** and **create new app**.
3. Give your app a **name** (it must be unique), select a **region** and click **create app**.
4. Under **deployment method** click **GitHub**.
5. Under **connect to GitHub** select your **repository**, enter the **repo-name** and click **search**.
6. Click the **connect** button that appears under your repository and repo-name.
7. Under **settings/ config vars** click **reveal vars**.
8. Enter **IP** for key, **0.0.0.0** for value and click **add**.
9. Enter **MONGO_URI** for key, **your uri** for value and click **add**.
10. Enter **SECRET_KEY** for key, **your secret key** for value and click **add**.
11. Under **deploy/ manual deploy** click **deploy branch**.
12. Under **resources/ free dynos** click **edit** and **confirm**.

# Credits

## Content

- Some recipes were taken from [bbcgoodfood website](https://www.bbcgoodfood.com/)
- Images from the carousel were taken from [pixabay](https://pixabay.com/)
- Quotes are from [google](https://google.com/)
  
## Code

- [Corey Schafer - Youtube Flask Series](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
- [Pretty Printed](https://www.youtube.com/results?search_query=pretty+printed+flask+login)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Flask Documentation](http://flask.palletsprojects.com/en/1.1.x/)

## Acknowledgements

- Another big thank you to my mentor Seun Owonikoko who guided me through another projectand to all the great people on Slack who take give their time to answer peoples questions. Many problems I have encountered have already been answered there.