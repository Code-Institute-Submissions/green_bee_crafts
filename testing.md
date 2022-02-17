# Testing

## Table of contents 
* [Code Validation](#validation)
* [Home Page](#homepage)
* [Navigation](#navbar)
* [Registration/ Login](#registration)
* [Products Page](#products)
* [Shopping Bag](#bag)
* [User Profile](#profiles)
* [Markets](#markets)
* [Upcylcing](#upcycle)

## Code Validation

* HTML code was vaildated through [WC3 HTML Markup validator](https://validator.w3.org/nu/) and passed.
* CSS code was vaildated using [WC3 CSS Validation](https://jigsaw.w3.org/css-validator/) and passed.
* JS code was validated using [JSHint](https://jshint.com/)

## Homepage
### Responsivness
* I tested in various devices including iMac, iPhone8, Samsung Tablet and iPad as well as various browswers including Chrome, Safari and Samsung.
* I checked for the quality of the landing page layout and title as well as colourings.
#### Conclusion
The landing page is clean and simple on all screen sizes encouraging the user to view products.
I am happy that it works well on all screen sizes and browsers.
### Functionality
The "Shop Now" button works and takes the user through to the products page.
### Lighthouse Report
### Mobile view

## Navigation
### Responsivness
* I tested in various devices including iMac, iPhone8, Samsung Tablet and iPad as well as various browswers including Chrome, Safari and Samsung.
### Functionality
- all users navigation

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Home button    | To redirect to home page | Click the home button | Button navigates to home | Pass |
| Navbar links | Clicking All Products takes user to All Products page | Click All Products | Redirected to All Products page | Pass |
|  | Clicking category takes user to the specific category page | Click each category in turn | Redirected to specific category page | Pass |
|   | Click Bag takes user to Bag page | Click Bag | Redirected to Bag page | Pass |
|   | Clicking Markets takes user to the Markets page | Click Upcoming Markets | Redirected to Markets Page | Pass |
|   | Clicking on the How we upycle page | Click Upcycling  | Redirected to How we upcycle page | Pass |

- users logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
||  Navbar links   | Clicking Profile takes user to their profile page | Click Profile | Redirected to Profile Page | Pass |
|  | Click Log Out logs out the user | Click Log Out | User logged out and redirected to Log In | Pass |


- user not logged in navigation

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Navbar links | Click Log In redirects to log in page | Click Log In | User redirected to Log In Page | Pass |
|  | Click Register redirects to log in page | Click Register | User redirected to Register Page | Pass |

### Lighthouse Report
### Mobile view

## Registration and Login
* During testing it became clear that the live email function was not working correctly, but after the removal of an unneeded config var it is all working corrrectly and new users can validate their email accounts and set up a profile.
### Responsivness
* I tested in various devices including iMac, iPhone8, Samsung Tablet and iPad as well as various browswers including Chrome, Safari and Samsung.
### Functionality
#### **Register Page**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Register functionality | Form validation for email requires `@` symbol |  Attempt to register without `@` in input field | Form validation requests valid email address | Pass |
| | E-mail Again value must be same as Email value | Attempt to register with incorrect email in email again input field | Form validation requests email address must match | Pass |
| | Username must be between 4 and 15 characters | Attempt to enter username with less than 4 characters | Feedback error displayed | Pass |
| | Username must be between 4 and 15 characters | Attempt to enter username with more than 15 characters | Form restricts the user from using more than 15 characters | Pass |
| | Password must be longer than 8 characters | Attempt to enter password with less than 8 characters | Form restricts the user from using less than 8 characters | Pass |
| | Register with new user and password to be logged in and redirected to Profile page | Enter email address, name, username, password and click register | New account registered and profile page shown | Pass |

#### **Log In Page**

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-----------------| ----------|  ---------- | :----: |
| Log in functionality | Correct user/pass combination directs user to their profile page with name displayed in tab | Log in with correct username/password combination | Redirected to user profile page with name displayed in tab | Pass |
|   | Incorrect username/password combination shows error message | Attempt to log in with incorrect credentials | "The username and/or password you specified are not correct." error message appears| Pass |
| Link to Register | Redirect to Register page | Click link to register | Redirected to Register page | Pass |

### Lighthouse Report
### Mobile view

## Products Page
### Responsivness
* I tested in various devices including iMac, iPhone8, Samsung Tablet and iPad as well as various browswers including Chrome, Safari and Samsung.
### Functionality
### Lighthouse Report
### Mobile view

## Shopping Bag
### Responsivness
* I tested in various devices including iMac, iPhone8, Samsung Tablet and iPad as well as various browswers including Chrome, Safari and Samsung.
### Functionality
### Lighthouse Report
### Mobile view

## User Profile
### Responsivness
* I tested in various devices including iMac, iPhone8, Samsung Tablet and iPad as well as various browswers including Chrome, Safari and Samsung.
### Functionality
### Lighthouse Report
### Mobile view

## Markets
### Responsivness
* I tested in various devices including iMac, iPhone8, Samsung Tablet and iPad as well as various browswers including Chrome, Safari and Samsung.
### Functionality
### Lighthouse Report
### Mobile view

## Upcycling Page
### Responsivness
* I tested in various devices including iMac, iPhone8, Samsung Tablet and iPad as well as various browswers including Chrome, Safari and Samsung.
### Functionality
### Lighthouse Report
### Mobile view


