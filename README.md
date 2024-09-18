
# Newspaper Agency Service

A Django-based web application that helps manage newspapers, topics, and editors. The project includes content creation and management features, as well as Bootstrap integration for a user-friendly interface.

## Installation

### 1. Clone the repository:

```bash
git clone git@github.com:GGsosna/newspaper-agency-service.git
cd newspaper-agency-service
```

### 2. Create a virtual environment:

- **For Windows:**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

- **For macOS/Linux:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 3. Install dependencies:

Run the following command to install all required packages:

```bash
pip install -r requirements.txt
```

### 4. Configure the environment:

Create a `.env` file in the root directory of the project and add the required environment variables:

```bash
SECRET_KEY=your-secret-key
DATABASES_URL = "here is the URL of your database"
```

#### Generating a SECRET_KEY:

You can generate a secret key for Django using Python:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated key and add it to the `.env` file:

```bash
SECRET_KEY="your-generated-secret-key"
```

### 5. Apply database migrations:

Run the migrations to initialize the database:

```bash
python manage.py migrate
```

### 6. Run the development server:

Once the database is set up, run the development server:

```bash
python manage.py runserver
```

## Usage

After starting the server, go to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser. Log in or register to access the application’s features.

## Running Tests

To run tests in your Django project, use the following command:

```bash
python manage.py test
```

## Demo
Login page:
![Demo of the Newspaper Agency Service](
https://private-user-images.githubusercontent.com/105813721/367844001-a271493d-6718-4d47-9923-6e18eca39468.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjY2NzE1NTIsIm5iZiI6MTcyNjY3MTI1MiwicGF0aCI6Ii8xMDU4MTM3MjEvMzY3ODQ0MDAxLWEyNzE0OTNkLTY3MTgtNGQ0Ny05OTIzLTZlMThlY2EzOTQ2OC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxOFQxNDU0MTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yNzBhZGQ1ZTFlYmFlMTE2YzUyZGI0YjFhMzY0ZjZiNWZmMmNmOWE1NmY4NDFmMTJkNzlmMTUwYTRmMGJiZDU2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.wU0qk8Bu9wNTBXnFRKcGrFhItfUl0P_VMo3dbZlSDCw)

Home page:
![Demo of the Newspaper Agency Service](https://private-user-images.githubusercontent.com/105813721/367844268-2721469f-672c-4384-8ee1-9e3760816e37.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjY2NzE1NTIsIm5iZiI6MTcyNjY3MTI1MiwicGF0aCI6Ii8xMDU4MTM3MjEvMzY3ODQ0MjY4LTI3MjE0NjlmLTY3MmMtNDM4NC04ZWUxLTllMzc2MDgxNmUzNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxOFQxNDU0MTJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wM2ZmN2I2ZmU3ZWM5ZGYyYzYxOGZjNTJhOWI3MThlYjJiZGExN2E0ZmIyZDhlMzNhZDhlODc4YWZhNWZmYWQ5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Jn4OdRREPTt44euZL_KBtxLZObeFzB0M3xES_h2d2c8)

Topic list page:
![Demo of the Newspaper Agency Service](https://private-user-images.githubusercontent.com/105813721/367853623-d209abf0-fc48-413a-9090-3c7f8612d411.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjY2NzIwNTgsIm5iZiI6MTcyNjY3MTc1OCwicGF0aCI6Ii8xMDU4MTM3MjEvMzY3ODUzNjIzLWQyMDlhYmYwLWZjNDgtNDEzYS05MDkwLTNjN2Y4NjEyZDQxMS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwOTE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDkxOFQxNTAyMzhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MjI0N2MzMGNhZTU5YmEwZTZmNTRhM2M4ZGZlYThjMDZiMWE3YTdlMWYwN2VlMGJlOTAzN2YyYjI1MjRmNDNhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.ZyEE7gZrrArxcqOrDHT1KufDxJDVy-K2zgiVfve4flk)


## Development Tools

Tools for ensuring code quality:

- **mccabe**, **pycodestyle**, **pyflakes** – used for linting and identifying errors in the code. Run the linter with the following command:

    ```bash
    pycodestyle <your-python-files>
    ```

