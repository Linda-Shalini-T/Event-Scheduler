Event Scheduler & Resource Allocation System

📌 Project Description

The Event Scheduler & Resource Allocation System is a web-based application developed using Flask and SQLAlchemy that enables users to create events, manage shared resources, allocate resources to events, and automatically detect scheduling conflicts.

The system is designed to handle overlapping events, prevent double-booking of resources, and provide clear visibility of resource utilization across different time ranges. This makes it suitable for academic institutions, training centers, and organizations managing shared facilities or equipment.

🛠️ Technologies Used

Backend: Python, Flask
Frontend: HTML, CSS, Bootstrap, Jinja2
Database: SQLite
ORM: SQLAlchemy
Version Control: Git
Environment: Virtualenv

⚙️ Installation Instructions

Follow the steps below to set up the project locally.

1️⃣ Clone the Repository

2️⃣ Create and Activate Virtual Environment
    python -m venv venv
    venv\Scripts\activate

3️⃣ Install Dependencies
    pip install -r requirements.txt

4️⃣ Database Setup
    flask db init
    flask db migrate
    flask db upgrade

▶️ How to Run the Application
    python run.py
Open your browser and visit:
    http://127.0.0.1:5000
    
✨ Features Implemented

🔹 Event Management
     Create, view, edit, and delete events
     Support for overlapping event time windows

🔹 Resource Management
     Create and manage shared resources
     Resource types (Room, Equipment, Instructor, etc.)

🔹 Resource Allocation
     Assign multiple resources to a single event
     Prevent duplicate or conflicting allocations

🔹 Conflict Detection
     Automatically detects resource conflicts
     Displays clear error messages when conflicts occur

🔹 Conflict Dashboard
     View all conflicting resource allocations in one place

🔹 Utilization Report
     Displays resource usage across different date ranges
     Helps analyze resource efficiency

🗄️ Database Schema

+---------------------+
|       Event         |
+---------------------+
| event_id (PK)       |
| title               |
| start_time          |
| end_time            |
| description         |
+---------------------+

+---------------------+
|      Resource       |
+---------------------+
| resource_id (PK)    |
| resource_name       |
| resource_type       |
+---------------------+

+-----------------------------------+
| EventResourceAllocation           |
+-----------------------------------+
| id (PK)                           |
| event_id (FK → Event.event_id)    |
| resource_id (FK → Resource.id)    |
+-----------------------------------+

Screenshot & video are in github
[text](https://drive.google.com/file/d/1WxMxbh8hlrE-IJwXZSR0oLQMrmRx4kwH/view?usp=drivesdk)
