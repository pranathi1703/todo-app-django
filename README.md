# todo-app-django
simple todo app with login and registration using django
## Overview
This repository contains the frontend code for the To-Do application. It includes login,register and todo files that implement the core user interface and functionality.

## File Structure
  **--> login.html** : It contains the html&css code for the login page of the todo app which asks the username and password.
  **--> register.html** : It contains the html and css code for the registration page which asks the username,email and password.
  **--> todo.html :** It contains the html,css and script code of todo app which adds the task with due date ,deletes the task and marks the task as complete of the user .It is also have the logout button to logout.

## Getting Started
1. **Clone the repository**:
    ```sh
    git clone https://github.com/pranathi1703/todo-app-django.git
    ```
2. **Navigate to the project directory**:
    ```sh
    cd tpg/todo/todoprj/todoapp/templates/todoapp
    ```
3. **Install dependencies**:
       pip install -r requirements.txt
4. **Apply migrations**:
        python manage.py makemigrations
        python manage.py migrate
5. **Run the development server**:
        python manage.py runserver
    **Access the application at http://127.0.0.1:8000/ in your web browser.**


## Development
To contribute or modify the code, please follow best practices for HTML, CSS, and JavaScript development.

## License
This project is licensed under the MIT License.
