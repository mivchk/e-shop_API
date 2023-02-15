import psycopg2

if __name__ == "__main__":
    with psycopg2.connect(dbname="postgres", user="postgres", password="mysecretpassword", host="127.0.0.1", port="5433") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Goods")

        result = cursor.fetchall()

        print(result)

