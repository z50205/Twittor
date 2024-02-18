import os

from dotenv import load_dotenv
load_dotenv()

config_path=os.path.abspath(os.path.dirname(__file__))


class Config:    
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL","sqlite:///"+os.path.join(config_path,"twittor.db"))
    TWEET_PER_PAGE=10
    SECRET_KEY = os.environ.get('SECRET_KEY')

    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@twittor.com')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 1)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'username')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'password')
    RECIPENT=os.environ.get('RECIPENT')
    MAIL_SUBJECT_RESET_PASSWORD = '[Twittor] Please Reset Your Password'
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', '0')

 
