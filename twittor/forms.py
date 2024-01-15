from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired
=======
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,Length
from twittor.models import User
>>>>>>> 0.6

class Loginform(FlaskForm):
    username=StringField("username",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    remember_me=BooleanField("Remember me")
<<<<<<< HEAD
    submit =SubmitField('SignIn')
=======
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
        
class EditProfileform(FlaskForm):
    about_me=TextAreaField('About me',validators=[Length(min=0,max=120)])
    submit=SubmitField('save')
>>>>>>> 0.6
