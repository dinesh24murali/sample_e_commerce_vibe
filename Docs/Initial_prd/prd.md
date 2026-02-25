You are an expert at creating a PRD based on the content provided. I need to create an e-commerce site for selling books. The product contains 3 applications:

1. A customer facing web application where customer can buy books
2. A basic admin site
3. The backend webserver that handles API calls

# customer facing web application

Here are the list of needed screens:
- Home page
- book list page
- Single book page
- login page
- sign up page
- accounts page
- order history page
- order details page
- cart page
- checkout page
- payment page
- payment success/failed page

Here are the requirements:
- Each book will be under a category.
- The customer can change his name and email under accounts page
- I want to user `Razorpay` for payment integration
- The customers can access all the pages except the following pages without login:
    - cart
    - accounts
    - checkout
    - payment
    - order history page
    - order details page
- In the book list page the customer can filter the book list by category
- The customer will use email and password to login
## Tech stack
Here are the tools and frameworks to use:
- Frontend framework: ReactJS
- Create a single page application
- Redux for state management

# Admin site

Here are the list of needed screens:
- CRUD operation for categories
- CRUD operation for books
- Login screen

Here are the requirements:
- There is no registration process for admin users
- Each book will be part of a category
- Here is the schema/fields for a book:
    - Name
    - Category ID
    - Description
    - ImageUrl
    - Price
    - Discount
    - Tax
    - IsAvailable

## Tech stack
Here are the tools and frameworks to use:
- Frontend framework: ReactJS, ant design UI components
- Create a single page application
- Redux for state management

# Backend web server

Here are the requirements:
- The web server will server content to both the customer facing site as well as the admin.
- The web server should have seed scripts to add the following:
    - add admin user with default username and password
    - add sample 2 categories and 2 products
- All APIs that the Admin site calls requires JWT token based authentication
- Provide adequate logging in the APIs
- Add audit fields for all the tables

## Tech stack
Backend framework: Django
Payment gateway: Razorpay
Database: PostgreSQL

# Other requirements

- For the frontend related tasks tag @react-frontend-builder subagent
- For the backend related tasks tag @django-backend-builder
- Follow test driven development for the server side. Write the test cases first and then write the code.
- Mention best design pattern to follow to generate the code
    - Django: Settings Splitting, "Fat Models, Thin Views", Service Layer, Repository Pattern (via Managers), Class-Based Views (CBVs)
    - ReactJS: Container vs Presentational Components, Redux Toolkit Slices
- Follow proper folder structure for all 3 projects
- Each of the 3 projects should be in their own individual folders