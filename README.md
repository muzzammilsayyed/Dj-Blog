
---

# Django Blog Project

## Overview

This is a Django-powered blog website that allows users to browse, search, and interact with blog posts. The project includes core features such as a search functionality, a contact form with validation, and a dynamic content management system.

## Features

- **Home Page:** Displays the latest blog posts.
- **About Page:** Provides information about the blog.
- **Contact Page:** Users can submit messages through a contact form with validation.
- **Search Functionality:** Users can search for blog posts by keywords.
- **Post Management:** Blog posts are dynamically managed using Django’s templating system.

## Technologies Used

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript (Jinja templating)
- **Database:** SQLite (or your preferred database system)


## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/django-blog-project.git
   cd django-blog-project
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser to access the Django admin panel:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Home Page:** Displays recent blog posts.
- **About Page:** Information about the blog and its purpose.
- **Contact Page:** Users can send messages through the contact form.
- **Search:** Use the search bar to find blog posts by title.




