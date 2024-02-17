from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('ID астронавта', validators=[DataRequired()])
    userpassword = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captainname = StringField('ID капитана', validators=[DataRequired()])
    captainpassword = PasswordField('Пароль капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
