from flask import Blueprint, render_template, flash, redirect, url_for

from webapp.calculation.forms import DataSetForm
from webapp.calculation.models import UserDataSet
from webapp.db import db

blueprint = Blueprint('calculations', __name__, url_prefix='/calculation')

'''
@blueprint.route('/')
def index():
    title = 'Расчёт модели'
    calculations_list = UserDataSet.query.order_by(UserDataSet.published.desc()).all()
    return render_template('calculation/index.html', page_title=title, calculations_list=calculations_list)
'''

@blueprint.route('/process-dataset', methods=['POST'])
def process_dataset():
    form = DataSetForm()
    if form.validate_on_submit():
        new_data = UserDataSet(name_of_the_feature=form.name_of_the_feature.data, frequency_1=form.frequency_1.data,
                               frequency_2=form.frequency_2.data)
        db.session.add(new_data)
        db.session.commit()
        flash('Можете вводить следующие данные.')
        return redirect(url_for('calculation.inputdata'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле {}: {}'.format(
                    getattr(form, field).label.text, error))
        return redirect(url_for('calculation.inputdata'))
