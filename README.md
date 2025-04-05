**Task Manager API**

Welcome to the **Task Manager API**! This project is designed to help you manage tasks effectively. Built with **Flask**, **Celery**, **PostgreSQL**, and **Redis**, it provides a secure and efficient way to create, update, delete, and track tasks. Whether you're building an app or just need a backend service for task management, this is a great starting point.

Features
- Create, Read, Update, Delete (CRUD): Full support for managing tasks.
- Background Processing with Celery: Automatically handle recurring tasks in the background.
- Role-Based Access Control: Manage who can do what on the platform.
- Testing with pytest: Make sure everything works as expected.
- Containerized with Docker: Easily deploy with Docker and Docker Compose.

Tech Stack
-Flask: The micro web framework that powers this API.
- SQLAlchemy: Manages database interactions.
- PostgreSQL: Stores data about tasks and users.
- Celery: Handles background tasks like sending emails or processing files.
- Redis: The message broker that Celery uses.
- Docker: Containerizes the app and its dependencies for easy deployment.
- pytest: For writing and running tests.
