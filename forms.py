from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField(
        label = "Username", 
        validators = [DataRequired(), Length(min = 2, max = 20)]
    )
    email = StringField(
        label = "Email", 
        validators = [DataRequired(), Email()]
    )
    password = PasswordField(
        label = "Password", 
        validators = [DataRequired(), Length(min = 8, max = 50)]
    )
    confirm_password = PasswordField(
        label = "Confirm Password", 
        validators = [
            DataRequired(), Length(min = 8, max = 50), EqualTo("password")
        ]
    )
    submit = SubmitField(label = "Sign Up")

class LoginForm(FlaskForm):
    email = StringField(
        label = "Email", 
        validators = [DataRequired(), Email()]
    )
    password = PasswordField(
        label = "Password", 
        validators = [DataRequired(), Length(min = 8, max = 50)]
    )
    remember = BooleanField(label = "Remember Me")
    submit = SubmitField(label = "Log In")