from flask import Blueprint, flash, redirect, render_template, url_for

from flask_login import current_user

from webapp.calculation.forms import DataSetForm
from webapp.calculation.models import UserDataSet
from webapp.db import db

blueprint = Blueprint('calculation', __name__, url_prefix='/calculations')


@blueprint.route('/')
def index():
    title = 'Расчёт модели'
    form = DataSetForm()
    return render_template('calculation/index.html', page_title=title, form=form)


@blueprint.route('/process-dataset', methods=['POST'])
def process_dataset():
    form = DataSetForm()
    if form.validate_on_submit():
        new_data = UserDataSet(name_of_the_feature=form.name_of_the_feature.data, n_samples=form.n_samples.data,
                               n_features=form.n_features.data, applicant=form.applicant.data, user_id=current_user.id)
        db.session.add(new_data)
        db.session.commit()
        flash('Можете вводить следующие данные.')
        return redirect(url_for('calculation.index'))
    elif form.validate_on_submit1():
        flash('Данные сохранены, сейчас будет результат. Благодарим за ожидание.')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле {}: {}'.format(getattr(form, field).label.text, error))
        return redirect(url_for('calculation.index'))
