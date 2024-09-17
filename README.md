
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

## Development Tools

Tools for ensuring code quality:

- **mccabe**, **pycodestyle**, **pyflakes** – used for linting and identifying errors in the code. Run the linter with the following command:

    ```bash
    pycodestyle <your-python-files>
    ```

