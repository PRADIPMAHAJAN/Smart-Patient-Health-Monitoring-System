from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo


class RegistrationForm(FlaskForm):
    Username=StringField('Username',validators=[DataRequired()])
    email=StringField('Email    ',validators=[DataRequired(),Email()])
    Password = PasswordField('Password    ',validators=[DataRequired()])
    Confirm_Password=PasswordField('Confirm_Password',validators=[DataRequired(),EqualTo('Password')])
    Submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    Password = PasswordField('Password', validators=[DataRequired()])
    Submit = SubmitField('Login')