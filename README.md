# MS4-anime-art

Anime Art is an online shop for buying authentic, unique drawings from a real artist, who is specialized in drawing animes.

![showcase](readme-files/showcase/showcase.png)

# Table of contents
- [UX](#ux)
    - [Business goals](#business-goals)
    - [Customer goals](#customer-goals)
    - [Structure of the website](#structure-of-the-website)
    - [Wireframes](#wireframes)
    - [Surface](#surface)
- [Apps and Features](#apps-and-features)
    - [Global features](#global-features)
    - [Apps](#apps)
    - [Features left to implement](#features-left-to-implement)
- [Database Schema](#database-schema)
- [Technologies used](#technologies-used)
- [Database](#database)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

#  UX 
### Backstory:
My friend [Shippudeve](https://www.instagram.com/shippudeve/) draws amazing anime images - both **classic (with pen and paper) and also digital**. This e-commerce website should help her to sell her drawings as posters. To support her talent the idea of "Anime Art" came up. 

**Anime Art stands for exclusive, self-made drawings that you can purchase nowhere else.** One day every anime fan (or not a fan) should be able to say: "I have a drawing of [Shippudeve](https://www.instagram.com/shippudeve/), the great artist". 


## Business goals
### As a business owner:
- I want to generate revenue by offering a product that can be purchased through a webshop.
- I want the user to understand what product I am offering.
- I want to offer only exclusive products, that a user cannot purchase anywhere else.
- I want to be able to add a product so that I can add new products to the shop.
- I want to be able to edit a product so that I can update product information.
- I want to be able to delete a product so that I can remove products from the shop.

## Customer goals
### As a user
- I want to be able to view products so that I can purchase the products I like.
- I want to be able to view the product details so that I can see the product name, product price, product description, and product image.
- I want to be able to understand what the webshop is selling so that I can evaluate if I am interested in the products.
- I want to be able to register for a user account so that I can view my profile.
- I want to be able to login and logout so that I can access my profile.
- I want to be able to reset my password so that I can access my profile in case I lost the password or secure my account by changing the password.
- I want to be able to receive an email confirmation after registering so that I can know I registered successfully.
- I want to be able to view my profile so that I can see my order history and save my information for future orders.
- I want to be able to filter products so that I can find easily the products by category.
- I want to be able to search for a product by name or description so that I can find a specific product.
- I want to be able to see what I have searched for and the number of results so that I can know if there are results.
- I want to be able to select the quantity of a product so that I can purchase a certain amount.
- I want to be able to view products in my cart so that I can always be aware of what I am about to purchase and how much it will cost.
- I want to be able to adjust the quantity of products in the cart so that I can delete or add more of the product.
- I want to be able to delete products in my cart so that I can change my mind at any given time.
- I want to be able to enter my payment information so that I can check out quickly and easily.
- I want to be able to get an order confirmation after checkout so that I can double-check that my data is correct.
- I want to be able to receive an email confirmation so that I can keep track of my purchases and won't lose it.


## Structure of the website
Anime Art is a responsive e-commerce website, so it is optimized for **all devices and screen sizes (desktop, mobile, and tablet)**.

It has an intuitive, user-friendly interface with an easy to use **navigation bar** on top. From the **homepage** a user can choose directly which kind of products to check out and on the **about** page, the user finds an explanation about Anime Art and its products. On the products navigation menu item, a user has another way to find either all products or the products filtered by type.

On the **account** menu item a user can **register or login**. When a user registers, a form has to be filled out and the user receives an email, which has to be confirmed before the account is created successfully. When a user is already logged in, the user has the possibility to view their **profile** or to **logout** of their account.

When clicking on the shopping cart icon, the user is able to **view their shopping cart**, so what they are about to purchase. From the shopping cart, the user can purchase what is in the shopping cart by clicking on a button ("go to secure checkout") and filling out a form on the **checkout page**. The form contains input fields for shipping/billing information and card as a payment method. On this page, the user can also review what they are about to purchase (in the order summary).

When actually purchasing the product and the purchase was successful, the user will land on a "thank you" page with a summary of all information (user information and information of the product that was purchased).

## Wireframes
Wireframes can be found here: [WIREFRAMES](readme-files/wireframes/anime-art-wireframes.pdf)

## Surface
### Fonts
- Headlines (h1-h6) and buttons: [`Cinzel`](https://fonts.google.com/specimen/Cinzel)
- All other elements (like paragraphs, links, etc.): [`Roboto`](https://fonts.google.com/specimen/Roboto)

### Colors
- Primary background-color: `#fbf9f9`

- Secondary background-color: `#e0cccc`

- Main font color: `#000000`

- Borders, texts, icons: `#650000`

Buttons:

- Red: border and text `#650000` | background `#e0cccc`

- Green: border and text `#3d4343` | background `#cce0e0`

### Effects
- All buttons have a hover grow effect

### Images
- Product images created by [Shippudeve](https://www.instagram.com/shippudeve/)
- Heroimage from [Pixabay.com](https://pixabay.com/de/illustrations/naruto-ninja-maske-charakter-5752319/)
- Loading Spinner from [Pixabay.com](https://pixabay.com/de/illustrations/moe-frau-m%c3%a4dchen-manga-anime-595954/)
- Image "Image coming soon" from [Freeiconspng.com](https://www.freeiconspng.com/downloadimg/23499)
- Favicon from [Softicons.com](https://www.softicons.com/culture-icons/sharingan-icons-1.5-by-harenome-razanajato/kakashi-icon)

# Apps and Features

## Global features
### Navigation
- The Logo "Anime Art", brings the user always to the homepage

- The website has a Bootstrap5 **Offcanvas** side navigation. It is functional and adjusted for every screensize.

![side-navigation](readme-files/features/side-navigation.png)

![navigation](readme-files/features/navigation.png)

The different navigation items:
- The shopping cart: The total price is shown next to the shopping cart icon, when a user adds something to the cart

![navigation-cart](readme-files/features/navigation-cart.png)

- Products: The user can open a dropdown item to see and select the different types of products

- The options are "All Products", "Digital Drawings" or "Classic Drawings"

![navigation-products](readme-files/features/navigation-products.png)

- Account: Via the account dropdown menu, a user can register or login (when logged out) **or** view the profile or logout (when logged in)

![navigation-account-logged-out](readme-files/features/navigation-account-logged-out.png)

![navigation-logged-in](readme-files/features/navigation-logged-in.png)

- Admin: When a user has admin rights (is a superuser), the user can add products. The option for this is shown by clicking on the dropdown item "Admin". As in the future, there should be more items related to admin, this is a dropdown as well.

![navigation-admin](readme-files/features/navigation-admin.png)

- About us: This item is not a dropdown. By clicking on this item, the user will land on the "about us" page

- When a user opens a dropdown item and then clicks on another one, the previous dropdown closes by itself

- In the navigation is also included the search field

#### Search
- The search field is included in the navigation `offcanvas`

![navigation-search](readme-files/features/navigation-search.png)

- When clicking on the search button without typing search input, the field will throw an error

![search-input-error](readme-files/features/search-input-error.png)

- The search field queries in all product names and product descriptions to find a match

- It brings the user to the product list page, where will be all products shown that match the search criteria

- When there is no match, the user lands on the product list page and sees an error message

![search-error-message](readme-files/features/search-error-message.png)

### Authentication (django-allauth feature)
- `Django-allauth` is a Python package

- "Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication." ([`django allauth` documenation](https://django-allauth.readthedocs.io/en/latest/))

- It provides a set of features such as signup, login, logout, and password change

- After signing up, a verification e-mail is sent to the registered e-mail to confirm it

- Once confirmed, the user can log in with their credentials and access the profiles app

- The links to these features can be found in the navigation, under the "Account" dropdown menu

- Screenshots of the flow:

![auth-sign-up](readme-files/features/auth-sign-up.png)

![auth-verify-email](readme-files/features/auth-verify-email.png)

![email-auth-conf](readme-files/features/email-auth-conf.png)

![auth-conf-email](readme-files/features/auth-conf-email.png)

![auth-sign-in](readme-files/features/auth-sign-in.png)

![auth-sign-out](readme-files/features/auth-sign-out.png)

### Messages (django, styled with bootstrap alerts)
- There are many ways what message a user might receive throughout the website

- The messages are Bootstrap5 alerts

- Here are some examples:

![messages-sign-out](readme-files/features/messages-sign-out.png)

![messages-sign-up-conf-email](readme-files/features/messages-sign-up-conf-email.png)

![messages-email-conf-success](readme-files/features/messages-email-conf-success.png)

![messages-sign-in-successful](readme-files/features/messages-sign-in-successful.png)

![messages-item-add-cart](readme-files/features/messages-item-add-cart.png)

![messages-item-removed-cart](readme-files/features/messages-item-removed-cart.png)

![messages-order-successful](readme-files/features/messages-order-successful.png)

![messages-profile-updated-successful](readme-files/features/messages-profile-updated-successful.png)

### Back to top button
- On every page, there is a **back to top button**, that the user can click to have an easy way to go to the top of the page without scrolling

![back-to-top-btn-desktop](readme-files/features/back-to-top-btn-desktop.png)

![back-to-top-btn-mobile](readme-files/features/back-to-top-btn-mobile.png)

### Automatic emails
- A Gmail account **animeartonlineshop@gmail.com** has been created specifically for this project and used as a sender for all verification, reset, and confirmation e-mails.
- Users receive for instance an **order confirmation e-mail** after a purchase, **account verification e-mail** after the registration, **password reset e-mail** after requesting a password reset, etc.

## Apps
Anime Art is a [django project](https://docs.djangoproject.com/en/3.1/ref/applications/), which consists of 5 applications:

- `home`
- `products`
- `cart`
- `checkout`
- `profiles`

Some features are available across the Django project, while others are tied to a specific Django application. The following lists explains every app and feature in detail.

### Home app
- `home` django app includes two pages `home` page and `about` page

#### Home
- On the `home` page the user will be welcomed and can read a short introduction to the Anime Art Onlineshop. The user can also start looking for products by clicking on one of the three prominent CTAs

![homepage-desktop](readme-files/features/homepage-desktop.png)

![homepage-mobile](readme-files/features/homepage-mobile.png)

#### About
- The `about` page is informative. The user can read here about why Anime Art was founded, about the products it offers, and about the artist, who creates the products. Also, the user can find a small FAQ on this page

![about-desktop](readme-files/features/about-desktop.png)

![about-mobile](readme-files/features/about-mobile.png)

### Products app
#### `products`
- The `products` app has 4 different pages: `products`, `product_display`, `add_product` and `update_product`

#### `products` (-list)
- On the products(-list) the user can see a list of all products available in the shop

![product-list](readme-files/features/products/product-list.png)

![product-list-mobile](readme-files/features/products/product-list-mobile.png)

- the user can see product cards that contain: an image, the product name, the product price and by clicking on the image, the user can view the details of the product (`product_display`)

![product-card](readme-files/features/products/product-card.png)

![product-card-mobile](readme-files/features/products/product-card-mobile.png)

- the user can `filter` by clicking on different types of products via the buttons on top of the page

![product-filter](readme-files/features/products/product-filter.png)

![product-filter-mobile](readme-files/features/products/product-filter-mobile.png)

#### `product_display`
- On the product_display page the user can view more details about the product: **product image, product name, product description and product price**

![product-display-details](readme-files/features/products/product-display-details.png)

![product-display-details-mobile](readme-files/features/products/product-display-details-mobile.png)

- The user can also adjust the quanity of products that should be added to the cart

![product-display-quantity](readme-files/features/products/product-display-quantity.png)

![product-display-quantity-mobile](readme-files/features/products/product-display-quantity-mobile.png)

- The user can add the product to the shopping cart. When an item is added to the cart, the user will be redirected back to the `product_display`page

![product-display-add-to-cart](readme-files/features/products/product-display-add-to-cart.png)

![product-display-add-to-cart-mobile](readme-files/features/products/product-display-add-to-cart-mobile.png)

- The user can go directly from the `product_display`page to the shopping cart

![product-display-go-to-cart](readme-files/features/products/product-display-go-to-cart.png)

![product-display-go-to-cart-mobile](readme-files/features/products/product-display-go-to-cart-mobile.png)

- If the user wants to keep shopping and viewing other product, by clicking on the button at the bottom of the page, the user will be redirected to the `product`(-list)

![product-display-back](readme-files/features/products/product-display-back.png)

![product-display-back-mobile](readme-files/features/products/product-display-back-mobile.png)


### Product Admin
- When a user is an admin user ([django superuser](https://docs.djangoproject.com/en/1.8/intro/tutorial02/)) and the user is logged in, it will be visible the menu item **Admin** on the navigation (explained in the section [Navigation](#navigation)). Here a user can go to the `add_product` page and add a new product by filling out a form

#### `add_product`
- The admin user can fill out the form to create a new product

- The image field is diabled, as images cannot be uploaded here directly. They have to be hosted on a cloud service like [AWS](https://aws.amazon.com/). The user sees a warning under the image field that explains that uploading an image directly is not possible

- When adding a product, the image will be by default a "Image coming soon" image

![admin-add-product](readme-files/features/admin/admin-add-product.png)

![admin-add-product-mobile](readme-files/features/admin/admin-add-product-mobile.png)

- The added product will be shown in the `products`(list) page

![admin-added-product](readme-files/features/admin/admin-added-product.png)

![admin-added-product-mobile](readme-files/features/admin/admin-added-product-mobile.png)

- And when clicking on the image, you can see the product details on the `product_display` page

![admin-product-display](readme-files/features/admin/admin-product-display.png)

#### `update_product`
- The admin user can also update existing products

- By clicking on the `edit` button either on the `product`(list) page or on the `product_display` page

![admin-update-product](readme-files/features/admin/admin-update-product.png)
![admin-update-product-mobile](readme-files/features/admin/admin-update-product-mobile.png)

![admin-product-update](readme-files/features/admin/admin-update-product.png)

- The `update_product` page contains already the existing data in the form fields, that can now be adjusted. Just like in `add_product`, it is not possible to upload and therefore to change an image

![admin-update-product-page](readme-files/features/admin/admin-update-product-page.png)
![admin-update-product-page-mobile](readme-files/features/admin/admin-update-product-page-mobile.png)

#### `delete`
- The admin user can delete a product. When viewing the `product_display` page, next to the `edit` button is a `delete` button

- This button should only be clicked, when it is absolutely sure that a user wants to delete the product. There is no security layer yet, so when hitting this button, the product will be deleted immediately. This will be fixed in the future 

![admin-product-delete](readme-files/features/admin/admin-product-delete.png)
![admin-product-delete-mobile](readme-files/features/admin/admin-product-delete-mobile.png)

### Cart app
`cart`
- The shopping cart can be found either when clicking on **Go to cart** on the `product_display` page or via the **navigation icon**

![cart-location](readme-files/features/cart/cart-location.png)

- When the cart is empty, it can still be accessed, but it will throw an error message and a button that leads back to the `products`(-list)

![cart-empty](readme-files/features/cart/cart-empty.png)

![cart-empty-mobile](readme-files/features/cart/cart-empty-mobile.png)

- When there are items in the cart, these details will be displayed: `product image`, `product name`, `product SKU, `product price`, `quantity`, `subtotal`, `cart total`, `delivery cost` and `grand total`

- When clicking on the `product image`, the user will be redirected to the `product_display` page, where again the details can be viewed

![cart-details](readme-files/features/cart/cart-details.png)

![cart-details-mobile](readme-files/features/cart/cart-details-mobile.png)

- The quantity can also be adjusted here in the cart
- The subtotal changes, when the quantity changes (price * quantity)

![cart-quantity-subtotal](readme-files/features/cart/cart-quantity-subtotal.png)

![cart-quantity-subtotal-mobile](readme-files/features/cart/cart-quantity-subtotal-mobile.png)

- The user can also delete completely the product from the shopping cart

![cart-delete](readme-files/features/cart/cart-delete.png)

![cart-delete-mobile](readme-files/features/cart/cart-delete-mobile.png)

- The user has the possibility to go back to the `product`(-list) by clicking on the button "to product overview"

![cart-back](readme-files/features/cart/cart-back.png)

![cart-back-mobile](readme-files/features/cart/cart-back-mobile.png)

- Finally the user can see in the shopping cart the `cart total`(sum of subtotal of all items in cart ), the `delivery cost`(fixed price) and the `grand total`(sum of cart total and delivery cost) and has the possibility to purchase the products in the shopping cart by clicking on the button "go to secure checkout", which brings the user to the `checkout` page

![cart-checkout](readme-files/features/cart/cart-checkout.png)

![cart-checkout-mobile](readme-files/features/cart/cart-checkout-mobile.png)


### Checkout app
`checkout`
- The `checkout` app serves the purpose of giving the user
    - A form for the user to insert the shipping information
    - A order summary of what the user is about to purchase
    - A way to pay for the product(s)

![checkout-overview](readme-files/features/checkout/checkout-overview.png)

![checkout-overview-mobile](readme-files/features/checkout/checkout-overview-mobile.png)

- In the order summary the user can see the `quantity` of the product(s) to be purchased, the `products name` and the `price` per unit
- The user also finds the `cart total`, the `delivery cost` and the `grand total`, so what has to be paid in the end

![checkout-order-summary](readme-files/features/checkout/checkout-order-summary.png)

![checkout-order-summary-mobile](readme-files/features/checkout/checkout-order-summary-mobile.png)

- The shipping information is built with [django crispy](https://django-crispy-forms.readthedocs.io/en/latest/) forms and gives the user feedback when the input is not correct

- The `select country` field is a dropdown menu, where the user can choose the country from

- Both registered and anonymous users can purchase products at Anime Art

- When a user is not registered or logged in yet, the user will see a note under the shipping form that leads to either the sign up or the sign in page

![checkout-info-logged-out](readme-files/features/checkout/checkout-info-logged-out.png)

![checkout-info-logged-out-mobile](readme-files/features/checkout/checkout-info-logged-out-mobile.png)

- When a user is logged in, there will be a note under the form which lets the user save their information to the profile

- When a user already has a profile or did a former purchase and saved the information the form on the `checkout` page will be populated automatically with the users information (except for the `first name` and `last name`)

![checkout-info-logged-in](readme-files/features/checkout/checkout-info-logged-in.png)

![checkout-info-logged-in-mobile](readme-files/features/checkout/checkout-info-logged-in-mobile.png)

- To be able to purchase what's in the cart, the user has to fill in their card payment details

- At this stage of production cart payment is the only payment method possible

- **Payments** are handled through `stripe`. A test purchase can be made with the following details:
    - **credit card:** 4242 4242 4242 4242
    - **expiration date:** 04 / 24
    - **CVC:** 242
    - **ZIP:** 42424

- By clicking on the "complete order and pay" button, the payment process starts

- A webhook is implemented to the `checkout` so that the order is successfully processed in case the checkout process gets interrupted. Some reasons might be closing the browser too soon or losing internet connection

![checkout-payment](readme-files/features/checkout/checkout-payment.png)

![checkout-payment-mobile](readme-files/features/checkout/checkout-payment-mobile.png)

- While the payment is being processed, a loading overlay is shown to the user. The overlay contains an image and a loading spinner that rotates to show the user that the payment is being processed

![checkout-payment-loading](readme-files/features/checkout/checkout-payment-loading.png)

![checkout-payment-loading-mobile](readme-files/features/checkout/checkout-payment-loading-mobile.png)

- After the payment has been processed the user will land on the `checkout_success` page with an order summary

- The user will see an alert that the order was successfull

![checkout-success](readme-files/features/checkout/checkout-success.png)

![checkout-success-mobile](readme-files/features/checkout/checkout-success-mobile.png)

- If logged in, the user will see here a button "go to profile", which leads the user to their user profile

![checkout-ty](readme-files/features/checkout/checkout-ty.png)

![checkout-ty-mobile](readme-files/features/checkout/checkout-ty-mobile.png)

- If **not** registered or logged in, the user will see on the thank you page the button "to product overview"

![checkout-ty-logged-out](readme-files/features/checkout/checkout-ty-logged-out.png)

![checkout-ty-logged-out-mobile](readme-files/features/checkout/checkout-ty-logged-out-mobile.png)

### Profiles app
`profiles`
- When a user registers at Anime Art, an user profile will be created
- The purpose for a user to create an account is
    - to save their information for the next purchase
    - to see the full order history in one place

- The user can update their information in the profile

![profile-info-update](readme-files/features/profile/profile-info-update.png)

![profile-info-update-mobile](readme-files/features/profile/profile-info-update-mobile.png)

- The full order history can be viewed in the profile

- The order history contains the `order date`, `order number`, `quantity of products`, `product names`, `grand total` and is visually displayed via an Bootstrap5 accordion, that closes the last menu item, when a new one is being opened

![profile-order-history](readme-files/features/profile/profile-order-history.png)

![profile-order-history-mobile](readme-files/features/profile/profile-order-history-mobile.png)

![profile-order-history-accordion](readme-files/features/profile/profile-order-history-accordion.png)

![profile-order-history-accordion-mobile](readme-files/features/profile/profile-order-history-accordion-mobile.png)

## Features left to implement
### Footer upgrade
- [SEO](https://en.wikipedia.org/wiki/Search_engine_optimization) wise it would be good to have more text and keywords related to the product that Anime Art sells in the footer, as well as blog articles, etc.

- A proper imprint and a contact page (with a contact form) should be implemented, to make the website more serious and trustworthy

- A newsletter sign-up field and a regular newsletter about new products would help promote the website and bring frequent traffic to the page

### Django pagination
- When more and more products will be added, something like [django pagination](https://docs.djangoproject.com/en/3.2/topics/pagination/) should be added, so the user does not have to scroll through the whole page

### Sorting products
- At the moment there are only two types of products (with only two different prices). As the inventory increases and more products with different prices will be added, then the user should be given the option not only to filter by type but also to sort the products by price

### Service to host static images
- As the product range is very small right now and is not increasing daily, I did not use any service for hosting static files (like [AWS](https://aws.amazon.com/)). As Heroku does not host static files by default, I used the workaround with [Whitenoise](http://whitenoise.evans.io/en/stable/), but this is not a scalable solution and does not allow you to upload images when adding or updating products in the `add_product` and `update_product` form

# Technologies used
## Languages
- [Python](https://www.python.org/): logic and structure for backend
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript): to add interactivity to the frontend
- [HTML](https://en.wikipedia.org/wiki/Hypertext_Markup_Language): to structure the website
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/): templating language for python

## Database
- [SQLite](https://www.sqlite.org/index.html): default database in django; used in development
- [PostgreSQL](https://www.postgresql.org/): production database in heroku

## Styling
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets): to style the HTML code
- [Bootstrap 5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/): to add responsiveness, styling and some functionality
- [Fontawesome](https://fontawesome.com/): as an icon library
- [Google Fonts](https://fonts.google.com/): as a font resource
- [Favicon](https://favicon.io/): to generate favicon

## Frameworks and libraries
- [Django](https://www.djangoproject.com/): high-level Python web framework
- [JQuery](https://jquery.com/): as a JavaScript library

## Planning
- [Balsamiq](https://balsamiq.com/): for creating wireframes
- [Google Sheets](https://en.wikipedia.org/wiki/Google_Sheets): to write user stories and plan the data models
- [DBeaver](https://dbeaver.io/): for entity relationship diagram
- [draw.io](https://draw.io): for database schema

## Testing 
- [Am I responsive?](http://ami.responsivedesign.is/): for checking responsiveness on different screen sizes and using screenshot as a showcase for this projects README.md
- [Comparium](https://front.comparium.app/livetesting): For live testing on different browsers
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools): constantly testing styling, responsiveness and functionality

## Miscellaneous:

- [Github](https://github.com/): for hosting the projects repository
- [Git](https://en.wikipedia.org/wiki/Git): for version control
- [Heroku](https://www.heroku.com/): cloud platform for deploying web app
- [Stripe](https://stripe.com/en-gb-de): to manage (test) payment transactions
- [Visual Studio Code](https://code.visualstudio.com/): as a IDE (Integrated Development Environment) for developing the project
- [Popper.js](https://getbootstrap.com/docs/5.1/getting-started/introduction/): required for using bootstrap
- [Gmail](https://www.google.com/intl/en/gmail/about/): for sending emails

## Code Validation Tools
- [PEP8 checker](http://pep8online.com/): to validate Python code
- [JShint](https://jshint.com/) to validate JavaScript code
- [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code
- [W3 HTML Validator](https://validator.w3.org/) to validate HTML code

# Database
As Django works with SQL databases by default, I was using SQLite in development. When deploying to Heroku, it provides a PostgreSQL database, that was used for deployment.

## Entity Relationship Diagram
![erd](readme-files/db-images/erd.jpeg)

## Data Models
![database-models](readme-files/db-images/database-models.png)

# Testing
Please find all the testing documentation in the [TESTING.md file](https://github.com/jacqueline-kraus/MS4-anime-art/blob/main/TESTING.md)

# Deployment
To run this project, you have to install 
- [Python3](https://www.python.org/downloads/): to run the app
- [PIP](https://pip.pypa.io/en/stable/installation/): to install all app requirements
- Any [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) (e.g. [Visual Studio Code](https://code.visualstudio.com/)) or if you want to work virtually e.g. [Gitpod](https://www.gitpod.io/)
- [GIT](https://gist.github.com/derhuerst/1b15ff4652a867391f03): for cloning and version control

And you have to create (free) accounts for these services:
- [Stripe](https://stripe.com/en-gb-de)
- [Gmail](https://www.google.com/intl/en/gmail/about/)

## [Local deployment](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
1. Clone repository
- Go to repository
- Click on the button "code"
- Select the "HTTPS" option
- Copy the URL presented
- Open your Terminal
- Create a directory for storing this repository
- Type `git clone https://github.com/jacqueline-kraus/MS4-anime-art.git`
- Press enter to create local clone repository
- Alternatively, if using Gitpod, you can click below to create your own workspace using this repository

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/jacqueline-kraus/MS4-anime-art)

2. Set up environment variables
- Create an `.env.py` file with your own credentials. You can use this [.env_sample.py](https://github.com/jacqueline-kraus/MS4-anime-art/blob/main/env_sample.py) file as a sample and insert your environment variables

3. Install all requirements from `requirements.txt`:
```
pip3 install -r requirements.txt
```

4. Migrate the models to create the database schema:
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

5. Load the data fixtures in this exact order:
```
python3 manage.py loaddata types
```
```
python3 manage.py loaddata products
```

6. Create a superuser in order to access the django admin panel:
```
python3 manage.py createsuperuser


(assign an admin username, email, and secure password)
```

7. Launch the django project in the IDE terminal:
```
python3 manage.py runserver
```

8. Log into Django admin
- After running the web app, add `/admin` at the end of the URL and log in with the superuser credentials from the previous step

## Heroku Deployment
1. For Heroku to know which required dependencies to install, first create a `requirements.txt` file by running the following command in the CLI:
```
pip3 freeze --local > requirements.txt
``` 

2. Create a `Profile` in the root directory and add the following line to the file:
```
web: gunicorn anime_art.wsgi:application
```

3. Sign up and/or log in to [Heroku](https://www.heroku.com/)

4. Create a new app by clicking on the button "New"

5. Give your app a name, select your region and click "Create app"

6. Navigate to the "Deploy" tab and select "Github" as a deployment method

7. Search for your repository name and connect

8. Set up Heroku Postgres
- In the 'Resources' tab search for 'Heroku Postgres'
- Select the 'Hobby Dev' free plan

9. Set up conf variables
- Open the "Settings" tab and click on "Reveal Config Vars"
- Add your configuration variables, you can find these in your `.env.py` file

10. Set up a new database
- In `settings.py`:
```
import dj_database_url
```
- Comment out `DATABASES` (temporarily, do not commit/push this code to GitHub until instructed so)
- Add this code snippet:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('<your Postgres database URL>'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

11. Migrate the models to the Postgres database:
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

12. Load the data fixtures in this exact order:
```
python3 manage.py loaddata types
```
```
python3 manage.py loaddata products
```

13. Create a superuser in order to access the Django admin panel:
```
python3 manage.py createsuperuser


(assign an admin username, email, and secure password)
```

14. Push to GitHub:
```
git add.

git commit -m "<your commit message>"

git push
```

10. Set up automatic deploys
- Go back to Heroku, navigate to the tab "Deploy" and enable "Automatic Deploys"
- Every time you push now to your Github repository the changes will be automatically deployed in Heroku.

## Handling payments with Stripe
1. Sign up for a free Stripe account

2. Navigate to the Developers section > click on API Keys

3. You should have two confidential keys which need to be added to your `.env` file and your Heroku Config Vars:
- Publishable Key (`STRIPE_PUBLIC_KEY`): pk_test_key
- Secret Key (`STRIPE_SECRET_KEY`): sk_test_key

## Sending emails through Gmail
1. If you don't have a Gmail account yet, then you have to create one

2. Navigate to "Other Google Account Settings" > "Security" tab > turn on 2-step-verification

3. Go back to the "Security" tab and click on "App passwords"

4. Select "Mail" (in app dropdown) > select "Other" (in device dropdown)

5. Copy the 16-character password

6. Open Heroku > Settings > Reveal Config Vars

7. Add copied password to `EMAIL_HOST_PASS` config var

8. Add the Gmail email address to `EMAIL_HOST_USER` config var


# Credits

## Images
- Product images created by [Shippudeve](https://www.instagram.com/shippudeve/)
- Heroimage from [Pixabay.com](https://pixabay.com/de/illustrations/naruto-ninja-maske-charakter-5752319/)
- Loading Spinner from [Pixabay.com](https://pixabay.com/de/illustrations/moe-frau-m%c3%a4dchen-manga-anime-595954/)
- Image "Image coming soon" from [Freeiconspng.com](https://www.freeiconspng.com/downloadimg/23499)
- Favicon from [Softicons.com](https://www.softicons.com/culture-icons/sharingan-icons-1.5-by-harenome-razanajato/kakashi-icon)


## Problem solving helpers
- [Django documentation](https://docs.djangoproject.com/en/3.2/)
- [Bootstrap documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- [W3Schools.com](https://www.w3schools.com/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn)
- [Stackoverflow](https://stackoverflow.com/)
- [Python documentation](https://docs.python.org/3/)

## Code
- [Boutique Ado Walkthrough Project from Code Institute](https://github.com/Code-Institute-Solutions/boutique_ado_v1): for understanding how django works, coded along many steps, to understand the concepts
- [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- [Google Fonts](https://fonts.google.com/): for the fonts used
- [Fontawesome](https://fontawesome.com/): for the icons
- [Ordinarycoders](https://www.ordinarycoders.com/blog/article/django-messages-framework): using messages in Django with bootstrap
- [Django-allauth.readthedocs.io](https://django-allauth.readthedocs.io/en/latest/installation.html): django allauth for authentication
- [Hover.css](https://github.com/IanLunn/Hover/blob/master/css/hover.css): hover effects
- [Stackoverflow](https://stackoverflow.com/questions/39031224/how-to-center-cards-in-bootstrap-4): aligning the product cards in center
- [SmileyChris](https://github.com/SmileyChris/django-countries): django countries in ISO format
- [Mdbootstrap](https://mdbootstrap.com/docs/standard/extended/back-to-top/):back to top button
- [Stripe](https://stripe.com/docs/webhooks/signatures): for payments

## Acknowledgments
- A huge thank you to [Shippudeve](https://www.instagram.com/shippudeve/) for letting me use her images and creativity 
- Also thank you so much, [Tim Nelson](https://github.com/TravelTimN)! He was an amazing mentor, who used his time and patience with me and helped me incredibly to stay motivated and optimistic in meeting my deadline.
- Also thanks to the Code Institute Slack Community and the Code Institute Tutors I could solve problems way faster than only by googling! Thank you.