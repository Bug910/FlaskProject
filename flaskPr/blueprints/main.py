from flask import Blueprint, render_template, request
from flaskPr.data.database import get_data

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    # Получите параметры страницы и фильтра из URL
    page = int(request.args.get('page', 1))
    per_page = 40  # Количество элементов на странице
    filter_id = request.args.get('filter_id')

    # Определите SQL-запрос для получения данных
    query = 'SELECT * FROM test_table'
    if filter_id:
        query += ' WHERE id = {}'.format(filter_id)
    query += ' ORDER BY id DESC'

    # Выполните SQL-запрос
    result = list(map(lambda x: {'id': x[0], 'name': x[1], 'age': x[2]}, get_data(query)))

    # Создайте объект пагинации, только если данные не помещаются на одной странице
    total = len(result)
    if total <= per_page:
        pagination = None
    else:
        pagination = get_pagination(page=page, per_page=per_page, total=total)

    # Отфильтруйте данные для текущей страницы
    offset = (page - 1) * per_page
    paginated_data = result[offset: offset + per_page]

    # Отобразите таблицу с данными и пагинацией
    return render_template('index.html', data=paginated_data, pagination=pagination, filter_id=filter_id)


@main_bp.route('/run_function', methods=['POST'])
def run_function():
    # Ваш код функции, которую нужно выполнить
    return 'Function executed successfully!'


def get_pagination(page, per_page, total):
    pagination = {}

    # Вычислите общее количество страниц
    total_pages = total // per_page + (total % per_page > 0)

    # Определите предыдущую и следующую страницу
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < total_pages else None

    # Определите список страниц для отображения в пагинации
    # В примере отображается максимум 5 страниц вокруг текущей страницы
    start_page = max(page - 1, 1)
    end_page = min(page + 1, total_pages)
    page_list = list(range(start_page, end_page + 1))

    pagination['prev_page'] = prev_page
    pagination['next_page'] = next_page
    pagination['page_list'] = page_list

    return pagination
