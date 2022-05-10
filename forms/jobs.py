from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Работа', validators=[DataRequired()])
    work_size = IntegerField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Соавторы', validators=[DataRequired()])
    start_date = StringField('Дата старта')
    end_date = StringField('Дата конца')
    is_finished = BooleanField("Готово")
    submit = SubmitField('Подтвердить')