from flask_wtf import FlaskForm

from webapp.calculation.models import UserDataSet

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class DataSetForm(FlaskForm):
    name_of_the_feature = StringField('Наименование показателея', validators=[DataRequired()],
                                      render_kw={"class": "form-control"})
    n_samples = StringField('Общее количество баллов', validators=[DataRequired()], render_kw={"class": "form-control"})
    n_features = StringField('Набранные баллы', validators=[DataRequired()], render_kw={"class": "form-control"})
    applicant = StringField('Претендент', render_kw={"class": "form-control"})
    submit = SubmitField('Добавить', render_kw={"class": "btn btn-success"})
    submit1 = SubmitField('Остановить', render_kw={"class": "btn btn-danger"})

    def validation_frequency_1(self, n_samples):
        frequency_count = UserDataSet.query.filter_by(n_samples=n_samples.data).count()
        if frequency_count is not int:
            raise ValidationError('Введите, пожалуйста, целое число')

    def validation_frequency_2(self, n_features):
        frequency_count = UserDataSet.query.filter_by(n_features=n_features.data).count()
        if frequency_count is not int:
            raise ValidationError('Введите, пожалуйста, целое число')