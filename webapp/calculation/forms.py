from flask_wtf import FlaskForm

from webapp.calculation.models import UserDataSet

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class DataSetForm(FlaskForm):
    name_of_the_feature = StringField('Наименование показателея', validators=[DataRequired()],
                                      render_kw={"class": "form-control"})
    frequency_1 = StringField('Частота КП1', validators=[DataRequired()], render_kw={"class": "form-control"})
    frequency_2 = StringField('Частота КП2', default=True, render_kw={"class": "form-control"})
    probability_1 = StringField('Вероятность КП1', render_kw={"class": "form-control"})
    probability_2 = StringField('Вероятность КП2', render_kw={"class": "form-control"})
    submit = SubmitField('Добавить', render_kw={"class": "btn btn-success"})

    def validation_frequency_1(self, frequency_1):
        frequency_count = UserDataSet.query.filter_by(frequency_1=frequency_1.data).count()
        if frequency_count is not int:
            raise ValidationError('Введите, пожалуйста, целое число')

    def validation_frequency_2(self, frequency_2):
        frequency_count = UserDataSet.query.filter_by(frequency_2=frequency_2.data).count()
        if frequency_count is not int:
            raise ValidationError('Введите, пожалуйста, целое число')
