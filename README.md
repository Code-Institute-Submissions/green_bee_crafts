# Green Bee Crafts
![Mock-up of site](media/images/???)
## Goal for this Project
To create a functioning e-commerce site to present to a client.
The client is a sole trader who upcyles fabrics, pots and furniture in an ethical manner and sells them at craft fairs and online.
Currently online sales are low as the client has no website of their own and sells via ebay and facebook but with a dedicated website hopes to reduce costs and increase sales.

---
## Table of contents 
* [UX](#ux)
    * [Site Owners Goals](#site-owners-goals)
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
    * [Design Choices](#design-choices)
* [Wireframes](#wireframes)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Technologies used](#technologies-used)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)
---

## UX Design

### Site Owners Goals

The owner of the site is a small business and whants in increase sales and awareness of her products and hopes that a dedicated website will help drive sales and increase customer engagement.

[Back to Top](#table-of-contents)

### User Goals

Users want to be able to easily navigate and buy products from Green Bee and find out when and where the next face to face markets will be. As well as any new products and business updates.

[Back to Top](#table-of-contents)

### User Stories

* As a user I want to be able to easily navigate the site.
* As a user I want to be able to easily find the products I am looking for.
* As a user I want to be able to buy directly from the site.
* As a user I want to find out when the next face to face market is.
* As a user I want to learn more about the details of the products and what they are made from or how they were sourced.
* As a user I want to 
 
[Back to Top](#table-of-contents)
### User Requirements and Expectations
### Requirements
* Clear easy navigation for users
* The ability to buy products directly from the site
* Ability to search for products
* A section with infromation about the company.

### Expectations

* Cutomers should be able to browse products
* Customers should be able to payfor and buy products directly from the website.
* Company history available for users to read. 


[Back to Top](#table-of-contents)
## Design Choices
### Colors
![colour palette](wireframes/)
After discussion with the business owner we decided upon a colour scheme combining natural colours and soft pastels to compliment her current branding.

#006D77 will be used as the main background colour
#FFDDD2 will be used as on overlay on products and bag pages
#83C5BE will be used for the buttons
#EDF6F9 will be used for button text and borders
#A26769 will be used for the navbar to help navigation stand out

### Fonts

I chose to use google fonts for this projects and decided to use Mukta as the main text font as well as Courgette for the Title font.

[Back to Top](#table-of-contents)

## Wireframes
I decided to use [Balsamiq](https://balsamiq.com/) to make the wireframes, theay can be viewed below.
## Desktop Wireframes


## Tablet Wireframes



## Mobile Wireframes



## Database


[Back to Top](#table-of-contents)
## Features
### Existing Features
* Users can browse products by price, category as well as find more specific details on products that they are
interested in.
* Users can build a basket of products to order.
* Users can sign in a nd register for an account with django allauth.
* Users can find information on upcomimg markets where they can buy products face to face.

[Back to Top](#table-of-contents)
### Features to be implemented 
* Blog section to be added for greater customer interaction and engagement.


[Back to Top](#table-of-contents)

## Technologies Used

### Languages

* HTML
* CSS
* JavaScript
* jQuery
* Python

### Libraries and Frameworks

* Django
* Bootstrap

### Tools

* Git
* Gitpod
* Heroku
* Balsamiq
* W3C HTML Validataion Service
* W3C CSS Validation Service


[Back to Top](#table-of-contents)

## Testing

[Back to Top](#table-of-contents)
## Bugs

[Bug fixes](bugs.md)

[Back to Top](#table-of-contents)
## Deployment
### Local Deployment

I have created the project using Github, from there I used [Gitpod](https://gitpod.io/) to write my code. 
Then I used commits to git followed by "git push" to my GitHub repository. 
I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku. 

For this project you need to create an account on Stripe for the reservation module as well as an account on AWS in order to store your static and media files.

This project can be ran locally by following the following steps: 
I used Gitpod for development, so the following steps will be specific to Gitpod. 
You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

To clone the project: 

1. From the application's repository, click the "code" button and download the zip of the repository.
    Alternatively, you can clone the repository using the following line in your terminal:

    ``` 
    git clone https://github.com/Spannakin/green_bee_crafts.git
    ``` 

1. Access the folder in your terminal window and install the application's [link to required modules](https://github.com/Spannakin/Green_Bee_Crafts/blob/master/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

1. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It will need to contain the following lines and variables:
    ```
    import os

    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEVELOPMENT"] = "True"

    os.environ["DEFAULT_FROM_EMAIL"] = 'DEFAULT_FROM_EMAIL'

    os.environ["STRIPE_PUBLIC_KEY"] = "STRIPE_PUBLIC_KEY"
    os.environ["STRIPE_SECRET_KEY"] = "STRIPE_SECRET_KEY"
    os.environ["STRIPE_WH_SECRET"] = "STRIPE_WH_SECRET"
    os.environ["STRIPE_CURRENCY"] = "EUR"

    ```
    
    If you're not sure how to get the above Stripe variables, please visit the [Stripe Documentation](https://stripe.com/docs)

    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.

1. Migrate the database models with the following command
    ```
    python3 manage.py migrate
    ```
1. Create a superuser and set up the credentials with the following command
    ```
    python3 manage.py createsuperuser
    ```
1. Run the app with the following command
    ```
    python manage.py runserver
    ```
    The address to access the website is displayed in the terminal  
    Add /admin to the end to access the admin panel with your superuser credentials

    
### Heroku Deployment 

1. Login to your Heroku account and create a new app. Choose your region. 
1. Once the app is created click on the resources button and under Add-ons, look for the Heroku Postgres to attach a postgres database to your project.
    Select the Hobby Dev - Free plan and click 'Submit order form'

1. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py ():
    !You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website. 

    ```
    AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
    AWS_S3_REGION_NAME = "AWS_S3_REGION_NAME"
    AWS_STORAGE_BUCKET_NAME = "AWS_STORAGE_BUCKET_NAME"
    USE_AWS = True
    
    DATABASE_URL = "This variable is automatically set when adding the Postgres Add on"

    SECRET_KEY = "SECRET_KEY"

    STRIPE_PUBLIC_KEY = "STRIPE_PUBLIC_KEY"
    STRIPE_SECRET_KEY = "STRIPE_SECRET_KEY"
    STRIPE_WH_SECRET = "STRIPE_WH_SECRET"
    STRIPE_CURRENCY = EUR

    DEFAULT_FROM_EMAIL = "DEFAULT_FROM_EMAIL"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_PASS = "EMAIL_HOST_PASS"
    EMAIL_HOST_USER = "EMAIL_HOST_USER"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    ```
1. From this screen, copy the value of DATABASE_URL
1. After this go to your settings.py in the green_bee_crafts directory and comment out the default database configuration and add:
    ```
    DATABASES = {
        'default': dj_database_url.parse('Put your DATABASE_URL here'))
    }
    ```
1. Migrate again with the following command
    ```
    python3 manage.py migrate
    ```


1. Create a superuser for the postgres database so you can have access to the django admin by setting up the credentials with the following command
    ```
    python3 manage.py createsuperuser
    ```

    --> Don't forget to login to the admin page and check the boxes 'Verified and primary"

1. Load the data into your newly created database by using the following command: 

    ```
    python3 manage.py loaddata <name of file containing the data *>
    ``` 

    * categories.json
    * products.json
    * markets.json
    * 

1. After migrations are complete, change database configurations to:
```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
```
This set up will allow your site to use Postgres in deployment and sqlite3 in development.


1. Make sure you have your requirements.txt file and your Procfile. In case you don't, follow the below steps:
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
1. The Procfile should contain the following line:
    ```
    web: gunicorn <project_name>.wsgi:application

    ```

1. Add your files and commit them to GITHUB by running the following commands:
    ```
    git add . 
    git commit -m "Your commit message"
    git push
    ```

1. Add your Heroku app URL to ALLOWED_HOSTS in your settings.py file
1. Disable collect static so that Heroku doesn't try to collect static files when you deploy by typing the following command in the terminal
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1
    ```
1. Go back to HEROKU and click "Deploy" in the navigation. 
1. Scroll down to Deployment method and Select Github. 
1. Look for your repository and click connect. 
1. Under automatic deploys, click 'Enable automatic deploys'

1. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes. 


1. Store your static files and media files on AWS. You can find more information about this on [Amazon S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
    If you would like to follow a tutorial instead, visit [this tutorial on Youtube from Amazon Web Services](https://youtube.com/watch?v=e6w9LwZJFIA)

1. Set up email service to send confirmation email and user verification email to the users. You can do this by following the next steps (Gmail only)

(Be aware that this migth be different for other providers or the process might have changed over time)

* Go to your email account and go to your account settings
* Under Security, scroll down to Signing in to Google and make sure 2 step verification is turned on
* Under the same heading (Signing in to Google) you will see the 'App passwords' option.
* Click on the option, select mail for the app and under device type select other and fill in 'Django'
* You will now get a password which you should copy and set it as a config variable in Heroku:

```
    EMAIL_HOST_PASS = 'Password you just copied'
    EMAIL_HOST_USER = 'Your gmail account
```
* Go to your settings.py in casa_pedra_nobre directory and add the following:

```
    if "DEVELOPMENT" in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
```

[Back to Top](#table-of-contents)
## Credits


[Back to Top](#table-of-contents)
