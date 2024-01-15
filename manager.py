from flask import Flask
<<<<<<< HEAD
from flask.cli import AppGroup
from twittor import create_app

app=create_app()
manager = AppGroup(app)

if __name__ == "__main__":
    app.run()
=======
from flask.cli import FlaskGroup
from flask_migrate import Migrate
from twittor import create_app, db
from twittor.models import User


app = create_app()
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)

cli=FlaskGroup(app)

if __name__ == "__main__":
    cli()
>>>>>>> 0.6
