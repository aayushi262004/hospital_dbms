Hospital Management System (DBMS Project)

📌 Project Overview

This is a web-based Hospital Patient Management System built using Flask (Python Web Framework) and Oracle Database. The system allows users to Add, Update, Delete, and View patient information in a secure and efficient manner.

🏗️ Tech Stack

Frontend: HTML (via Jinja2 templates rendered by Flask)

Backend: Python (Flask Framework)

Database: OracleDB (Express Edition)

✅ Features

Add new patient records

Update existing patient data

Delete patient records

View all registered patients in a tabular format

Automatic column detection and table creation during initialization

🌐 HTTP Methods Used

Method

Routes

Purpose

GET

/, /patients, /update_patient/<id>

Display pages and retrieve data

POST

/add_patient, /delete_patient/<id>, /update_patient/<id>

Submit form data for insert, delete, or update operations

🧠 SQL Methods Used

SQL Command

Purpose

CREATE TABLE

Creates the PATIENTS table if it does not exist

ALTER TABLE

Adds columns like gender, doctor, etc. if missing

SELECT

Fetches columns or patient data

INSERT INTO

Adds new patient data

UPDATE

Modifies patient records

DELETE FROM

Removes patient record by ID

TO_DATE()

Converts string input to Oracle DATE

TO_CHAR()

Converts DATE to string for form rendering

🐍 Flask / Python Functions Used

Function / Method

Purpose

@app.route()

Binds URL paths to specific Python functions

render_template()

Loads HTML templates with dynamic content

request.form[]

Retrieves submitted form field values

redirect()

Redirects user to another route after form actions

url_for()

Generates URLs dynamically using route names

try/except

Handles errors gracefully

conn.cursor()

Prepares SQL statements via Oracle DB cursor

cursor.execute()

Executes SQL queries

conn.commit()

Commits changes to the DB

cursor.fetchone()

Retrieves one row of result

cursor.fetchall()

Retrieves all rows from a query

cursor.close() / conn.close()

Closes DB connection properly

⏳ Date Handling Methods

Tool

Purpose

datetime.strptime()

Converts string (from form) to Python datetime object

TO_DATE() (Oracle)

Converts string to Oracle-compatible DATE

TO_CHAR() (Oracle)

Formats DATE to string for display in forms

📂 Folder Structure

project/
├── app.py                # Main Flask app
├── templates/
│   ├── index.html
│   ├── patients.html
│   └── update_patient.html
└── static/               # (Optional) CSS/JS files

🏁 How to Run the Project

Install dependencies:

pip install flask oracledb

Run the app:

python app.py

Open browser and visit: http://localhost:5000

✍️ Author

This project was developed as part of a Database Management System (DBMS) coursework to demonstrate integration between Flask web apps and Oracle DB for CRUD operations.

