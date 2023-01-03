import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn
def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
database='hw.db'

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity DOUBLE(10) NOT NULL DEFAULT 0
)
'''
def create_products(conn, products):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
def update_quantity(conn, products):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
def update_price(conn, products):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_products(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_limits(conn, price_limit, quantity_limit):
    try:
        sql = '''SELECT * FROM products WHERE price <= ? and quantity >= ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_product_title(conn, select):
    try:
        sql = '''SELECT * FROM products WHERE product_title = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (select,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


connection = create_connection(database)
if connection is not None:
    # create_table(connection, sql_create_products_table)
    # create_products(connection, ('Жидкое мыло с запахом ванили', 35.99, 30))
    # create_products(connection, ('Мыло детское', 39.99, 30))
    # create_products(connection, ('Масло сливочное', 199.99, 45))
    # create_products(connection, ('Сметана', 99.99, 45))
    # create_products(connection, ('Сервелат', 354.99, 50))
    # create_products(connection, ('Растишка', 69.99, 25))
    # create_products(connection, ('Чай гринфилд', 89.99, 85))
    # create_products(connection, ('Мармелад', 19.99, 35))
    # create_products(connection, ('Кофе', 199.99, 15))
    # create_products(connection, ('Яйца', 25.89, 84))
    # create_products(connection, ('Какао', 259.99, 55))
    # create_products(connection, ('Яблоки', 62.99, 57))
    # create_products(connection, ('Говядина', 699.99, 6))
    # create_products(connection, ('Курица', 399.99, 64))
    # create_products(connection, ('Мороженое', 69.99, 25))
    # update_quantity(connection, (85, 55))
    # update_price(connection, (70, 15))
    # delete_products(connection, 15)
    # select_products_by_limits(connection, 100, 50)
    # select_all_products(connection)
    select_products_by_product_title(connection, ('мыло'))
    print('Done')
    connection.close()