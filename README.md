# Simple REST API

This is a simple web API capable of CRUD operations on a "person" resource. Written in Python with the aid of the Django web framework, it utilises the SQLite database and Django REST framework for storage and serialisation of data.

## Set Up
1. Clone the repository to your local machine by running `git clone https://github.com/remikeks/simple-rest-api.git`.
2. Navigate to the project directory by running `cd simple-rest-api`.
3. Install the required packages by running `pip install -r requirements.txt`

## Running the Application
Run `python manage.py runserver` to start up the server on your local machine.

## Using the Application
1. To (C)reate a new "person" send a POST request to the `/api` endpoint.
2. To (R)ead, (U)pdate or (D)elete a "person" resource, send a GET, PUT(or PATCH) or DELETE request to the `/api/{user_id}` endpoint.