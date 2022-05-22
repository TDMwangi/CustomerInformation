# Customer information
- Create a simple Django REST API which provides information about customers.
- Create a django management command to import the customers.csv file into your database.
- Create two extra fields for latitude and longitude and fill them up by customer's address using any Geolocation API.
- Implement a REST API with two endpoints, one for listing all customers and, another one for getting a single customer by its id.
- Create a simple web page to consume the REST API (you can use auto-documentation like djangoyasg).
## Installation
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Execute the geocoding management command with the following:
```sh
python3 manage.py geocoding
```
Execute the database management command with the following:
```sh
python3 manage.py postdb
```
Update the database with the following:
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
Start the web server:
```sh
python3 manage.py runserver
```
## Usage
To access the swagger API documentation navigate to:
```sh
http://localhost:8080/swagger
```
To access all customer information navigate to:
```sh
http://localhost:8080
```
To access individual customer information navigate to:
```sh
http://localhost:8000/{id}
```