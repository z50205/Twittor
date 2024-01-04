from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError
from twittor.models import User

class Loginform(FlaskForm):
    username=StringField("username",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    remember_me=BooleanField("Remember me")
    submit =SubmitField('SignIn')

class Registerform(FlaskForm):
    username=StringField("username",validators=[DataRequired()])
    email=StringField("Email Address",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    password2=PasswordField("Password Repeat",validators=[DataRequired(),EqualTo('password')])
    submit =SubmitField('Register')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('please use different username!!!')
        
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('please use different email!!!')