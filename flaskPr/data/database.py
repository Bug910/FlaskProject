import psycopg2

db_host = 'localhost'
db_port = 5432
db_name = 'postgres'
db_user = 'postgres'
db_password = '1234'

conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)


def get_data(query):
    with conn.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()

    return data


def set_data(query):
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()
