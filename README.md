*Employee Management System*

Project Overview
----------------

This project is a Django-based Employee Management System that allows user authentication and dynamic form creation for employee records. The system enables users to log in, create employees, and manage them efficiently using dynamic, customizable forms.

Features

1. Authentication & Profile
---------------------------

Login: Secure user authentication.

Register: New users can register.

Change Password: Users can reset their password.

Profile: Manage user profile information.

2). Employee Management
-----------------------

Form Design

Create and edit customizable forms with various field types (Number, Text, Date, Password, etc.).

Add new sections dynamically using an "Add Field" button.

Implement drag-and-drop functionality to rearrange form sections.

3).Employee Creation & Update
-----------------------------

Use a pre-designed form to create employee records.

Ensure dynamic input fields reflect in employee records.

Handle form submissions using AJAX or Axios (without Django form actions).

4).Employee Listing
-------------------

Display a list of employee records.

Implement search and filter functionality based on dynamic fields.

Allow users to delete employee records as needed.


Setup Instructions
------------------

git clone https://github.com/yourusername/employee-management-system.git
cd employee-management-system

Access the Application
----------------------

Login: http://127.0.0.1:8000/accounts/login/

Admin Panel: http://127.0.0.1:8000/admin/


*) Technologies Used
--------------------

Backend: Django, Django ORM

Frontend: HTML, CSS, JavaScript, Bootstrap

AJAX / Axios: For dynamic form handling

Database: SQLite
