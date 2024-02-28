# 💽 Local

1. Clone or download the repository.
2. Create a virtual environment and install requirements from requirements.txt file.
3. Create an **.env** file or rename **.env.example** in **.env** and populate it **only with development variables**
4. Make migrations:
    * `python src/manage.py migrate`
5. Create user:
    * `python src/manage.py createsuperuser`
6. Download data from the link:
    * `python src/manage.py update_currency_parser`
7. Upload data manually:
    * `python src/manage.py update_currency_console <name> <rate>`
8. Run development server:
    * `python src/manage.py runserver`


# 🌄 Demonstration

1. Authenticate using the link by sending a request to http://127.0.0.1:8000/token
```shell
  http://127.0.0.1:8000/token
  POST
  {
    "username":
    "password":
  }
```
2. Сopy the access token and paste it in all requests in headers
```shell
  "Authorization": Bearer ...
```
3. Send a get request to http://127.0.0.1:8000/currencies to get a list of all currencies
4. Send a get request to http://127.0.0.1:8000/currency/<id> to get a currency with id=id