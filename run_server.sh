#!/bin/sh


set FLASK_APP=manager.py
flask db migrate
flask db upgrade
gunicorn --bind=0.0.0.0:8000 --log-level info --workers 4 twittor.wsgi:application