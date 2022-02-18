# Testing

## Contents 
* [Code Validation](#validation)
* [Functionality](#functionality)
* [Home Page](#homepage)
* [Navigation](#navbar)
* [Registration/ Login](#registration-and-login)
* [Products Page](#products-pages)
* [Shopping Bag](#bag)
* [Checkout](#checkout)
* [User Profile](#user-profile)
* [Markets](#markets)
* [Upcylcing](#upcycling-page)
* [Lighthouse](#lighthouse)
* [User Stories Testing](#user-stories-testing)

## Code Validation

* HTML code was vaildated through [WC3 HTML Markup validator](https://validator.w3.org/nu/) and passed.
* CSS code was vaildated using [WC3 CSS Validation](https://jigsaw.w3.org/css-validator/) and passed.
* JS code was validated using [JSHint](https://jshint.com/)

[Back to contents](#contents)

## Responsivness
* I tested in various devices including iMac, iPhone8, Samsung Tablet and iPad as well as various browswers including Chrome, Safari and Samsung.
* I checked for the quality of the landing page layout and title as well as colourings.
#### Conclusion
The landing page is clean and simple on all screen sizes encouraging the user to view products.
I am happy that it works well on all screen sizes and browsers.

[Back to contents](#contents)

## Functionality
### Homepage

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Shop Now button    | To redirect to products page | Click the shop now button | Button navigates to all products page | Pass |

[Back to contents](#contents)

### Navigation
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

[Back to contents](#contents)

### Registration and Login
* During testing it became clear that the live email function was not working correctly, but after the removal of an unneeded config var it is all working corrrectly and new users can validate their email accounts and set up a profile.

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

[Back to contents](#contents)

### Products Pages
##### **Products**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| All products visible | Products page shows all products | Open Products page and view products | Products visible and 12 to a page  | Pass |
|  | Searching by category shows products from that category | Select to search by each category | Products from each category successfully displayed | Pass |

##### **Product Details**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Product Details | Product description displayed for individual product | Open Product Detail page and view products | Product details visible | Pass |
| Add to bag | Clicking Add To Bag adds the product to the bag | Open Product Detail page click add to bag | Product available in bag | Pass |
|

##### **Add Product**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Add Products | Only admin is allowed to visit add product page | Log in as non-superuser and attempt to access /products/add/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass |
| Form Validation | Required fields must be completed to add the product  | Attempt to add product without filling in a required field | Error message "Please fill in this field" | Pass |


##### **Edit Product**
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Edit Products | Only admin is allowed to visit edit product page | Log in as non-superuser and attempt to access /products/<item_id>/edit/ | Redirect to home page, error message displayed "Sorry, only store owners can do that." | Pass |
| Form Validation | Required fields must be completed to edit the product  | Attempt to edit product without filling in a required field | Error message "Please fill in this field" | Pass |

[Back to contents](#contents)

### Shopping Bag
| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| View Items | Correct products are in the bag | Add product to bag and check quantity and total are in the bag | Expected products are in the bag | Pass |
| Update Items | Update the number of a product in the bag and it will reflect in bag and price | Change number of product in bag and check quantity and total has updated | Total and quantity updated | Pass |
| Remove Items | Click remove item for item to be removed from the bag | Click remove beside relevant product | Item removed from bag and notification to confirm this "Removed <item> from your bag" | Pass |

[Back to contents](#contents)

### Checkout

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| View Items | Correct products are in the checkout | Add products to bag, click Secure Checkout | Expected products are in the checkout product list | Pass |
| Form Validation | Required fields must be completed to complete  | Attempt to check out without filling in a required field | Error message "Please fill in this field" | Pass |

[Back to contents](#contents)

### User Profile

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Personal Information | Personal information is visible if previously saved | Navigate to Profile page, view personal information | The personal information is visible in Personal Information section | Pass |
| | Order History | Order History is visible if order placed while logged in | Navigate to Profile page, view Order History Section | The Order History is visible | Pass |
| | Order information can be accessed by clicking order number | Navigate to Profile page, view Order History Section, click Order Number | Order Information is visible | Pass |

[Back to contents](#contents)

### Markets

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| Upcoming Markets | Information on upcoming markets visible | Navigate to Upcoming Markets page, view upcoming markets information | The upcomimg marjets are visilbe in this section | Pass |

[Back to contents](#contents)

### Upcycling Page

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----:|
| How we upcycle | Information on upcycling is visilbe in this section | Navigate to Upcycling information page, view upcycling information | The upcomimg marjets are visilbe in this section  Pass |

[Back to contents](#contents)

### User Stories Testing

| User Story ID  | As a/an  | I want to be able to...  | So that I can... | Testing | Pass/Fail |
|-------------------|-------------------|-----------------|-------------------|-------------------|---------------|
| Viewing Products & Navigation |
| 1  | User/Shopper | view individual products | identify their qualities and compare. | View Products | Pass |
| 2  |  User/Shopper | be able to add, edit quantity and remove items from my bag | buy them after browsing. | add product to bag,  update item quantity, remove item from bag | Pass |
| 3  | User/Shopper  | see any special offers | take advantage of saving money on products I'd like to buy. | Navigation bar displays free shipping if shopper spends £50 or more | Pass |
| 4  |  User/Shopper | see when the next face to face markets are and where they will be. | go to see products in real life and meet the maker. | Details of up coming markets can be viewed | Pass |
| 5  | User/Shopper  | find out more about the upcycling processes that Green Bee uses as well as information about when materials are sourced from. | have better information about the history and ethics behind an item | Upcycling page has information about the sourcing of products and materials visible for the user | Pass |
| Registration and Accounts |
| 6  | User/Shopper | register for an account | keep track of my orders and check my personal details. | Users can register, for an account and view their orders in the profile page | Pass |
| 7  |  User/Shopper | receive email confirmation upon signing up | verify my set up was successful. | User receives email when they register for an account | Pass |
| 8  |  User/Shopper | be able to reset my password in case I forget it | gain access to my account. | User can request  to reset their password | Pass |
| 9  | User/Shopper  | have the ability to log in to the site with my details | view my orders and personal details | Users can log in using their registered details and view their orders and personal details | Pass |
| 10  | User/Shopper | update my personal details | keep them up to date. | Users can update their personal details in the profile section | Pass |
| 11 | User/Shopper  | purchase from the site without having to create an account | check out quickly and easily. | Users can use the checkout without registering for an account  | Pass |
| 12  | User/Shopper | search for specific products | find products I am interested in buying. | Users can search on the site for products and if no product available message to confirm this | Pass |
| 13  | User/Shopper  | sort by price, name, category | view a wide range and choose which to buy. | Users can sort by price, name and category on the products page | Pass |
| Checkout  |
| 14 | Shopper | have a running total of my bag | stay within my budget. | Users can see the total in the bag icon on the navbar. | Pass |
| 15  | Shopper  | view my bag contents | keep track of which products I have selected. | Users can view their bag to see which products and quantities have been added | Pass |
| 16  | Shopper  | adjust the quantity of products to buy | update the order without going back to the product page. | Users can update quantities in the shopping bag successfully. | Pass |
| 17  |  Shopper | easily enter my payment details | checkout as quickly and easily as possible. | Users can navigate the checkout form payment input easily | Pass |
| 18  |   | view the full order before entering card details | check it before confirmation. | The Order can be viewed on the checkout page before entering card details | Pass |
| 19  | Shopper  | receive email notifications when I make an order | confirm my order has been placed and refer back to. | Users receive an email | Pass |
| Admin/Management  |
| 20  | Store owner/Admin | add a product | sell new items in my store  | Super users can add a product  | Pass |
| 21  | Store owner/Admin  | update a product | change descriptions, sizes, images in my store. | Super users can edit a product | Pass |
| 22  | Store owner/Admin  | delete a product | remove items no longer on sale. | Super users can delete a product | Pass |

[Back to contents](#contents)

## Wave

The site was inspected for accessibility using the [Wave Browser Extension](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh) and changes made to HTML following this inspection. 
The result is no major errors although my lablelling need to improve for accessibility.

## Lighthouse
