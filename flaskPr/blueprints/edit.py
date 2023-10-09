from flask import Blueprint, render_template, request, redirect, url_for
from flaskPr.data.database import get_data, set_data

edit_bp = Blueprint('edit', __name__)


@edit_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # Получите данные из базы данных по id
    query = 'SELECT * FROM test_table WHERE id = {}'.format(id)
    result = get_data(query)
    data = {'id': result[0][0], 'name': result[0][1], 'age': result[0][2]}

    if request.method == 'POST':
        # Обработайте отправленные данные для редактирования записи
        name = request.form['name']
        age = request.form['age']

        # Обновите запись в базе данных
        query = "UPDATE test_table SET name = '{}', age = {} WHERE id = {};commit".format(name, age, id)
        set_data(query)

        # Перенаправьте на главную страницу
        return redirect(url_for('main.index'))

    # Отобразите форму редактирования данных
    return render_template('edit.html', data=data)
