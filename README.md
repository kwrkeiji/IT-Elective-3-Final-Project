# canteen-project

Welcome to the *canteen-project* repository! This project serves as the backend for a canteen management system, providing essential user authentication, CRUD functionalities for products, categories, and orders, and rate-limiting features for API endpoints.

## User Authentication API

This API allows users to register, log in, and access protected routes. Below are the details for each endpoint.

### 1. User Registration

- **Method**: POST
- **Endpoint**: `/api/auth/register/`
- **Description**: This endpoint allows new users to create an account by providing a username, email, and password.

- **Request Body** (JSON):

    ```json
    {
      "username": "john",
      "email": "john@example.com",
      "password": "TestPass123",
      "password2": "TestPass123"
    }
    ```

- **Response**:
  - **Success**: Returns a success message and user details.
  - **Error**: Returns validation errors if the input is invalid.

### 2. User Login

- **Method**: POST
- **Endpoint**: `/api/auth/login/`
- **Description**: This endpoint allows users to log in by providing their username and password.

- **Request Body** (JSON):

    ```json
    {
      "username": "john",
      "password": "TestPass123"
    }
    ```

- **Response**:
  - **Success**: Returns an access token and user details.
  - **Error**: Returns an error message if the credentials are incorrect.

### 3. Access Protected Route

- **Method**: GET
- **Endpoint**: `/api/auth/protected/`
- **Description**: This endpoint is accessible only to authenticated users. It requires a valid Bearer token for access.

- **Authorization**:

  - **Type**: Bearer Token
  - **Token**: Include the access token received from a successful login in the Authorization header:
    
    ```
    Authorization: Bearer <access_token>
    ```

- **Response**:
  - **Success**: Returns protected resource data.
  - **Error**: Returns an error message if the token is missing or invalid.

---

## CRUD API Endpoints

### 1. Categories

#### a. List and Create Categories

- **Method**: GET, POST
- **Endpoint**: `/api/product/categories/`
- **Description**: 
  - GET: Retrieve a list of all categories.
  - POST: Create a new category.

- **Rate Limit**: 3 requests per minute.

- **Request Body (POST)** (JSON):

    ```json
    {
      "name": "Beverages"
    }
    ```

- **Response**:
  - **GET Success**: Returns a list of categories.
  - **POST Success**: Returns the created category.
  - **Rate Limit Exceeded**: Returns a 429 error with a message to wait before retrying.

#### b. Retrieve, Update, and Delete a Category

- **Method**: GET, PUT, DELETE
- **Endpoint**: `/api/product/categories/<int:pk>/`
- **Description**: 
  - GET: Retrieve details of a specific category.
  - PUT: Update a category.
  - DELETE: Delete a category.

- **Rate Limit**: 5 requests per minute.

- **Request Body (PUT)** (JSON):

    ```json
    {
      "name": "Snacks"
    }
    ```

- **Response**:
  - **GET Success**: Returns the category details.
  - **PUT Success**: Returns the updated category.
  - **DELETE Success**: Returns a success message.
  - **Rate Limit Exceeded**: Returns a 429 error with a message to wait before retrying.

---

### 2. Products

#### a. List and Create Products

- **Method**: GET, POST
- **Endpoint**: `/api/product/products/`
- **Description**: 
  - GET: Retrieve a list of all products.
  - POST: Create a new product.

- **Rate Limit**: 3 requests per minute.

- **Request Body (POST)** (JSON):

    ```json
    {
      "name": "Coke",
      "price": 1.50,
      "image": "image_url",
      "category": 1,
      "stock": 100
    }
    ```

- **Response**:
  - **GET Success**: Returns a list of products.
  - **POST Success**: Returns the created product.
  - **Rate Limit Exceeded**: Returns a 429 error with a message to wait before retrying.

#### b. Retrieve, Update, and Delete a Product

- **Method**: GET, PUT, DELETE
- **Endpoint**: `/api/product/products/<int:pk>/`
- **Description**: 
  - GET: Retrieve details of a specific product.
  - PUT: Update a product.
  - DELETE: Delete a product.

- **Rate Limit**: 5 requests per minute.

- **Request Body (PUT)** (JSON):

    ```json
    {
      "name": "Pepsi",
      "price": 1.75,
      "image": "new_image_url",
      "category": 1,
      "stock": 120
    }
    ```

- **Response**:
  - **GET Success**: Returns the product details.
  - **PUT Success**: Returns the updated product.
  - **DELETE Success**: Returns a success message.
  - **Rate Limit Exceeded**: Returns a 429 error with a message to wait before retrying.

---

### 3. Orders

#### a. List and Create Orders

- **Method**: GET, POST
- **Endpoint**: `/api/order/orders/`
- **Description**: 
  - GET: Retrieve a list of all orders.
  - POST: Create a new order.

- **Rate Limit**: 3 requests per minute.

- **Request Body (POST)** (JSON):

    ```json
    {
      "product": 1,
      "quantity": 2,
      "mode": "delivery",
      "total": 3.00
    }
    ```

- **Response**:
  - **GET Success**: Returns a list of orders.
  - **POST Success**: Returns the created order.
  - **Rate Limit Exceeded**: Returns a 429 error with a message to wait before retrying.

#### b. Retrieve, Update, and Delete an Order

- **Method**: GET, PUT, DELETE
- **Endpoint**: `/api/order/orders/<int:pk>/`
- **Description**: 
  - GET: Retrieve details of a specific order.
  - PUT: Update an order.
  - DELETE: Delete an order.

- **Rate Limit**: 5 requests per minute.

- **Request Body (PUT)** (JSON):

    ```json
    {
      "product": 1,
      "quantity": 3,
      "mode": "pick-up",
      "total": 4.50
    }
    ```

- **Response**:
  - **GET Success**: Returns the order details.
  - **PUT Success**: Returns the updated order.
  - **DELETE Success**: Returns a success message.
  - **Rate Limit Exceeded**: Returns a 429 error with a message to wait before retrying.

---

## Rate Limiting

### General Information

Rate limiting is applied to prevent abuse of the API. Each endpoint has a specific limit on the number of requests that can be made within a given time window. If the limit is exceeded, the server will respond with a `429 Too Many Requests` status code.

### Sample Rate Limit Response

- **Status Code**: 429
- **Response Body**:

    ```json
    {
      "error": "Too many requests",
      "detail": "Please wait 60 seconds before trying again.",
      "retry_after": 60
    }
    ```

- **Headers**:
  - `Retry-After`: Indicates the time (in seconds) the client should wait before retrying.


## Getting Started

To get started with the canteen-project, clone the repository and follow the setup instructions in the [Installation Guide](#).

## Contributing

Contributions are welcome! Please read the [Contributing Guidelines](#) for more information on how to contribute to this project.

## License

This project is licensed under the [MIT License](#).

---

Feel free to reach out if you have any questions or need further assistance!