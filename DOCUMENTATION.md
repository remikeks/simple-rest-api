# REST API Documentation

This documentation outlines the standard formats, sample usage, instruction for setting up and deploying the API, among others.

## Standard Formats

### Create Person 
1. Request format (http POST `/api`)
    ```
    {
    "name": "Mark Essien"
    }
    ```
2. Response format (json, 201 Created)
    ```
    {
    "id": 1,
    "name": "Mark Essien"
    }
    ```

### Retrieve Person 
1. Request format  (http GET `/api/{user_id}`)

2. Response Format (json, 200 OK)
    ```
    {
    "id": 1,
    "name": "Mark Essien"
    }
    ```

### Update Person 
1. Request format (http PATCH `/api/{user_id}`)
    ```
    {
    "id": 1,
    "name": "Elon Musk"
    }

2. Response format(json, 200 OK)
    ```
    {
    "id": 1,
    "name": "Elon Musk"
    }
    ```

### Delete Person
1. Request format (http DELETE `/api/{user_id}`)

2. Response format(204 No Content)
    ```
    No content

    ```

## Sample API Usage

### Create Person 
1. Example Request: POST `/api`
    * * request body
    ```
    {
    "name": "Mark Essien"
    }
    ```
2. Expected response
    ```
    {
    "id": 1,
    "name": "Mark Essien"
    }
    ```

### Retrieve Person 
1. Sample request:  GET `/api/1`

2. Expected response
    ```
    {
    "id": 1,
    "name": "Mark Essien"
    }
    ```

### Update Person 
1.Sample Request: PATCH `/api/1`
    ```
    {
    "id": 1,
    "name": "Elon Musk"
    }

2. Expected Response
    ```
    {
    "id": 1,
    "name": "Elon Musk"
    }
    ```

### Delete Person
1. Sample Request: DELETE `/api/1`

2. Expected Response (204 No Content)
    ```

    ```

## Limitations or Assumptions
1. The json payload in the body of the POST request must be string-only.

## Set Up
1. For set up instructions, see [README](/README.md)

## Deployment
1. To run your site locally, run the command `python manage.py runserver` to start up the server.
Visit `http://localhost:8000/api/` to access the API.

2. On a remote server, sign up and follow the instructions provided on your preferred hosting service. Eg. [Render](https://www.render.com)


