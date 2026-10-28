LITTLE LEMON - BACK-END DEVELOPER CAPSTONE
==========================================

A Django + Django REST Framework API for the Little Lemon restaurant.
It serves a static HTML page, a menu API and a table booking API,
stores data in MySQL, and uses token authentication (Djoser + DRF).


SETUP
-----
1. Install the packages:
       pipenv install -r requirements.txt
       pipenv shell
   (or: pip install -r requirements.txt)

2. Create the MySQL database:
       CREATE DATABASE littlelemon;

3. Put your MySQL user and password in littlelemon/settings.py
   (DATABASES section), or set DB_USER and DB_PASSWORD as environment variables.

4. Run:
       python manage.py migrate
       python manage.py createsuperuser
       python manage.py runserver


PATHS TO TEST (base URL: http://127.0.0.1:8000)
-----------------------------------------------

Static HTML page
    /restaurant/                                GET

User registration and authentication (Djoser)
    /auth/users/                                POST   register: username, email, password
    /auth/users/me/                             GET    current user (needs token)
    /auth/token/login/                          POST   username + password -> auth_token
    /restaurant/api-token-auth/                 POST   username + password -> token

Menu API (needs token)
    /restaurant/menu/                           GET    list all menu items
    /restaurant/menu/                           POST   add a menu item (title, price, inventory)
    /restaurant/menu/<id>                       GET    one menu item
    /restaurant/menu/<id>                       PUT / PATCH   update a menu item
    /restaurant/menu/<id>                       DELETE delete a menu item

Table booking API (needs token)
    /restaurant/booking/tables/                 GET    list all bookings
    /restaurant/booking/tables/                 POST   add a booking (name, no_of_guests, booking_date)
    /restaurant/booking/tables/<id>/            GET    one booking
    /restaurant/booking/tables/<id>/            PUT / PATCH   update a booking
    /restaurant/booking/tables/<id>/            DELETE delete a booking

Admin
    /admin/


TESTING WITH INSOMNIA
---------------------
1. POST /auth/users/ with a username, email and password to register.
2. POST /restaurant/api-token-auth/ with the same username and password.
   Copy the "token" value from the response.
3. For every menu and booking request, add this header:
       Authorization: Token <your-token>
   Without the header, the API returns 401 Unauthorized.

Example body for POST /restaurant/menu/
    {"title": "Greek Salad", "price": "12.50", "inventory": 20}

Example body for POST /restaurant/booking/tables/
    {"name": "John", "no_of_guests": 4, "booking_date": "2026-11-02T19:30:00Z"}


UNIT TESTS
----------
Tests are in the project-level tests/ folder (test_models.py, test_views.py).
Run them with:
       python manage.py test
