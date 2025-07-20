# 🐍 Django Notes 

Welcome to my Django learning journey! This note contains **theoretical concepts**, **installation steps**, and **basic project setup** — perfect for beginners!

---

## 📖 What is Django?

Django is a **high-level Python web framework** that allows developers to build robust, scalable, and secure web applications quickly and efficiently.

### 🧠 Key Features of Django:

- Follows **MVT architecture** (Model - View - Template)
- Comes with built-in **admin panel**
- Handles **authentication**, **URL routing**, **ORM**, and more
- Highly **secure**, **scalable**, and **batteries included**

---

## 🏗️ Django Architecture – MVT

| Component | Description |
|----------|-------------|
| **Model** | Deals with database. Defines the structure of data. |
| **View**  | Contains the business logic and communicates with Models and Templates. |
| **Template** | Handles the front-end: HTML, CSS, and dynamic data rendering. |

---
<img width="265" height="645" alt="Screenshot 2025-07-20 170951" src="https://github.com/user-attachments/assets/dd8410fe-7f53-4c03-9779-ec2b8099b7c4" />

## ⚙️ Prerequisites

Make sure you have Python installed:

```bash
python --version
# 1. Create a virtual environment
python -m venv env

# 2. Activate the virtual environment
# For Linux/macOS:
source env/bin/activate
# For Windows:
env\Scripts\activate

# 3. Install Django
pip install django

# 4. Create a new Django project
django-admin startproject myproject

# 5. Navigate into the project directory
cd myproject

# 6. Run the development server
python manage.py runserver



