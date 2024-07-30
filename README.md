# todo-app-django
simple todo app with login and registration using django and SQLite
## Overview
This repository contains the frontend code for the To-Do application. It includes login,register and todo html files that implement the core user interface and functionality.

## File Structure
  **--> login.html** : It contains the html&css code for the login page of the todo app which asks  for the username and password.
  
  **--> register.html** : It contains the html and css code for the registration page which asks for  the username,email and password.
  
  **--> todo.html :** It contains the html,css and script code of todo app which adds the task with due date ,deletes the task and also marks the task as complete.It is also have the logout button to logout.

## Getting Started
1. **Clone the repository**:
    ```sh
    git clone https://github.com/pranathi1703/todo-app-django.git
    ```
2. **Navigate to the project directory**:
    ```sh
    cd todo\todoprj
    ```
3. **Install dependencies**:
     ```sh
       pip install -r requirements.txt
     ```
5. **Apply migrations**:
     ```sh
        python manage.py makemigrations
        python manage.py migrate
     ```
7. **Run the development server**:
     ```sh
        python manage.py runserver
     ```
    **Access the application at http://127.0.0.1:8000/ in your web browser.**


## Development
To contribute or modify the code, please follow best practices for HTML, CSS, and JavaScript development.

## License
This project is licensed under the MIT License.
