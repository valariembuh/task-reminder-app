# Task Reminder API (Dockerized)

This project is a simple REST API built with Python (Flask) and containerized using Docker.

I created it to practice how applications are packaged, deployed, and run in a containerized environment — a key skill in DevOps.

---

## What the project does

- Add tasks
- View all tasks
- Run the application inside a Docker container

---

## Tech Stack

- Python (Flask)
- Docker

---

## Project Structure

task-reminder-app/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md

---

## How to run (Docker)

Build the image:

docker build -t task-reminder-app .

Run the container:

docker run -d -p 8080:8080 task-reminder-app

---

## Access the app

http://localhost:8080

---

## Example usage

Add a task:

curl -X POST http://localhost:8080/tasks \
-H "Content-Type: application/json" \
-d '{"task": "Learn Docker"}'

Get all tasks:

curl http://localhost:8080/tasks

---

## What I learned

- Writing Dockerfiles
- Running containers
- Building simple APIs
- Using Git and GitHub

---

## Next steps

- Add a database
- Use Docker Compose
- Deploy to the cloud

---

## Author

Valarie M
https://github.com/valariembuh
