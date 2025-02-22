🏠 Smart Home API

📌 Overview

The Smart Home API is a RESTful API built with FastAPI that allows users to manage homes, rooms, and smart devices.It provides endpoints for creating, retrieving, updating, and deleting Users, Houses, Rooms, and Devices while ensuring data validation and error handling.

🚀 Features

✅ User Management – Create, update, delete users✅ House Management – Assign owners, update details, retrieve house info✅ Room Management – Link rooms to houses, store smart devices✅ Device Management – Add, update, and delete devices in rooms✅ Error Handling – Ensures validation for emails, IDs, and duplicates✅ Unit Tests – API is fully tested using pytest✅ GitHub Actions CI/CD – Runs automated tests on every push

🧐 Tech Stack

FastAPI – Web framework for building APIs

Pydantic – Data validation and serialization

Uvicorn – ASGI web server

Pytest – Automated testing

GitHub Actions – CI/CD for running tests automatically

👤 Project Structure

smart-home-api/
│\── app/
│   ├── __init__.py
│   ├── main.py  # Main entry point
│   ├── data_model.py  # Pydantic models
│   ├── routes/
│   │   ├── users.py  # User API endpoints
│   │   ├── houses.py  # House API endpoints
│   │   ├── rooms.py  # Room API endpoints
│   │   ├── devices.py  # Device API endpoints
│\── tests/
│   ├── test_users.py
│   ├── test_houses.py
│   ├── test_rooms.py
│   ├── test_devices.py
│\── .github/workflows/
│   ├── test.yml  # GitHub Actions CI/CD
│\── requirements.txt  # Dependencies
│\── README.md  # Documentation

🛠️ Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/your-username/smart-home-api.git
cd smart-home-api

2️⃣ Create a Virtual Environment

python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate  # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the API

uvicorn app.main:app --reload

✅ Open http://127.0.0.1:8000/docs to access the interactive API documentation.

🛠️ API Endpoints

📌 Users

Method

Endpoint

Description

POST

/users/

Create a new user

GET

/users/email/{email}

Get user by email

PUT

/users/email/{email}

Update user details

DELETE

/users/email/{email}

Delete user

📌 Houses

Method

Endpoint

Description

POST

/houses/

Create a new house

GET

/houses/id/{house_id}

Get house by ID

GET

/houses/id/{house_id}/owners

Get house owners

PUT

/houses/id/{house_id}

Update house details

DELETE

/houses/id/{house_id}

Delete house

📌 Rooms

Method

Endpoint

Description

POST

/rooms/

Create a new room

GET

/rooms/name/{room_name}

Get room details

GET

/rooms/name/{room_name}/devices

Get devices in a room

PUT

/rooms/name/{room_name}

Update room details

DELETE

/rooms/name/{room_name}

Delete room

📌 Devices

Method

Endpoint

Description

POST

/devices/

Create a new device

GET

/devices/name/{device_name}

Get device details

PUT

/devices/name/{device_name}

Update device details

DELETE

/devices/{device_name}

Delete device

🛠️ Running Tests

To ensure the API is working correctly, run:

pytest tests/

✅ All tests should pass.

🔄 Continuous Integration (CI)

📝 GitHub Actions (.github/workflows/test.yml) runs pytest on every push to validate code.

📄 License

This project is licensed under the MIT License.

📩 Contact

For questions, reach out to:📧 Email: your-email@example.com🔗 GitHub: your-github-username

💪 Now you have a complete README.md for your project! 🚀 Let me know if you need modifications! 🔥
