import sqlite3

con = sqlite3.connect("online_shop.db")
cursor = con.cursor()
cursor.executescript("""
CREATE TABLE if not exists Categories(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT,
    number_of_products_in_stock INTEGER
    );
    
CREATE TABLE if not exists Products(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT,
    product_name TEXT,
    product_size INTEGER,
    product_quantity INTEGER,
    price DOUBLE(5, 2),
    FOREIGN KEY(category_name) REFERENCES Categories(category_name)
    );

CREATE TABLE if not exists Users(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    email TEXT,
    password TEXT,
    age INTEGER CHECK(age > 18),
    phone_number TEXT,
    address TEXT,
    country TEXT
    );
    
CREATE TABLE if not exists Cart(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    category_name TEXT,
    product_name TEXT,
    product_size INTEGER,
    product_quantity INTEGER,
    price NUMERIC DECIMAL (5,2),
    total NUMERIC GENERATED ALWAYS AS (price * product_quantity) VIRTUAL,
    discount INTEGER,
    total_after_discount NUMERIC GENERATED ALWAYS AS (price * product_quantity -price * product_quantity * discount) VIRTUAL,
    FOREIGN KEY(category_name) REFERENCES Categories(category_name),
    FOREIGN KEY(product_name) REFERENCES Categories(product_name)
    );

CREATE TABLE if not exists Carts(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    category_name TEXT,
    product_name TEXT,
    product_size INTEGER,
    product_quantity INTEGER,  
    FOREIGN KEY(user) REFERENCES Users(user)
    );
    
CREATE TABLE if not exists Recent_views(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    category_name TEXT,
    product_name TEXT,
    product_size INTEGER,
    FOREIGN KEY(user) REFERENCES Users(user)
    );
""")
cursor.execute("SELECT * FROM Categories")
print(cursor.fetchall())
cursor.execute("SELECT * FROM Products")
print(cursor.fetchall())
cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())
cursor.execute("SELECT * FROM Cart")
print(cursor.fetchall())
cursor.execute("SELECT * FROM Carts")
print(cursor.fetchall())
cursor.execute("SELECT * FROM Recent_views")
print(cursor.fetchall())

cursor.execute("INSERT INTO Categories (category_name, number_of_products_in_stock) VALUES('Topo equipments', 150)")
cursor.execute("INSERT INTO Categories (category_name, number_of_products_in_stock) VALUES('Scan equipments', 90)")
cursor.execute("INSERT INTO Categories (category_name, number_of_products_in_stock) VALUES('Winter gear', 101)")
cursor.execute("INSERT INTO Categories (category_name, number_of_products_in_stock) VALUES('Accessories', 200)")

cursor.execute("SELECT * FROM Categories")
print(cursor.fetchall())

products = [
    ("Topo equipments", "Rover System GPS Hi-Target vRTK", "130mm diameter, 80mm height", 1, 2600.00),
    ("Topo equipments", "Rover System GPS Hi-Target V200", "132 mm x 67 mm", 1, 3000.00),
    ("Topo equipments", "Total station Hi-Target HTS 420R", "-", 1, 2400.00)
    ]


SQL_query = "INSERT INTO Products (category_name, product_name, product_size, product_quantity, price) VALUES (?,?,?,?,?)"
cursor.executemany(SQL_query, products)
cursor.execute("SELECT * FROM Products")
print(cursor.fetchall())
con.commit()

