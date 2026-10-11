import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT,
    price REAL,
    quantity INTEGER
)
""")

conn.commit()
conn.close()

print("Database and Table Created Successfully!")


def add_product(product_id, product_name, category, price, quantity):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO products
    (product_id, product_name, category, price, quantity)
    VALUES (?, ?, ?, ?, ?)
    """, (product_id, product_name, category, price, quantity))
    print("Product Added Successfully!")

    conn.commit()
    conn.close()

    

def view_products():
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        conn.close()
        return products

def update_product(product_id, product_name, category, price, quantity):
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()

        cursor.execute("""
    UPDATE products
    SET product_name = ?, category = ?, price = ?, quantity = ?
    WHERE product_id = ?
    """, (product_name, category, price, quantity, product_id))

        conn.commit()
        conn.close()

def delete_product(product_id):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))

    conn.commit()
    conn.close()

def search_product(product_name):
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()

        cursor.execute(
           "SELECT * FROM products WHERE product_name LIKE ?",
           ('%' + product_name + '%',)
    )

        products = cursor.fetchall()

        conn.close()
        return products

def low_stock():
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products WHERE quantity < 10")
        products= cursor.fetchall()

        conn.close()
        return products

def dashboard():
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM products")
        total_products = cursor.fetchone()[0]

        cursor.execute("SELECT SUM(quantity) FROM products")
        total_quantity = cursor.fetchone()[0]

        cursor.execute("SELECT SUM(price * quantity) FROM products")
        total_value = cursor.fetchone()[0]

        conn.close()

        if total_quantity is None:
           total_quantity = 0

        if total_value is None:
           total_value = 0

        return total_products, total_quantity, total_value