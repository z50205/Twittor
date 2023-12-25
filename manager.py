from flask import Flask
from flask.cli import AppGroup
from twittor import create_app

app=create_app()
manager = AppGroup(app)

if __name__ == "__main__":
    app.run()