# MS4-anime-art


# Table of contents
- [UX](#ux)
    - [Website owner business goals](#website-owner-business-goals)
    - [User goals](#user-goals)
    - [User stories](#user-stories)
    - [Structure of the website](#structure-of-the-website)
    - [Wireframes](#wireframes)
    - [Surface](#surface)
- [Database Schema](#database-schema)
- [Features](#features)
    - [Existing features](#existing-features)
    - [Features left to implement](#features-left-to-implement)
- [Technologies used](#technologies-used)
- [Code Validation](#code-validation)
- [Database](#database)
- [Deployment](#deployment)
- [Credits](#credits)


#  UX 

## Website owner business goals

## User goals
### Unregistered user
### Registered user

## User stories
### As a business owner:
### As a user

## Structure of the website

## Wireframes

## Surface
### Fonts
- font-family: 'Cinzel', serif;
- font-family: 'Roboto', sans-serif;

### Colors
### Images


# Database Schema

# Features
## Existing Features

### Navigation
#### Search

### Home

### Authentication (Registration, Login, Logout, PW reset)
- django allauth for authentication (login etc.)

### Product List Page
#### Filter

### Product Display Page

### Account

### Cart

### Checkout

### Messages (django, styled with bootstrap)

### Includes

## Features left to implement:


# Technologies used:

## Languages:
- [Python](https://www.python.org/): 
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript): 

- [HTML](https://en.wikipedia.org/wiki/Hypertext_Markup_Language): for structuring the website

## For styling:
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets): to write custom style for the HTML code
- [Bootstrap 5.1](): for responsiveness, styling and some functionality
- [Fontawesome](https://fontawesome.com/): as an icon library
- [Google Fonts](https://fonts.google.com/): as a font resource
- [Favicon](https://favicon.io/): to generate favicon

## Frameworks and libraries:
- [Django](): as a framework for Python
- [JQuery](https://jquery.com/): as a JavaScript library

## Planning
- [Balsamiq](https://balsamiq.com/): for creating wireframes

## Testing
- 

## Miscellaneous:
- [Github](https://github.com/): for hosting the projects repository
- [Heroku](): for deploying the website
- [Postgres]():
- [Visual Studio Code](https://code.visualstudio.com/): as a IDE (Integrated Development Environment) for developing the project
- [Git](https://en.wikipedia.org/wiki/Git): for version control

## Code Validation Tools
- [PEP8 checker](http://pep8online.com/): to validate Python code
- [JShint](https://jshint.com/) to validate JavaScript code
- [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code
- [W3 HTML Validator](https://validator.w3.org/) to validate HTML code

# Code validation
- [PEP8 checker](http://pep8online.com/): 
- [JShint](https://jshint.com/): 
- [W3 CSS Validator](https://jigsaw.w3.org/css-validator/): 
- [W3 HTML Validator](https://validator.w3.org/): 


# Database
## Postgres


# Deployment

To run this project, you have to install:
- [Django](): to use as a framework
- [Python3](): to run the app
- [PIP](): to install all app requirements
- Any [IDE]() (e.g. [Visual Studio Code]()) or if you want to work virtually e.g. [Gitpod]()
- [GIT](): for cloning and version control

- Heroku & Postgres

If you use Visual Studio Code:
how to run
- python3 -m venv .venv  
- source .venv/bin/activate

how to stop
- deactivate

## [Local deployment](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
1. Go to repository
2. Click on the button "code"
3. Select the "HTTPS" option.
4. Copy the URL presented
5. Open your Terminal
6. Create a directory for storing this repository
7. Type `git clone https://github.com/jacqueline-kraus/MS4-anime-art`
8. Press enter to create local clone repository

## Heroku Deployment
1. 
2. 
3. 



# Credits

## Images
- Page header image for home page taken from [Pixabay](https://pixabay.com/illustrations/naruto-eyes-anime-cartoon-japan-5823848/)
- Product images created by [Shippudeve](https://www.instagram.com/shippudeve/)


## Problem solving helpers
- [Django documentation]()
- [Bootstrap documentation]()
- [w3schools.com](https://www.w3schools.com/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn)
- [stackoverflow](https://stackoverflow.com/)
- [Python documentation](https://docs.python.org/3/)


## Code
- Bootstrap
- [Google Fonts](https://fonts.google.com/): for the fonts used
- [Fontawesome](https://fontawesome.com/): for the icons
- [Understanding messages and how to use them in Django with bootstrap](https://www.ordinarycoders.com/blog/article/django-messages-framework)
- django allauth for authentication (login etc.)
- Hover effect copied from Hover.css (https://github.com/IanLunn/Hover/blob/master/css/hover.css)
- https://stackoverflow.com/questions/39031224/how-to-center-cards-in-bootstrap-4
--> to align the product cards in center


## Acknowledgments
- 
- 
- 


# NOTES

- Navbar and header image needs to be mobile adjusted
- For later: Order product list page by showing digital type first
- Leave out sorting for now, might add later when time left.
- Highlight active the button on product page that is active.
- add favicon
- Add delivery fees to faq
- Change home to "about us" and show on home not the whole text
- Add information like faq and delivery cost to about us page
- footer is not fixed --> check how to fix for when cart is empty or how it is on XL devices
- upload wireframes
- rename button "back to overview"
- find solution with image problem!!
- fix navbar alignment -> when there is something in the cart, it breaks in two rows
- django pagination (too many products on one page)
- checkout app / stripe payment
- profile/account page
- admin
- show total cost not always, only by hovering over.
- write down a simple marketing strategy, why some things are like they are