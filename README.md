# Usermanagement

## Requirements
* Python 3.4+
* PostgreSQL 9.6+
* Linux/Unix OS
* Pipenv
## Setup
* Project dependencies are managed by `Pipenv`[https://pipenv.pypa.io/en/latest/]. Install Pipenv using `pip3 install pipenv` 
* Go to the project library and run `pipenv sync`
* Create database and update your the database name, username and password in `.env` file
* Run `pipenv run python manage.py runserver` to start the development server
* Open your browser and go to `localhost:8000/api/users/`

## Running Tests
* Open command terminal and run  `pipenv run python manage.py test`