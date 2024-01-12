# Newspaper

- Newspaper is a web application built using Django framework that allows users to upload articles and enables other users to comment on them.
- The project includes authentication and authorization features, ensuring that only the creator of a post can edit or delete it.
- It also includes functionality for user registration, login, logout, and email sending.

## Features

- Custom user model: Developer can config the user model.
- Testing: Tests for user app to make sure everything work well.
- User registration and authentication: Users can create accounts, log in, and log out of the system.
- Article creation and management: Authenticated users can upload articles and have full control over their own posts, including editing and deleting them.
- Commenting system: Users can leave comments on articles to engage in discussions.
- Email notifications: The project includes functionality for sending email notifications, such as account activation or password reset emails.

## Technologies Used

- Django: A high-level Python web framework used for building the backend of the application.
- Django's authentication system: Used for user registration, login, and logout.
- Django's authorization system: Implemented to handle user permissions and access control.
- Django's templating system: Used for rendering dynamic HTML templates.
- Sqlite: The project uses Sqlite as the database backend for data storage.
- HTML and Bootstrap: Used for frontend development and user interface design.
- Class-based generic views: Utilized for creating reusable and efficient views in Django.

## Setup Instructions

To set up the project locally, follow these steps:

1. Clone the repository:
   git clone <repository-url>
   
2. Install the project dependencies:
   pip install django-crispy-forms
   pip install django==4.2

   And make sure you have python version > 3.10
    
4. Configure the database settings in the `settings.py` file.

5. Apply database migrations:   
   python manage.py migrate

6. Run the development server:   
   python manage.py runserver

7. Access the application at `http://localhost:8000` in your web browser.

