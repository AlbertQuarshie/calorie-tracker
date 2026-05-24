# Daily Calorie Counter

## A. Contributor

- **Albert Junior Quarshie**

---

## B. Overview

- **Daily Calorie Counter** is a responsive web application built with Django. It allows users to log their food intake, track their total daily calories, and view their eating history in real-time.

- The backend is powered by Python and Django to handle the app's core logic, while a PostgreSQL database is used to securely save and store all your food items and tracking logs.

- The frontend interface uses Tailwind CSS instead of Bootstrap, creating a clean, modern, single-page design that automatically resizes to look great on both smartphones and computers.

---
## C. Requirements
- These are the required applications you need to have installed in your computer:

1.  Python 3.14 or later.
---
2.  Postgresql version 18.4 or later.

-Here are the download links if you don't have them installed:
```bash
https://www.python.org/downloads/
```



```bash
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
```
---

## D. Installation

- Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/AlbertQuarshie/calorie-tracker
cd calorie-tracker
```

### 2. Set Up Virtual Environment
- Create and activate an isolated Python environment to keep dependencies separate from your global system:


```bash
# Windows Users
python -m venv my_env
my_env\Scripts\activate

# macOS/Linux Users
python3 -m venv my_env
source my_env/bin/activate
```

### 3. Install Dependencies
- Install all required software versions simultaneously using the project's requirements:

```bash
pip install django
pip install psycopg2-binary
```

### 4. Setup Database Configurations
- Ensure a physical local relational database instance named calorie_tracker is active in your PostgreSQL system.

- Open calorie_tracker_project/settings.py and modify the default credential fields inside the DATABASES configuration mapping to match your local database instance management rules:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'calorie_tracker',
        'USER': 'your_postgres_username',      # Replace with your local PG username
        'PASSWORD': 'your_postgres_password',  # Replace with your local PG database password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
### 5. Run Database Migrations
- Apply the structural database schema layout directly onto your PostgreSQL instance tracking container matrices:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Installation Complete
- Now the application is ready for usage.



---


## E. Usage
### 1. Launch the Application
- Access the local environment engine execution routine by visiting the address in your browser:
```Bash
python manage.py runserver
```

### 2. Log Food Entries
- Input a food name and its corresponding calorie count value into the main entry header, then submit the form to add it to the database matrix.

### 3. Remove Logged Records
- Click the corresponding action control element next to any row to dynamically invoke item deletion logic, updating summary statistics in real time.

### 4. Clear Daily Metric Progress
- Use the dedicated dashboard control button to purge all tracking log metadata records matching the active calendar time window, resetting calculations immediately to zero.
---
## F. Features
### 1. Calorie Tracking Logic
- Simple inputs for adding precise food item definitions mapped together with corresponding nutritional metrics.

### 2. Real-Time Metric Aggregation
- Automatic parsing of food entries inside the current date criteria loop to present an accurate total summation score.

### 3. Targeted Data Deletion
- Secure route workflows utilizing get_object_or_404 validation to eliminate specific row items by ID without interrupting database consistency.

### 4. Single-Action Workspace Refresh
- Bulk item deletion logic targeting exclusively today's entries to clear the user dashboard without altering historic data.

### G. Security & CSRF Protections
- Implementation of secure form parsing patterns that natively enforce Cross-Site Request Forgery ({% csrf_token %}) validation checks.
---
## H. Tech Stack
- These are the technologies implemented in the creation of this project:


| **Layer**             | **Technology**       |
| --------------------- | -------------------- |
| Environment           | Python 3.14.4        |
| Web App Framework     | Django               |
| Database              | Postgresql           |
| User Interface        | HTML                 |
| Styling Component     |  Tailwind            |  
