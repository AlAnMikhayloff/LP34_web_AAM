from flask import Blueprint, render_template
from webapp.db import db
from webapp.calculations.models import UserDataSet

blueprint = Blueprint('calculations', __name__)


@blueprint.route('/')
def index():
    title = 'Расчёт модели'
    calculations_list = UserDataSet.query.order_by(UserDataSet.published.desc()).all()
    return render_template('calculations/index.html', page_title=title, weather=weather, calculations_list=calculations_list)

@blueprint.route('/process-dataset', methods=['POST'])
def process_dataset():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле {}: {}'.format(
                    getattr(form, field).label.text, error))
        return redirect(url_for('user.register'))
