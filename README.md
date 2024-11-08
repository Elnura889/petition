# Petition API Project

This is a simple API project for managing petitions. The API allows user registration, login, petition creation, voting, and filtering petitions. User authentication is handled using JWT (JSON Web Tokens).

## Prerequisites

1. **Python 3.8 or higher**
2. **PostgreSQL** - Ensure PostgreSQL is installed and running on your system.
3. **Git** - To clone the repository.

## Installation

Follow these steps to set up and run the project:

### Step 1: Clone the Repository

```bash
git clone https://github.com/Elnura889/petition.git
cd petition

### Set Up a Virtual Environment
Create a virtual environment and activate it:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### Install Dependencies
Install the required libraries:
```bash
pip install -r requirements.txt
```

### Database Setup
1. **Create a PostgreSQL Database**:
   - Start PostgreSQL and create a new database, e.g., `petition_db`.

2. **Configure Database Connection** in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'petition_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Migrations
Create and apply migrations for the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser
Create an admin account to access the admin interface:
```bash
python manage.py createsuperuser
```

### Run the Server
Start the development server:
```bash
python manage.py runserver
```

### Access the API
Open your browser and go to:
```plaintext
http://127.0.0.1:8000
```

## Testing the API
You can test the API through Swagger (if configured) or using tools like Postman.
```plaintext
http://127.0.0.1:8000/api/schema/swagger-ui/
```

### Example Requests:
- **Get All Petitions**:
  ```http
  GET /api/petitions/
  ```

- **Create a New Petition**:
  ```http
  POST /api/petitions/
  Content-Type: application/json

  {
      "title": "New Petition",
      "description": "Description of the petition."
  }
  ```

- **Vote for a Petition**:
  ```http
  POST /api/votes/
  Content-Type: application/json

  {
      "petition": 1
  }
  ```

