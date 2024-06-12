import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('icecream.db')
c = conn.cursor()

# Create tables if they don't exist
c.execute('''CREATE TABLE IF NOT EXISTS flavors (
                id INTEGER PRIMARY KEY,
                name TEXT,
                season TEXT
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY,
                ingredient TEXT,
                quantity INTEGER
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS suggestions (
                id INTEGER PRIMARY KEY,
                flavor_suggestion TEXT,
                customer_id INTEGER,
                FOREIGN KEY (customer_id) REFERENCES customers (id)
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS allergies (
                id INTEGER PRIMARY KEY,
                allergen TEXT,
                customer_id INTEGER,
                FOREIGN KEY (customer_id) REFERENCES customers (id)
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )''')

# Insert fabricated data into the tables
flavors = [
    ('Vanilla', 'Summer'),
    ('Chocolate', 'Winter'),
    ('Strawberry', 'Spring'),
    ('Mint', 'Summer'),
    ('Pumpkin Spice', 'Autumn'),
    ('Gingerbread', 'Winter')
]

inventory = [
    ('Milk', 200),
    ('Sugar', 100),
    ('Vanilla Beans', 50),
    ('Cocoa Powder', 30),
    ('Strawberries', 25),
    ('Mint Leaves', 20),
    ('Pumpkin Puree', 15),
    ('Gingerbread Spice', 10)
]

customers = [
    ('Alice Smith', 'alice@example.com'),
    ('Bob Johnson', 'bob@example.com'),
    ('Charlie Brown', 'charlie@example.com'),
    ('Dana White', 'dana@example.com'),
    ('Evan Davis', 'evan@example.com')
]

suggestions = [
    ('Blueberry', 1),
    ('Cookie Dough', 2),
    ('Salted Caramel', 3),
    ('Matcha', 4),
    ('Lemon', 5)
]

allergies = [
    ('Peanuts', 1),
    ('Gluten', 2),
    ('Dairy', 3),
    ('Soy', 4),
    ('Tree Nuts', 5)
]

c.executemany('INSERT INTO flavors (name, season) VALUES (?, ?)', flavors)
c.executemany('INSERT INTO inventory (ingredient, quantity) VALUES (?, ?)', inventory)
c.executemany('INSERT INTO customers (name, email) VALUES (?, ?)', customers)
c.executemany('INSERT INTO suggestions (flavor_suggestion, customer_id) VALUES (?, ?)', suggestions)
c.executemany('INSERT INTO allergies (allergen, customer_id) VALUES (?, ?)', allergies)

# Commit changes and close connection
conn.commit()
conn.close()
