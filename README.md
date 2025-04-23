# Django REST API with JWT Authentication and Task Management

This project is a RESTful API built with Django and Django REST Framework (DRF), using a custom user model with JWT authentication via `djangorestframework-simplejwt`.

---

## 🚀 Features

- User registration with strong password validation
- JWT-based login, token refresh, and logout (blacklisting)
- Secure user profile endpoint
- Task CRUD (Create, Read, Update, Delete) per authenticated user
- Permissions to ensure users can only manage their own tasks

---

## 🛠 Setup Instructions

### 1. Clone the Repository
git clone https://github.com/cole15sky/Interview-Task.git
cd mytask

### 2. Create a Virtual Environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Apply Migrations & Create Superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 5. Run the Development Server
python manage.py runserver


