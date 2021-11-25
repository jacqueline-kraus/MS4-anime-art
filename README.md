# MS4-anime-art


# Table of contents
- [UX](#ux)
    - [Business goals](#business-goals)
    - [Customer goals](#customer-goals)
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
### Backstory:
My friend [Shippudeve](https://www.instagram.com/shippudeve/) draws amazing anime images - both classic (with pen and paper) and also digital. This e-commerce website should help her in the future to be able to sell her drawings as posters and with more features implemented, she can even draw images on request or on different materials (like shoes or shirts). To support her talent the idea of "Anime Art" came up. 

Anime Art stands for exclusive, selfmade drawings that you can purchase nowhere else. One day every anime fan (or not fan) should be able to say: "I have a drawing of [Shippudeve](https://www.instagram.com/shippudeve/), the great artist". 


## Business goals
### As a business owner:
- I want to generate revenue through offering a product that can be purchased through a webshop.
- I want the user to understand what product I am offering.
- I want to offer only exclusive products, that a user cannot purchase anywhere else.

## Customer goals
### As a user
- I want to be able to view products so that I can purchase the products I like.
- I want to be able to view the product details so that I can see the product name, product prize, product description and product image.
- I want to be able to understand what the webshop is selling so that I can evaluate if I am interested in the products.
- I want to be able to register for an user account so that I can view my profile.
- I want to be able to login and logout so that I can access my profile.
- I want to be able to reset my password so that I can access my profile in case I lost the password or secure my account by changing the password.
- I want to be able to receive an email confirmation after registering so that I can know I registered successfully.
- I want to be able to view my profile so that I can see my order history, open requests and save my information for future orders.
- I want to be able to filter products so that I can find easily the products by category.
- I want to be able to search for a product by name or description so that I can find a specific product.
- I want to be able to see what I have searched for and the number of results so that I can know if there are results.
- I want to be able to select the quantity of a product so that I can purchase a certain amount.
- I want to be able to view products in my cart so that I can always be aware of what I am about to purchase and how much it will cost.
- I want to be able to adjust the quantity of products in the cart so that I can delete or add more of the product.
- I want to be able to delete products in my cart so that I can change my mind at any given time.
- I want to be able to enter my payment information so that I can checkout quick and easy.
- I want to be able to get an order confirmation after checkout so that I can double check that my data is correct.
- I want to be able to receive an email confirmation so that I can keep track on my purchases and won't loose it.


## Structure of the website
Anime Art is a responsive e-commerce website, so it is optimized for all devices and screen sizes (desktop, mobile and tablet). It has an intuitive, user friendly interface with an easy to use navigation bar on top. From the homepage a user can choose directly which kind of products to check out and on the "about" page the user finds exlpanation about Anime Art and its products. On the products navigation menu item, a user has another way to find either all products or the products filtered by type. On the Account menu Item a user can register or login. When a user registers, a form has to be filled out and the user receives an email, which has to be confirmed before the account is created successfully. When a user is already logged in, the user has the possibility to view their profile or to logout of their account. In the last item, the shopping cart icon, the user is able to view their shopping cart, so what they are about to purchase. From the shopping cart, the user can purchase whats in the shopping cart by clicking on a button ("Go to secure checkout") and filling out a form on the checkout page. The form contains input fields for shipping/billing information and card as a payment method. On this page the user can also review what they are about to purchase (in the order summary). When actually purchasing the product and the purchase was successful, the user will land on a "thank you" page with a summary of all information (User information and information of the product that was purchased).

## Wireframes
---> Add wireframes here 

## Surface
### Fonts
- font-family: 'Cinzel', serif;
- font-family: 'Roboto', sans-serif;

### Colors
### Images




# Apps & Features
## Existing Features

## Global features
### Navigation
#### Search
### Authentication (Registration, Login, Logout, PW reset)
- django allauth for authentication (login etc.)
### Messages (django, styled with bootstrap)
### Includes


### Home app
`home`

#### About

### Products app
`products`

#### Products (List Page)
#### Product Display
#### Filter

### Profiles app
`profiles`


### Cart app
`cart`

### Checkout app
`checkout`



## Features left to implement:
- Footer with imprint, SEO Texts, Contact Us page, Newsletter Signup

# Database Schema
### Data Models
---> List all models and their name, database key,field type and type validation


# Technologies used:

## Languages:
- [Python](https://www.python.org/): logic and structure for backend
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript): to add interactivity to the frontend

- [HTML](https://en.wikipedia.org/wiki/Hypertext_Markup_Language): to structure the website
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/): templating language for python

## Database
[SQLite](https://www.sqlite.org/index.html): default database in django; used in development
[PostgreSQL](https://www.postgresql.org/): production database in heroku

## Styling:
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets): to style the HTML code
- [Bootstrap 5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/): to add responsiveness, styling and some functionality
- [Fontawesome](https://fontawesome.com/): as an icon library
- [Google Fonts](https://fonts.google.com/): as a font resource
- [Favicon](https://favicon.io/): to generate favicon

## Frameworks and libraries:
- [Django](https://www.djangoproject.com/): high-level Python web framework
- [JQuery](https://jquery.com/): as a JavaScript library

## Planning
- [Balsamiq](https://balsamiq.com/): for creating wireframes
- [Google Sheets](https://en.wikipedia.org/wiki/Google_Sheets): to write user stories and planning the data models

## Testing
- [Am I responsive?](http://ami.responsivedesign.is/): for checking responsiveness on different screen sizes and using screenshot as a showcase for this projects README.md
- [Comparium](https://front.comparium.app/livetesting): For live testing on different browsers
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools): constantly testing styling, responsiveness and functionality

## Miscellaneous:

- [Github](https://github.com/): for hosting the projects repository
- [Heroku](https://www.heroku.com/): cloud platform for deploying web app
- [Stripe](https://stripe.com/en-gb-de): to manage (test) payment transactions
- [Visual Studio Code](https://code.visualstudio.com/): as a IDE (Integrated Development Environment) for developing the project
- [Git](https://en.wikipedia.org/wiki/Git): for version control
- [Popper.js](https://getbootstrap.com/docs/5.1/getting-started/introduction/): required for using bootstrap

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

- bg for loading spinner: Image by <a href="https://pixabay.com/users/jsks-632850/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=595954">ryo taka</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=595954">Pixabay</a>


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
- https://github.com/SmileyChris/django-countries to understand django countries in iso

## Acknowledgments
- 
- 
- 


# NOTES

## Todos
### Small styling/content stuff:
- add favicon
- Add delivery fees to faq
- Highlight active the button on product page that is active
- footer is not fixed --> check how to fix for when cart is empty or how it is on XL devices
- rename button "back to overview"
- Order product list page by showing digital type first
- show total cost not always, only by hovering over
- fix navbar alignment -> when there is something in the cart, it breaks in two rows
- evtl change font size of p
- change color of account menu when logged in or show a small dot
- search: error message when no result found

- Messages
- loading overlay in checkout --> fix image
- product list: sm col 12 not 1
- write texts
- increment/decrement buttons --> right one is edgy, left is round

### Responsive adjustments
- Navbar and header image needs to be mobile adjusted

### Features missing
- django pagination (too many products on one page)
- profile/account page
- admin
- Leave out sorting for now, might add later when time left

### Other
- Finish Readme
- write down a simple marketing strategy, why some things are like they are


### Bugs / Problems that NEED to be solved
- static / images are not shown in development




### done:
- add subtotal
update subtotal when adjusting the quantity in the cart.
add subtotal to checkout
- evtl bug: look at the buttons logic before adding to cart. 
- Change home to "about us" and show on home not the whole text
- Add information like faq and delivery cost to about us page
- upload wireframes
- find solution with image problem!! Maybe aws after all?
- add stripe keys to heroku
- crispy forms in checkout
- test if webhooks are working
- social icons target blank
- checkout app / stripe payment
- alt names