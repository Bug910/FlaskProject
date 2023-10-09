from flask import Blueprint, render_template, request, redirect, url_for
from flaskPr.data.database import get_data, set_data

add_bp = Blueprint('add', __name__)


@add_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Обработайте отправленные данные для редактирования записи
        name = request.form['name']
        age = request.form['age']

        # Обновите запись в базе данных
        query = "insert into test_table(name,age) values('{}',{});".format(name, age)
        set_data(query)

        # Перенаправьте на главную страницу
        return redirect(url_for('main.index'))

    # Отобразите форму редактирования данных
    return render_template('add.html')


