# Smart Home API

## Overview
The Smart Home API is a RESTful API built with FastAPI that allows users to manage homes, rooms, and smart devices.  
It provides endpoints for creating, retrieving, updating, and deleting Users, Houses, Rooms, and Devices while ensuring data validation and error handling.

## Features
- User Management: Create, update, and delete users.
- House Management: Assign owners, update details, and retrieve house information.
- Room Management: Link rooms to houses and manage smart devices.
- Device Management: Add, update, and delete devices in rooms.
- Error Handling: Ensures validation for emails, IDs, and duplicates.
- Unit Testing: Fully tested using `pytest`.
- Continuous Integration: Automated testing through GitHub Actions.

## Tech Stack
- FastAPI: Web framework for building APIs.
- Pydantic: Data validation and serialization.
- Uvicorn: ASGI web server.
- Pytest: Automated testing.
- GitHub Actions: Continuous integration for automated testing.
