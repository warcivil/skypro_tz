#!/bin/bash

python manage.py makemigrations
python manage.py migrate

python manage.py loaddata sky_api/fixtures/load_data.json


python manage.py runserver 0.0.0.0:8000