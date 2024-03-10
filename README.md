## Description

This is a CRUD (Create, Read, Update, Delete) application built with FastAPI for managing todos.

## Installation

1. Clone the repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run the application with `uvicorn main:app --reload`.

## Usage

You can interact with the API using tools like cURL or Postman. Here are some example requests:

- GET / - Returns a ping response.
- GET /todo - Retrieves the list of todos.
- POST /todo - Adds a new todo to the list.
- PUT /todo/{id} - Updates an existing todo.
- DELETE /todo/{id} - Deletes a todo.

### Sample Request (POST /todo)

```json
{
  "id": "3",
  "Activity": "Meeting with client at 10:00 AM."
}
