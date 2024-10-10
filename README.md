# kumo-hq interview task

create the backend APIs 

1. Signup API

Endpoint: /api/auth/signup
Method: POST
Description: Register a new user

Request Body:

{
  "email": "string",
  "password": "string",
}

Response:

{
  "id": "string",
  "email": "string",
  "message": "User registered successfully"
}

2. Login API

Endpoint: /api/auth/login
Method: POST
Description: Authenticate a user and return a token

Request Body:

{
  "email": "string",
  "password": "string"
}

Response:

{
  "token": "string",
  "id": "string",
  "email": "string"
}

3. Validate Token API

Endpoint: /api/auth/validate
Method: GET
Description: Validate the user's token

Request Headers:

Authorization: Bearer <token>

Response:

{
  "valid": true,
  "id": "string",
  "email": "string"
}

User Books APIs
1. Create Book API

Endpoint: /api/books
Method: POST
Description: Create a new book for the authenticated user

Request Headers:

Authorization: Bearer <token>

Request Body:

{
  "title": "string",
  "author": "string",
  "isbn": "string",
  "published_date": "string (YYYY-MM-DD)"
}

Response:

{
  "id": "string",
  "title": "string",
  "author": "string",
  "isbn": "string",
  "published_date": "string (YYYY-MM-DD)",
  "user_id": "string"
}

2. Get Books with Filter API

Endpoint: /api/books
Method: GET
Description: Retrieve books for the authenticated user with optional filters

Request Headers:

Authorization: Bearer <token>

Query Parameters:

title (optional): Filter by book title (partial match)
author (optional): Filter by author name (partial match)
start_date (optional): Filter by published date range start
end_date (optional): Filter by published date range end
page (optional): Page number for pagination
per_page (optional): Number of items per page

Response:

{
  "total": 0,
  "page": 0,
  "per_page": 0,
  "books": [
    {
      "id": "string",
      "title": "string",
      "author": "string",
      "isbn": "string",
      "published_date": "string (YYYY-MM-DD)"
    }
  ]
}

Frontend

Create a login page, register page, dashboard and logout. Redirect to login page when logged out.



