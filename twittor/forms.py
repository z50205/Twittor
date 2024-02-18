from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,MultipleFileField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,Length
from twittor.models.user import User

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
        
class EditProfileform(FlaskForm):
    about_me=TextAreaField('About me',validators=[Length(min=0,max=120)])
    submit=SubmitField('save')


class Tweetform(FlaskForm):
    tweet=TextAreaField('Tweet',validators=[DataRequired(),Length(min=0,max=140)])
    submit=SubmitField('Tweet')


class PasswdResetRequestForm(FlaskForm):
    email=TextAreaField('Email Address',validators=[DataRequired(),Email()])
    submit=SubmitField('Reset Password')

    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError(
                'You do not have an account for this email address'
            )

class PasswdResetForm(FlaskForm):
    password1=PasswordField('password1',validators=[DataRequired()])
    password2=PasswordField('password2',validators=[DataRequired(),EqualTo('password1')])
    submit=SubmitField('Reset Password')

class UpLoadForm(FlaskForm):
    files = MultipleFileField('File(s) Upload')