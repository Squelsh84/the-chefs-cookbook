
# [The Chefs Cookbook](https://the-chefs-diary.herokuapp.com/index)

![Responsive Dashboard](https://github.com/Squelsh84/the-cookbook/blob/master/static/img/website.png)

## Table of Contents

1. [UX](#ux)
    - [User Stories](#user-stories)
    - [Design](#design)

2. [Wireframes](#wireframe)

3. [Features](#features)
    - [Current Features](#current-features)
    - [Future Features](#future-features)

4. [Database Design](#database-design)

5. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Tools](#tools)

6. [Testing](#testing)
    - [User Testing](#user-testing)
    - [Testing on Browsers](#testing_on_browsers)
    - [Manual Testing](#manual-testing)
    - [Validators](#validators)

7. [Deployment](#deployment)
    - [Clone in Github](#clone-in-github)
    - [MongoDB Atlas Database](#mongodb-atlas-database)
    - [Heroku Deployment](#deploy-to-heroku)

8. [Credits](#credits)
    - [Content](#content)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

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

### Theme

- The idea for the theme was to keep it simple and not over crowded with information. I wanted to keep it simple for  ease of navigation. Some ideas came from this [website](https://preview.themeforest.net/item/ranna-food-recipe-blog-bootstrap-4-template/full_screen_preview/23245048?_ga=2.101376133.508568564.1577723273-1672125964.1570478969)

### Typography

- I have kept the font to just one. I went with a very easy and readible font Montserrat, which is always a popular    font and it's easy to see why.

# Wireframe

- I decided to use balsamiq to create my mock-ups because it is easy to use and gave me a real visual of what I        wanted to implement. These can be found [here](https://github.com/Squelsh84/the-cookbook/tree/master/wireframes).

# Features

## Current Features

### Home Page

- Any user that arrives at the home page can view recipes by category. If they have an account they can log in on by   the link in the navbar. If they don't have an account they have the option to register. Once the user logs in the    navbar will change and have the options to view recipes, add recipes and logout.

### Register New Account Page

- Any user can join the commnity by creating a new account. Before the account is created the username is check to     ensure that it hasn't been created before. Users passwords are hashed for security purposes and once all criteria    is met they are redirected to the home page. If a user has an account already then they can click the link to the    login page.

### Login User Page

- Users can easily log into their accounts by providing their username and password. The password will be cross        checked with the password in the database. If the username or password are incorrect a message will flash saying     "Username of password are incorrect". When the user enters in their username and password correctly they are         redirected to the home page and a message flashes saying "You're Logged in."
  
### Create Recipe Page

- If a user is signed up and logged in they can add a recipe to the database. The add recipe page is a form with       each section being mandatory. If a user misses a a part they will be reminded when the click the add button. For     the ingredients and method section they can add and remove lines as its one instruction per line. For the category   and difficulty sections it is a dropdown to choose from. Once all fields are filled they can add the recipe.

### View Recipes Page

- All recipes are displayed on the recipes page. Each recipe displays a little bit of information about the recipe.    If a user wants to see more they can click on the image and will be redirected to that recipes page. If a user       wants to see a specific category they can click on the recipes tab on the navbar and select the specific category.

### Update/Edit Recipe Page

- A user has the option to update their own recipes. They must be logged in to view this option att the bottom of      their recipe. If they want to update their recipe it will bring them to update recipe page where they can add or     remove what they need.  

### Delete Recipe

- Users can only delete their own recipes. The user must be logged in to have this option. When the user is logged in and the usernames match the delete option becomes available. The delete button when click will activate a pop-up to confirm that the user really wants to delete the recipe. If they are sure the can click delete, if pressed by mistake they can close the pop-up and continue what they were doing.

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

--Collection name:-- `users`

```{
    "_id": <ObjectId>,
    "user_name": <string>,
    "email": <string>,
    "password": <string>
}
```

--Collection name:-- `categories`

```{
    "_id": <ObjectId>,
    "category": <string>
}
```

--Collection name:-- `difficulty`

```{
    "_id": <ObjectId>,
    "difficulty": <string>
}
```

--Collection name:-- `recipes`

```{
    "_id": <ObjectId>,
    "recipe_name": <String>,
    "recipe_description": <String>,
    "recipe_prep": <String>,
    "recipe_cook": <String>,
    "recipe_image": <String>,
    "Recipe_ingredients": <Array>,
    "Recipe_method": <Array>,
    "recipe_cat": <String>,
    "recipe_dif": <String>,
    "recipe_author": <String>,
}
```

# Technologies Used

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

## User Testing

- The website was shared with friends and family to test. When testing there were some issues with design. The block   of information of difficulty and prep time was sitting to the left. To fix this i added a media query to             justify-content: center;. Apart from this there were no major issues reported back.

## Testing on Browsers

- As I don't have every type of screen size and ocomputer on hand I used browserstack to help test across multiply     browsers. While I have google chrome and internet explorer available to me I used their developmet tools to help     with adjusting css and also to see if I had any errors in the console.

## Manual Testing

### Landing Page

- Each button and link was test on the landing page. Social media icons were tested to ensure the opened in a new      tab. The page was also tested to see if unregistered user had access to the add recipe tab.

### Register an Account

- To test the register account I created various test accounts. After creating a new account I would try to recreate   an account using  the same username. When doing this it would flash a message saying it was already used.

### Login User

- After creating test accounts I logged out and tried to log back in again. When first creating this I ran into        issues with the hashing of the password. I tried using Flask-bycrpt to begin but after not being able to get it to   function I went with Bycrpt. Also only after logining in is the add recipe tab displayed.

### Add Recipe

- I ran into some issues at the begining when trying to get the recipe to add more than one ingredient. Instead of     saving it as an array it would save it as a string. To get arround this I created and add and remove button fo       each ingredient and cooking step.

### Read Recipe

- Each recipe that is added can be seen on the recipe page. When clicked on you can view the recipe. To the            ingredients section I added a checkbox to mark what ingredients you have. An issue I had with this is that when      the page is refreshed the boxs are reset. I could not fix this issue after many tries and hope to fix it in the      future.

### Edit Recipe

- The biggest challenge for me was the edit recipe page. After testing the page I found out I was getting the recipe   but when posted to update it wasn't finding the recipe. After two days of trying to get this to work and with some   help I discover that I had the id wrong in the form and that I was url_for the wrong address. This was the most      frustrating and biggest issue I had throughout this project.

### Delete the Recipe

- The edit and delete buttons are only available to the user who created the recipe. This is done by verifying the     username is in session. Once all these have been confirmed the recipe can be deleted. In the begining I noticed      that it was too easy to delete a recipe, so I added a modal to the delete recipe button. I created thi so the user   must really want to delete the recipe.

### Print Recipe

- An added Feature to the view recipe page is the print the recipe button. This was tested on multple platforms to     check funtionality and to see if it really printed. Also it helps to save the recipe as a pdf if unable to print.

## Validators

- [W3c validator](https://validator.w3.org/) to validate both HTML and CSS. I copied my code and pasted it into the validator to check for errors and warnings.

- [JSHint](https://jshint.com/) was used to validate JavaScript.

- [PEP8 Online](http://pep8online.com/) was used to check everything was right with code.

- [BrowserStack](https://www.browserstack.com/) was used to test across multiple browsers.

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
2. Click the --clone or download-- button.
3. In the --clone with HTTPs-- pop-up, click the --copy icon--.
4. Open --git bash--.
5. Change the current working directory to where you want the cloned directory to be made.
6. Type --git clone-- and paste the URL copied earlier.
7. Press --enter--.

## MongoDB Atlas Database

1. On the [MongoDB](https://cloud.mongodb.com/user#/atlas/login) website log into your Atlas account.
2. Under --cluster/ collections-- click --create database-- and enter a --database name-- and --collection name--.
3. Click --create collection-- to add more collections as per the database design above.
4. Under --cluster/ overview-- click --connect--.
5. Click --connect your application--.
6. Select --Python-- as the --driver-- and select the --version--.
7. Copy the connection string `mongodb+srv://root:<password>@myfirstcluster-fgb6v.azure.mongodb.net/test?retryWrites=true&w=majority`.

## Deploy to Heroku

1. On the [Heroku](https://id.heroku.com/login) website log into your account.
2. Click --new-- and --create new app--.
3. Give your app a --name-- (it must be unique), select a --region-- and click --create app--.
4. Under --deployment method-- click --GitHub--.
5. Under --connect to GitHub-- select your --repository--, enter the --repo-name-- and click --search--.
6. Click the --connect-- button that appears under your repository and repo-name.
7. Under --settings/ config vars-- click --reveal vars--.
8. Enter --IP-- for key, --0.0.0.0-- for value and click --add--.
9. Enter --MONGO_URI-- for key, --your uri-- for value and click --add--.
10. Enter --SECRET_KEY-- for key, --your secret key-- for value and click --add--.
11. Under --deploy/ manual deploy-- click --deploy branch--.
12. Under --resources/ free dynos-- click --edit-- and --confirm--.

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
- [Checkbox Ingredients](https://bootsnipp.com/snippets/j6xjx)
- [Add Ingredients](https://stackoverflow.com/questions/9173182/add-remove-input-field-dynamically-with-jquery)

## Acknowledgements

- Another big thank you to my mentor Seun Owonikoko who guided me through another project and also a special thank you to Joke Heyndels who saved me on the last day by helping me greatly with my project.  to all the great people on Slack who take give their time to answer peoples questions.Many problems I have encountered have already been answered there.
