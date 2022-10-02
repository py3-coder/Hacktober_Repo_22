from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,BooleanField,IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from se_hackethon_project.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4)])
    password_confirm = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(name=username.data).first()
        if user:
            raise ValidationError("This username has already been taken. Please choose a different one!!!")

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("This email already exits in our database. Please choose a different one!!!")

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class AccountUpdateForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Update Account')

    def validate_username(self,username):
        user = User.query.filter_by(name=username.data).first()
        if username.data != current_user.name:
            if user:
                raise ValidationError("This username has already been taken. Please choose a different one!!!")

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if email.data != current_user.email:
            if user:
                raise ValidationError("This email already exits in our database. Please choose a different one!!!")

class RequestResetForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(),Email()])
    submit = SubmitField('Request Password Reset')
    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError("There is no account with that email. Register First!!!!")


class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Reset Password')

class SuggestionForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Suggestion in Detail',validators=[DataRequired()])
    submit = SubmitField('Submit Request')


class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content',validators = [DataRequired()])
    picture = FileField('Upload Post Pic',validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Post')

class HelpForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content',validators = [DataRequired()])
    submit = SubmitField('Post')
