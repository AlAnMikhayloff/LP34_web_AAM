from flask import Blueprint, flash, redirect, render_template, url_for

from webapp.calculation.forms import DataSetForm
from webapp.calculation.models import UserDataSet
from webapp.db import db

blueprint = Blueprint('calculation', __name__, url_prefix='/calculations')


@blueprint.route('/')
def index():
    title = 'Расчёт модели'
    return render_template('calculation/index.html', page_title=title, form=DataSetForm())


@blueprint.route('/process-dataset', methods=['POST'])
def process_dataset():
    form = DataSetForm()
    if form.validate_on_submit():
        new_data = UserDataSet(name_of_the_feature=form.name_of_the_feature.data, frequency_1=form.frequency_1.data,
                               frequency_2=form.frequency_2.data)
        db.session.add(new_data)
        db.session.commit()
        flash('Можете вводить следующие данные.')
        return redirect(url_for('calculation.index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле {}: {}'.format(getattr(form, field).label.text, error))
        return redirect(url_for('calculation.index'))
