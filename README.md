# weather_api

Automatically create temperature/date and work with it via API endpoints.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing


* Create a virtualenv for the project
* Install the requirements.txt file with pip


```
pip install -r requirements.txt
```
* Create Postgresql db corresponding to settings.py

* Create dummy data via command:

```
python manage.py setup_test_data
```

* Run the django server

```
python ./manage.py runserver
```

* Enjoy the site at 127.0.0.1:8000 or your corresponding localhost

---
### Dummy data
The amount of dummy data can be changed via parameter in `temperature/management/commands/setup_test_data.py`, specifically:
```
...
NUM_TEMPERATURES = 50
...
```

### Api endpoints
YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
```

```