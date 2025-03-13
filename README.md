# Standoff 2 Case Opening

A case-opening project for the game Standoff 2, developed in Python using Django.

## Description

This project allows users to open virtual cases with items from the Standoff 2 game. It features a spinning animation system, Django admin panel for data management, and database integration for storing item information and drop rates.

## Features

- User registration and authentication
- Case opening with spinning animation
- User inventory management
- Database connection for storing skins data
- Logging and drop analytics

## Technologies

- Python 3.x
- Django
- PostgreSQL
- HTML, CSS, JavaScript

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/jamshid6573/Standuz.git
```

2. Navigate to the project directory:

```bash
cd standoff2-case-opening
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # for Linux
venv\Scripts\activate  # for Windows
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Configure the database in `settings.py`.

6. Apply migrations:

```bash
python manage.py migrate
```

7. Run the development server:

```bash
python manage.py runserver
```

The project will be available at `http://127.0.0.1:8000`

## License
[MIT License](LICENSE)

## Contact

If you have any questions or suggestions, contact me at: [jamshid125200@gmail.com](mailto:jamshid125200@gmail.com)
