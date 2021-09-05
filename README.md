# Milestone 4 Project
## Home Fitness
<br>

## Site Owner Goals

>I want to create a website where people can buy the latest fitness equipment. I'm a small start up so I don't have the largest array of products, but I hope to increase this by bringing people to buy my products. <br>
Users with accounts should be rewarded and given things which non-registered users don't have access to, such as leaving reviews or rating for the items they buy. I'm hoping this will encourage returning customers and make it easier for them to put my products as well by saving their details. I also want registered users to be able to have more than one delivery address to make it easier to switch between addresses.

## UX

## Summary 

## User Stories

- User wants to add an item in their basket and see what they've added

- User wants to see their old orders
- User wants to remove an item from their bag
- User doesn't want to have to re-enter their delivery information when placing a new order
- User wants to register for a new account
- User wants to get a record of their order
- User wants to only see products of a certain type
- User wants to sort all items by price

## Site owner features
- Owner wants to be able to create, remove, update and delete products
- Owner wants to able to look at and update user details if they needed or asked to by the user. 
- Owner wants a modile responsive design, as I know a lot of users are mobile based.
- Owner want users to be able to easily find items, and also search by price, rating and category.

<br>

## Features

- Checkout

- Profile page

- Select a delivery address at the checkout

- Autofills delivery information

- Shopping bag - Updated whenever a new product is selected

- Emails - Sent whenever a new user signs up to confirm. another is sent whenever an order has been made

- Admin - section of the site where the site owner can look at users emails, addresses etc. Admin can also add remove and edit new products, including adding images

- 

## Wireframes



<br>

## Technologies Used

- Django - Used to create seperate apps throughout the project, enabling the developer to edit and alter each feature individually. It also increasees the scalability of the project along the line. 

- Django allauth - Used to create the register and sign-in feature in the project.

- Django Countries - Used to allow users to select a full list of countries.

- Django Crispy Forms - Used to generate and style forms.

- Stripe - Used to create and enable the payment feature.

- Python - Used create functions allowing the use of linking to mongoDB.

- HTML5 - Markup language used to display files in a browser.

- CSS3 - Used for styling purposes, allowing consistency across the website.

- JQuery - Used with Materialize to create basic responsive elements within the website.

- Bootstrap - Used for the basic CSS layouts, as well as basic forms and navigator bar.

- Balsamiq - To create wireframes at the initial design stage of the project.

- Font-awesome - Used for the icons shown against some of the fields in the website.

- Google-fonts - For the fonts used in the website content.

- GitHub - Used for version control, storing the code used for the website and to enable editing/deleting.

- Heroku - Used to deplay a live version of the site.

- Gunicorn - Used to connect the project with Heroku.

- Amazon Web Service (AWS) - used to store images and static files for the website.

## Testing

Follow this link to go to the test completed completed alongside the user stories.

## Code Used

- I implemented code from the Code Instutitue while completing the projects throughtout the course. This code was used to get the basic apps into the Home Fitness project. The main code was used around the models and JavaScript of the Stripe functionality.

## Deployment
<br>

###  Github
- I set the project up from the Code Institute template which contained a lot of features of add-ons to help with formatting and other features in the project.

- Used for version control through the commands:

    git add .<br>
    git commit -m "<i>commit message</i>" <br>
    git push

    This one done whenever new features, fixes and testing was done.

- A place to keep the project files and media files. 

<br>

### Heroku

<br>

I used Heroku to set the project up in a live environment. To this this, I took these steps: 

- Created a free user profile on [Heroku](https://heroku.com/).
- Created a new project name side-on-home-fitness. This created a live site for the project here: [Home Fitness](https://side-on-home-fitness.herokuapp.com/)
- I then connected Heroku to the GitHub repository through the Deploy tab. There was a Github button on the Deploy tab page and I went through my log in details to link that to the Heroku app. I found the project I was working on and connected it and selected auto-deploy. Now everytime I pushed a change in GitHub, Heroku would redeploy with the changes made.  
- I then created a database in the website to hold all of my data. I used the Postgres free database under the resources tab of the project page.
- In the gitpod command interface, I installed two packages: dj_database_url and psycopg2 to connect the database to the project, by typing pip3 install .....
- As these are required, I froze them into the requirements.txt. To do this, I entered the command: pip3 freeze > requirements.txt.
- I replaced the current database settings in the project level settings.py with: DATABASES = {
    'default': dj_database_url.parse('DATABASE_URL')
} 
<br>
I ensured that I kept from commiting and pushing this to GitHub because it contains senstive information on accessing the database. <br>
To avoid this, along with other files which contain sensitive information, I created an env.py file, and added it to the gitignore file. This stops it from being pushed to GitPod).
- After the database has been created in Heroku, I needed to migrate the existing databases. To this is I used the command: heroku python3 manage.py makemigrations --dry-run. This command shows a glimpse of what the migrations are expected to be, and to make it isn't going to do anything weird. 
- If it looks good, run the command heroku python3 manage.py migrate.
- To create a superuser (an admin to look at all of the products, addresses etc) I ran the command: heroku python3 manage.py createsuperuser. Then entered an email, username and password. (Made a note of that straight away)
- I used an if else statement to determine what database to use. This was:
    if "DATABASE_URL" in os.environ:
            DATABASES = {
                "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
    else:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
- With everything done, the Postgres database was ready to go!

- <u>Gunicorn</u> 
- This was a package needed to tell Heroku that that app is a web application.I did this by entering pip3 install Gunicorn
- Heroku needs a Procfile to tell it how to run the app as well. I made one by created a new folder, not within any of the apps or other files on the project. (can be done by entering touch Procfile in the command line). 
- Within the Procfile, I added on the first line: web: gunicorn (your appname) wsgi:application.
- 


-----

## Acknowledgements

- I followed the Code Institutes video lessons, esepically the Boutique Ado introduction project. This was to get a basic grasp and concept of the many features of Django. It was also used to get a basic template of the overal project and a lot of the layout and apps were in line with what I wanted to achieve in this project, so I used 

- I looked at the Django documentation to understand best practices when using things like models and forms.

- All of those I spoke to in the tutor help chat. 

- The users of Slack, and those who had already asked and answered the questions I had throughout the project.

