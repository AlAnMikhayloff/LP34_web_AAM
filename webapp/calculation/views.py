import csv
import sqlite3

from flask import Blueprint, flash, redirect, render_template, url_for

from flask_login import current_user

import numpy as np

import pandas as pd

from sklearn.naive_bayes import GaussianNB

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
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле {}: {}'.format(getattr(form, field).label.text, error))
        return redirect(url_for('calculation.index'))


@blueprint.route('/process-export-csv', methods=['GET'])
def process_export_csv():
    
    # Подключение к базе данных SQLite

    conn = sqlite3.connect('webapp.db')
    cursor = conn.cursor()

    # Выполнить SQL-запрос

    cursor.execute('SELECT * FROM user_data_set WHERE user_id=?', (current_user.id,))
    data = cursor.fetchall()

    # Записать данные в CSV-файл

    with open(f'output{current_user.id}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])  # Write header
        writer.writerows(data)  # Write data rows

    # Закрыть подключение к базе

    conn.close()
    flash('Данные сохранены, можете приступать к расчёту.')
    return redirect(url_for('calculation.index'))


@blueprint.route('/engine', methods=['GET'])
def engine():
    df = pd.read_csv(f"output{current_user.id}.csv")

    result = list([i, j] for i, j in zip(df.iloc[:, 2].to_list(), df.iloc[:, 3].to_list()))
    result1 = list(df.iloc[:, 4].to_list())

    X = np.array(result)
    Y = np.array(result1)

    clf = GaussianNB()
    clf.fit(X, Y)
    flash('Сейчас будет результат:')
    # return clf.predict([[10, 7]])
    clf_pf = GaussianNB()
    clf_pf.partial_fit(X, Y, np.unique(Y))
    # return redirect(url_for('calculation.index'))
    answer = int(clf_pf.predict([[10, 5]]))
    # flash('Преимущество у претендента №', {answer})
    flash(f'С большой долей вероятнсти можно отдать предпочтение претенденту № {answer}')
    return render_template('calculation/engine.html', answer=answer)


@blueprint.route('/answer_NB', methods=['POST'])
def answer_nb():
    pass   # flash('Преимущество у претендента № {}', format.getattr(engine.answer_nb))
