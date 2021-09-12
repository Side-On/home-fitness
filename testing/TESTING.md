# Testing 

## User stories

Below I've gone through the journey of a potential customer. Each part meeting a users expectations and going through their user story. I've followed the spreadsheet whilst testing that each works as expected, any issues with the process has been documented along with the fixes. The testing was done on desktop, and the mobile screen testing was focused on the layout, as apposed to the functionality aspect. This is detailed in the CSS section of the testing.
<br>

### User Stories List

![User stories list](/testing/images/user_stories/user-stories-list.png)

<br>

#### User story 1 - What's the website about

![Index page](/testing/images/user_stories/user-story-1.png)

This is the first page the user sees. They are shown the hero image of a gym, and the name of the company. There is text at the bottom of the screen tellers users what the site is about. Below that is a selection of categories to shop by, and also why they should sign up to become a member. There is a navigation bar at the top of the page, which users can also choose a category they want to shop in. They can all choose all products, and they choose from price, rating or just all products.


#### User story 2 - Look at products

![Products page](/testing/images/user_stories/user-story-2.png)

If the user selects all products and chooses a way to sort by, they are taken to this page. This lists all products which are available on the site. Each page is different depending on what catergory they chose. So if the user selects weights, they'll be shown all items which are in the weights category. The product card displays the name, a photo of the product and also the price and rating.

#### User story 3 - Product details

![Product information page](/testing/images/user_stories/user-story-3.png)

After the user selected a product they want to look at, they'll be taken to the product information page. Again, this shows the price, rating and other information about the product. There is also a review section at the bottom of the page. Logged in users can leave reviews of each product. A non-logged in user is show two links to either sign in or register for an account.

#### User story 4 - Find a product

![Searching for a product](/testing/images/user_stories/user-story-search.png)

The search bar is located at the top of the page throughout the website. This allows users to search for any product by name, brand, description and category.

##### Results

![Search results](/testing/images/user_stories/user-story-search-results.png)

This shows the products page and search results.

#### User story 5 - Sort items by price

![Sorting products](/testing/images/user_stories/user-sort-products.png)

The user is able to look at all of the items, sorted by certain criteria. This example shows the items organised by cheapest first.

#### User story 6 - Add product to bag

![Add product to a bag](/testing/images/user_stories/user-story-4.png)

When the user clicks on the add to bag button, a notifcation will appear next to the bag logo, along with details of the product and the grand total.

##### Confirmation

![Shopping bag information](/testing/images/user_stories/user-story-5.png)

The user can then click on the bag item, and is shown the contents of their bag. Is also has a grand total of everything in there.

#### User story 7 - Alter quanitity of items in the bag

![Changing contents of the bag](/testing/images/user_stories/user-story-6.png)

If the user decides to buy more of the same product, they can change the quantity on the shopping bag page. When they click the make changes button, the new total cost is shown, and they are notified of the changes made.

#### User story 8 - Remove an item from the bag

![Remove an item from the bag](/testing/images/user_stories/user-story-remove-item-bag.png)

If the user no longer wants an item, they can selete the remove button.

#### User story 9 - Buy the items

![Order details](/testing/images/user_stories/user-story-7.png)

This is the checkout page where the user inputs all of their delivery details for the item. Each field with a * is required, and if that field is empty when the user presses Complete Checkout, they are notified that the field is empty.

#### User story 10 - Confirmation of the purchase

![Successful payment](/testing/images/user_stories/user-story-8.png)

This is the page shown when a payment has succeeded. The user is sent a notification email when the process is complete as well, with all of their order details. 

##### Confirmation email and payment through Stripe

![Payment succeeded events](/testing/images/user_stories/payment-succeeded-events.png)

This is the order confirmation the user receives. I used [Temp Email](https://temp-mail.org) to generate an email address to test the confirmation emails. This was also used when testing password resets and account verification. The webhook from [Stripe](https://stripe.com/gb) also confirms that the payment request was received and successfully made. 

#### User story 11 - Register

![Register](/testing/images/user_stories/user-register.png)

User registration page, allows user to enter their email and chosen username and password.

#### User story 12 - Login 

![Login](/testing/images/user_stories/user-login.png)

If the user already has an account they can do to this page and login here. This also has the reset password option, if the user has forgotten their password.

#### User story 13 - Forgot/reset password

![Password reset](/testing/images/user_stories/password-reset.png)

Asks the user to enter their account email address to send the password reset link to.

##### Password reset email 

![Password reset email](/testing/images/user_stories/password-reset-email.png)

Email to show this function works and the user is able to choose a new password by clicking on the link.

![Change password](/testing/images/user_stories/user-change-password.png)

#### User story 14 - Verify email address

![Verify email address](/testing/images/user_stories/user-verify-email.png)

### Logged in users

#### User story 15 - Log out of account

![Sign out](/testing/images/user_stories/user-sign-out.png)

This is to show the user can logout to secure their account, and also a notification to show this has been done.

#### User story 16 - Previous orders 

![User order history](/testing/images/user_stories/user-order-history.png)

This shows the currently logged in user all of their order history. Details of what was ordered, price and date of each order.

#### User story 17 - Leave a review

![Leave a review](/testing/images/user_stories/user-story-leave-review.png)

On any of the product pages, a logged in user can leave a review of an item. If the user isn't logged in, they are shown links to get them to either sign in, or register for an account.

#### User story 18 - Leave a fit tip

![Leave a fit tip](/testing/images/user_stories/user-story-leave-fit-tip.png)

This works the same as the review. If the user is logged in they can leave a fit tip, otherwise they are shown the sign up or login buttons. Taking them to the relevant page.

#### User story 19 - Change delivery address details

![Update address](/testing/images/user_stories/user-address-update.png)

A user can go to their profile and change their delivery address. The next time they order something, the new address will populate the fields.

### Admin

#### User story 20 - Add new product

![Add a product](/testing/images/user_stories/admin-add-product.png)

When the site admin is logged in, they can add a new product by clicking on the product management link on under the profile logo. They can use this to add all details to the product they want to add. Some fields are mandatory to create the basic set up of the product.

#### User story 21 - Edit a product

![Edit a product](/testing/images/user_stories/admin-edit-product.png)

Any existing product can be edited by going to the product page itself, and clicking the edit product button. This button is only visible to the site admin. Any user who tries to access a product edit page, who isn't logged in at the site admin, will be redirected to the sign in page.

#### User story - Delete a product

![Delete a product](/testing/images/user_stories/admin-delete-product.png)

This button is also only visible to the admin, and will remove the selected product from the database. Any user who copies the url to the delete page and isn't logged in as the site admin, will be redirected to the sign in page.



## HTML 

Working through the user stories I explored each link to reach the expected outcome. This was completed several times throughout the production of the project so I was constantly testing and resolving any issues with it.

### Code validation

Each HTML page was passed through [w3 Validator](https://validator.w3.org/). Below are some of the errors encountered. I've ignored the errors which are connecting to Django, for example: `{% extends "base.html" %}`

One error showing on the checkout.html page:

```
Empty heading.

From line 136, column 3; to line 136, column 51

<h1 class="text-light logo-font loading-spinner">↩    <
```
This is required for the overlay to show the loading spinner what a payment is being processed.


## CSS

### Code validation

### Responsive

## Python and Django

### Code Validation

## Any issues or other bugs in the project

