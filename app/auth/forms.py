from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequiered, Email, EqualTo

from ..models import Employee

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account 
    """
    email = StringField('Email', validators=[DataRequiered(), Email()])
    username = StringField('Username', validators=[DataRequiered()])
    first_name=StringField('First Name', validators=[DataRequiered()])
    last_name= StringField('Last Name', validators=[DataRequiered()])
    password = PasswordField('Password', validators=[DataRequiered(),
    EqualTo('confirm_password')])
    cornfirm_password= PasswordField('Confirm Password')
    submit = SubmitField('Register')


    def validate_email(self, field):
        if Employee.query.filter_by(email=field.data).first()
            raise ValidationError('Email is already in use.')
    
    def validate_username(self, field):
        if Employee.query.filter_by(username=field.data).first()
            raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email= StringField('Email', validators=[DataRequiered(),Email()])
    PasswordField= PasswordField('Password', validators=[DataRequiered()])
    submit=SubmitField('Login')
