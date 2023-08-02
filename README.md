# DataPilot

The DataPilot is a web application developed using the Django web framework. It provides users with a simple web-based interface to execute SQL queries and view the results. The application includes user authentication, and user-specific database assignment to ensure a secure and personalized experience. However, each user can have only one database for the time being.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication: Register, login, and logout functionality.
- User-specific database assignment: Each user is assigned a unique database file for executing SQL queries.
- SQL Query Execution: Execute SQL queries and view the results in a tabular format.
- Error handling: Informative error messages for invalid queries or potential issues.

## Technologies Used

- Python: The programming language used for backend development.
- Django: The web framework responsible for request handling and application management.
- SQLite: The database management system used to store user data.
- django-allauth: A package for user authentication and email verification.
- HTML/CSS: Markup and styling languages for the user interface.

## Getting Started

### Installation

1. Make sure you have Python installed on your system. If not, download and install it from the official website: https://www.python.org/downloads/

2. Clone this repository to your local machine:

```bash
git clone https://github.com/arindam-sahoo/datapilot.git
cd datapilot
```

3. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
```

4. Activate the virtual environment (Windows):

```bash
.\.venv\Scripts\activate
```

4. Activate the virtual environment (macOS/Linux):

```bash
source .venv/bin/activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the Application

1. Create the SQLite database and apply migrations:

```bash
python manage.py migrate
```

2. Start the development server:

```bash
python manage.py runserver
```

3. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

1. Register a new account using your email address and password.
3. Upon successful authentication, you will be redirected to the DataPilot dashboard.
4. Enter your SQL queries in the provided textarea and click "Execute" to see the results.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.