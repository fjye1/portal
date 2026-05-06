from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, TextAreaField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email, Length


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()], render_kw={"autocomplete": "username"})
    password = PasswordField("Password", validators=[DataRequired()],render_kw={"autocomplete": "current-password"})
    submit = SubmitField("Let Me In!")
    
    
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[
        DataRequired(), 
        Length(min=8)
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    
class ProjectForm(FlaskForm):
    title = StringField(
        "Project Title",
        validators=[DataRequired(), Length(min=2, max=200)]
    )
    description = TextAreaField(
        "Description",
        validators=[Length(max=1000)]
    )
    # choices populated at request time in the route, not here
    user_id = SelectField("Assign to User", coerce=int, default=0)

    submit = SubmitField("Create Project")