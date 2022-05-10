from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, IntegerField, BooleanField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Пароль повторение', validators=[DataRequired()])
    surname = StringField('Фамилия')
    name = StringField('Никита')
    age = IntegerField('Возраст')
    position = StringField('Позиция')
    speciality = StringField('Специализация')
    address = TextAreaField("Адрес")
    submit = SubmitField('Готово')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Готово')