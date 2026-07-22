# Python HTTP Server

A lightweight HTTP server built using Python's standard `http.server` module.

This project demonstrates how to build a simple HTTP server **without using any third-party frameworks** such as Flask or Django. It follows clean architecture principles by separating request handling, response generation, constants, and utility functions into different modules.

---

## Features

- Built using Python's built-in `http.server`
- Class-based request handler
- Clean project structure
- Separation of concerns
- Manual JSON response construction
- Plain text and JSON responses
- Echo request body for POST requests
- Proper HTTP status codes
- Handles unsupported routes and methods
- No external dependencies

---

## Project Structure

```
python_http_server/
│
├── main.py              # Application entry point
├── server.py            # HTTP server configuration
├── handlers.py          # Request handler
├── responses.py         # Response helper methods
├── utils.py             # Utility functions
├── constants.py         # Application constants
└── README.md
```

---

## Requirements

- Python 3.8+

No external packages are required.

---

## Running the Server

Navigate to the project directory:

```bash
cd python_http_server
```

Start the server:

```bash
python main.py
```

or

```bash
python3 main.py
```

If the server starts successfully, you'll see:

```
Server running at http://localhost:8000
```

---

## Supported Endpoints

### 1. GET /

Returns a plain text welcome message.

**Request**

```
GET /
```

**Response**

Status:

```
200 OK
```

Content-Type:

```
text/plain
```

Body

```
Welcome to the Python HTTP Server!
```

---

### 2. GET /time

Returns the current server time as JSON.

**Request**

```
GET /time
```

**Response**

Status

```
200 OK
```

Content-Type

```
application/json
```

Example response

```json
{
    "server_time": "2026-07-08 16:45:21"
}
```

---

### 3. POST /echo

Reads the request body and sends it back unchanged.

Example using curl:

```bash
curl -X POST \
-d "Hello World" \
http://localhost:8000/echo
```

Response

```
Hello World
```

You can also send JSON:

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"name":"Jamshaid"}' \
http://localhost:8000/echo
```

Response

```json
{"name":"Jamshaid"}
```

---

## Error Handling

### Unknown Route

Request

```
GET /unknown
```

Response

```
404 Not Found
```

---

### Unsupported HTTP Method

Request

```
PUT /
```

Response

```
405 Method Not Allowed
```

---

## Example Requests

### Browser

Open:

```
http://localhost:8000/
```

or

```
http://localhost:8000/time
```

---

### Using curl

Welcome message

```bash
curl http://localhost:8000/
```

Current server time

```bash
curl http://localhost:8000/time
```

Echo text

```bash
curl -X POST \
-d "Hello Python" \
http://localhost:8000/echo
```

Echo JSON

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"language":"Python"}' \
http://localhost:8000/echo
```

---

## HTTP Status Codes Used

| Status Code | Description |
|-------------|-------------|
| 200 | Request completed successfully |
| 404 | Requested resource not found |
| 405 | HTTP method not supported |

---

## Design Principles

The project follows several software engineering best practices:

- Single Responsibility Principle (SRP)
- Separation of concerns
- Reusable helper functions
- Centralized constants
- Minimal code duplication
- Clean and modular architecture

---

## Author

Jamshaid Mehmood
