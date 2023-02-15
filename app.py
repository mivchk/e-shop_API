from flask import Flask, request
import psycopg2

app = Flask(__name__)


@app.route("/api/product_all") # Эндпоинт возвращает все значения таблицы "товары"
def get_all():
    with psycopg2.connect(dbname="postgres", user="postgres", password="mysecretpassword", host="127.0.0.1",
                          port="5433") as conn:
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM Goods")

        result = cursor.fetchall()
    return result


@app.route('/api/<get_id>', methods=['GET']) # Эндпоинт возвращает позицию из таблицы с продуктами с необходимым id
def hello_world(get_id):
    with psycopg2.connect(dbname="postgres", user="postgres", password="mysecretpassword", host="127.0.0.1",
                          port="5433") as conn:
        cursor = conn.cursor()

        cursor.execute(f"SELECT name, price FROM Goods WHERE id={get_id}")

        result = cursor.fetchall()
    return result


@app.route('/api/add', methods=['POST']) # Эндпоинт позволяет добавить
def add_product():
    name_add = str(request.form['name_add'])
    price_add = int(request.form['price_add'])
    with psycopg2.connect(dbname="postgres", user="postgres", password="mysecretpassword", host="127.0.0.1",
                          port="5433") as conn:

        cursor = conn.cursor()

        cursor.execute("insert into goods (name, price) values (%s, %s) returning name",
                       (name_add, price_add))

    return 'Done!'


if __name__ == '__main__':
    app.run(debug=True)
