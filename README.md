# Milestone 4 Project
## Home Fitness

This project was designed and created by Side-On in the Software Development Diploma course, provided by the [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma-uk/). 
The site I've built is meant to represent everything I've learned throughtout the course. It takes on all four languages introduced to me:
- HTML
- CSS
- JavaScript
- Python

For this project I've also included the use of the web framework [Django](https://www.djangoproject.com/). It includes the `CRUD` (Create, Read, Update and Delete) functionality in various apps which have been created to give a real feel to the site. It includes password resets, reviews, tips to give other users on the products, order history and real confirmation emails.  

<br>

The site I designed is called `Home Fitness`. I thought of it during the lockdown period when there wasn't much else to do, other than work from home and design some homemade gym equipment. From IKEA bags filled with books to two 5ltr water bottles on the end of a broomhandle. I thought I'd try and create an ecommerce site where people could buy products for their home, but also leave homemade tips to share with each other. To try and build some sense of community between customers.

<br>

<strong>THIS IS NOT A REAL SITE.</strong> Even though it can take card details, and you get an order confirmation email sent to your email address, this will not take any payment from your card.

<br>

## Site Owner Goals

>I want to create a website where people can buy the latest fitness equipment. I'm a small start up so I don't have the largest array of products, but I hope to increase this by bringing people to buy my products. <br>
Users with accounts should be rewarded and given things which non-registered users don't have access to, such as leaving reviews or rating for the items they buy. I'm hoping this will encourage returning customers and make it easier for them to put my products as well by saving their details. I also want registered users to be able to have more than one delivery address to make it easier to switch between addresses.

## UX

## User Stories

Please head over to the testing area, it shows all of the user stories there, along with the testing carried out against each of them in order to achieve full functionality. 

[User stories and testing](testing/TESTING.md)

## Features

- Checkout - User can take everything that's in their shopping bag and look at the summary of what they've got all in one place. It'll also show the total amount of the contents. They can then make a secure payment, when they are ready to purchase. They can also edit the amount they want of each item, and also remove any items they no longer want.

- Profile page
This is where the user can look at all of their past orders. As well as look at their other addresses used when purchasing their items. 

- Shopping bag - Updated whenever a new product is selected. This appears in the top right of the screen and shows the user what's currently in the shopping bag. It also shows a small image of what the product is, and what the running total is.

- Emails - Sent whenever a new user signs up to confirm. another is sent whenever an order has been made. This is to give users a record of whatever they've previously ordered.

- Admin - section of the site where the site owner can look at users emails, addresses etc. Admin can also add remove and edit new products, including adding images.

- Navbar - Located at the top of the pages throughout the site. This had a logo to take the user back to the home page. A search bar for users to search for products by name, brand name, category and description.

- Account logo -Takes the user to their account. If they aren't signed in, the dropdown menu on the logo will give options to register or login.

- Basket - This shows the user how much is in there basket, and the total cost of what they have in there. Clicking on this shows the user the contents, and show a button to take them to the checkout to update or pay for their items.

- Fit Tips - Page for users to share any workout tips or ideas to other users. This allows a logged in user to select which item they want to leave a tip about. User must be authorised and logged in to leave a fit tip.

## Features to implement 

- Multiple addresses - Select a delivery address at the checkout and autofill. A user can have more than one delivery address. And to save them from having to enter a new one each time, this feature will save it for them for later use.

- Change password - Update the profile to allow the user to update their password.

- More in depth categorisation - Better ways of sorting products like, most expensive first, or most reviewed etc.

## Wireframes

Please head over to the [Wireframes](wireframes/wireframes.md) and design ideas.

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

Follow this [Testing documentation link](testing/TESTING.md) to go to the tests completed alongside the user stories. This is also contains the validation issues and other bugs found in the project.

## Code Used

- I implemented code from the Code Instutitue while completing the projects throughtout the course. This code was used to get the basic apps into the Home Fitness project. The main code was used around the models and JavaScript of the Stripe functionality.

## Deployment
<br>

###  Github

- I set the project up from the Code Institute template which contained a lot of features of add-ons to help with formatting and other features in the project.

- Used for version control through the commands:

```
git add .
git commit -m "commit message"
git push
```

This one done whenever new features, fixes and testing was done.

- A place to keep the project files and media files. 

<br>

### Heroku

<br>

I used Heroku to set the project up in a live environment. To this this, I took these steps: 

1. Created a free user profile on [Heroku](https://heroku.com/).
2. Created a new project name side-on-home-fitness. This created a live site for the project here: [Home Fitness](https://side-on-home-fitness.herokuapp.com/)
3. I then connected Heroku to the GitHub repository through the Deploy tab. There was a Github button on the Deploy tab page and I went through my log in details to link that to the Heroku app. I found the project I was working on and connected it and selected auto-deploy. Now everytime I pushed a change in GitHub, Heroku would redeploy with the changes made.  
4. I then created a database in the website to hold all of my data. I used the Postgres free database under the resources tab of the project page.
5. In the gitpod command interface, I installed two packages: dj_database_url and psycopg2 to connect the database to the project, by typing pip3 install 'package name'
6. As these are required, I froze them into the requirements.txt. To do this, I entered the command: `pip3 freeze > requirements.txt`.
7. I replaced the current database settings in the project level settings.py with: 
```
DATABASES = {
    'default': dj_database_url.parse('DATABASE_URL')
} 
```
<br>

I ensured that I kept from commiting and pushing this to GitHub because it contains senstive information on accessing the database. <br>
To avoid this, along with other files which contain sensitive information, I created an env.py file, and added it to the gitignore file. This stops it from being pushed to GitPod).
After the database has been created in Heroku, I needed to migrate the existing databases. To this is I used the command: `heroku python3 manage.py makemigrations --dry-run` . This command shows a glimpse of what the migrations are expected to be, and to make it isn't going to do anything weird. 
If it looks good, run the command `heroku python3 manage.py migrate`.
To create a superuser (an admin to look at all of the products, addresses etc) I ran the command: `heroku python3 manage.py createsuperuser`. Then entered an email, username and password. (Made a note of that straight away)
I used an if else statement to determine what database to use. This was:

```
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
```

8. With everything done, the Postgres database was ready to go!

<u>Gunicorn</u> 

1. This was a package needed to tell Heroku that that app is a web application.I did this by entering pip3 install Gunicorn
2. Heroku needs a Procfile to tell it how to run the app as well. I made one by created a new folder, not within any of the apps or other files on the project. (can be done by entering touch Procfile in the command line). 
3. Within the Procfile, add on the first line: `web: gunicorn (your appname) wsgi:application`.


### AWS (Amazon Web Service) for all your static and media files
1. Create a free AWS account.
2. Create a bucket, which stores media and static files
3. Name the bucket and select with region you're closest to
4. Make the bucket public by unchecking the box
5. Create the bucket
6. In the permissions tab, go to properties - static website hosting.
7. Create a new endpoint and save
8. Still inside the permissions tab, add:
```
[
  [
      {
          "AllowedHeaders": [
              "Authorization"
          ],
          "AllowedMethods": [
              "GET"
          ],
          "AllowedOrigins": [
              "*"
          ],
          "ExposedHeaders": [

          ]
      }
  ]
]
```
8. Look for the Bucket Policy, in that choose Policy Generator to create a new policy by:
    1. Selecting S3 Bucket Policy for the type
    2. Allow multiple principles by using `'*'`
    3. Action - Get Object
    4. At the top of the 'Bucket Policy Editor' tab, find the 'ARN' and paste it in
    5. Add policy > Generate policy
    6. Copy and paste the generate policy into the policy ediot on the previous page.
    7. Before you save! You'll need to add `'/*'` at the end of the Resources value.
    8. Go to Access Control List and select Everyone under Public Access

#### IAM  Management

1. Go back to the services menu.
2. Select IAM.
3. In the user groups, give the group a name (best to keep it the same as the project).
4. Go to policies.
    1. Go to the `JSON` tab and then the import manage policy area.
    2. Search for `S3` and then `S3 Full Access Policy`.
    3. Restrict the access to the bucket by replacing the Resource value the with ARN created in the previous instructions.
    4. Click `Next:Tags` and `Review Policy`.
    5. Give a name and `Create Policy`
5. To attach the newly created policy to the group, select the group name under `User Groups`.
6. Find and attach the new policy.
7. In `Users`, add a new user to the group with the same name as the project.
8. Append `-staticfiles-user` to identiy the user type.
9. Select `Programmatic Access` under `Permissions`.
10. Select the previously created group.
11. Go through the netx pages to create the user
12. On the final page, download the csv file to get the secrets keys which are required to authenticate the Django Project. <u>Keep these safe!</u>

### Connect Django to AWS bucket

1. Install two packages:

```
pip3 install boto3
pip3 install django-storages

add these to requirements
pip3 freeze > requirements.txt

```

2. In settings.py, add `'storages'` to the list of installed apps.
3. Add this to the settings.py as well:

```
if "USE_AWS" in os.environ:
      # Bucket configurations
      AWS_STORAGE_BUCKET_NAME = "<bucket name>"
      AWS_S3_REGION_NAME = "<bucket region>"
      AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID") # from the downloaded csv file
      AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY") # from the downloaded csv file
      AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

      # static and media files
      STATICFILES_STORAGE = "custom_storages.StaticStorage"
      STATICFILES_LOCATION = "static"
      DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
      MEDIAFILES_LOCATION = "media"

      STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
      MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

4. In Heroku, go to the settings tab and reveal config vars.
5. Enter the required variables.
6. In the IDE, create a new custom_storages.py file at the root level
7. Add at the top of the file:

```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
``` 

8. Add inside the file:
```
  class StaticStorage(S3Boto3Storage):
      location = settings.STATICFILES_LOCATION
  
  class MediaStorage(S3Boto3Storage):
      location = settings.MEDIAFILES_LOCATION
```
 9. Commit and push changes to GitHub.

 #### Adding files to the AWS bucket

 1. in the AWS bucket, create an images or media file where you want them to be located.
 2. Drag and drop the files into the file location.
 3. Make sure you select to grant public access before saving them.

 -----

## Acknowledgements

- I followed the Code Institutes video lessons, esepically the Boutique Ado introduction project. This was to get a basic grasp and concept of the many features of Django. It was also used to get a basic template of the overal project and a lot of the layout and apps were in line with what I wanted to achieve in this project, so I used what I need to get the foundations of the website. 

- I looked at the [Django](https://docs.djangoproject.com/en/3.2/) documentation to understand best practices when using things like models and forms.

- All of those I spoke to in the tutor help chat. Thank you so much for your patience and guidance on the issues I was having with the project. 

- The users of Slack, and those who had already asked and answered the questions I had throughout the project.

- Images taken from [Pexels](https://www.pexels.com/). Amazing site to find free to use images.

- Content and reviews written by myself, as well as the product details.