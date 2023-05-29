#!/bin/bash

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py init_admin
python manage.py init_mock_data
