# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to manage tasks. Practice defining endpoints, accepting validated request data, and returning appropriate responses and status codes.

## 📝 Tasks

### 🛠️ List Tasks

#### Description
Install FastAPI with `python -m pip install "fastapi[standard]"`, then start the app with `fastapi dev main.py`. Complete the `GET /tasks` endpoint in the starter code so clients can retrieve all tasks currently stored by the API. Use the interactive documentation at `http://127.0.0.1:8000/docs` to try your endpoints.

#### Requirements
Completed program should:

- Return a JSON array from `GET /tasks`
- Return an empty array when no tasks have been added
- Include each task's `id`, `title`, and `completed` fields in the response


### 🛠️ Create Tasks

#### Description
Add a `POST /tasks` endpoint that accepts a task title and an optional `completed` value. Give each new task a unique ID and keep it in the in-memory task list.

#### Requirements
Completed program should:

- Accept a JSON request body with a non-empty `title` and an optional `completed` boolean
- Return the newly created task as JSON with its assigned `id`
- Respond with HTTP `201 Created` when a task is added
- Reject an empty title with a validation error


### 🛠️ Retrieve a Task

#### Description
Add a `GET /tasks/{task_id}` endpoint to retrieve one task by its ID.

#### Requirements
Completed program should:

- Return the matching task as JSON when the ID exists
- Respond with HTTP `404 Not Found` when the ID does not exist
- Keep the response fields consistent with `GET /tasks`


### 🛠️ Delete a Task

#### Description
Add a `DELETE /tasks/{task_id}` endpoint so clients can remove a task by its ID.

#### Requirements
Completed program should:

- Remove the matching task from the in-memory task list
- Respond with HTTP `204 No Content` when the task is deleted
- Respond with HTTP `404 Not Found` when the ID does not exist
