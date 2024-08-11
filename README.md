# todo-app-django
simple todo app with login and registration using django and SQLite
## Overview
This repository contains the frontend code for the To-Do application. It includes login,register and todo html files that implement the core user interface and functionality.
# Demo
**login page**

![WhatsApp Image 2024-08-11 at 15 49 53_960878a0](https://github.com/user-attachments/assets/1103872f-49be-4a9a-b7f5-e8b8808d6b26)

**register page**

![WhatsApp Image 2024-08-11 at 15 49 53_5c072c91](https://github.com/user-attachments/assets/fdbd0ac8-ca92-465c-a78d-8502fd3d33af)

**todo page**

![WhatsApp Image 2024-08-11 at 15 49 53_fd823ed7](https://github.com/user-attachments/assets/f69f9d58-9f6f-4ebf-85eb-ae8cb75a4a4e)


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
4. **Create virtual envoronment**(Make sure that pipenv is installed)
       ```sh
          python -m pipenv
          python -m pipenv shell
       ```
     ```
6. **Apply migrations**:
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
