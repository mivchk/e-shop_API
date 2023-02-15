from flask import Flask, request
import psycopg2

app = Flask(__name__)


@app.route("/api/product_all")
def get_all():
    with psycopg2.connect(dbname="postgres", user="postgres", password="mysecretpassword", host="127.0.0.1",
                          port="5433") as conn:
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM Goods")

        result = cursor.fetchall()
    return result


@app.route('/api/<get_id>', methods=['GET'])
def hello_world(get_id):  # put application's code here
    with psycopg2.connect(dbname="postgres", user="postgres", password="mysecretpassword", host="127.0.0.1",
                          port="5433") as conn:
        cursor = conn.cursor()

        cursor.execute(f"SELECT name, price FROM Goods WHERE id={get_id}")

        result = cursor.fetchall()
    return result


@app.route('/api/add', methods=['POST'])
def add_product():
    name_add = str(request.form['name_add'])
    price_add = int(request.form['price_add'])
    with psycopg2.connect(dbname="postgres", user="postgres", password="mysecretpassword", host="127.0.0.1",
                          port="5433") as conn:

        cursor = conn.cursor()

        cursor.execute("insert into goods (name, price) values (%s, %s) returning name",
                       (name_add, price_add))

    return 'Done!'


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        result = a + b
        return f'{a} + {b} = {result}'
    return f'Был получен {request.method} запрос.'


if __name__ == '__main__':
    app.run(debug=True)
