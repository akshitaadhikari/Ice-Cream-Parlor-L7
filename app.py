import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def connect_db():
    """Establish a connection to the SQLite database."""
    return sqlite3.connect('icecream.db')

@app.route('/')
def index():
    """Provide a welcome message and list available endpoints."""
    return "Welcome to the Ice Cream Parlor API! Available endpoints: /flavors, /inventory, /suggestions, /allergies, /cart"

@app.route('/favicon.ico')
def favicon():
    """Handle requests for the favicon."""
    return "", 204

@app.route('/flavors', methods=['GET', 'POST'])
def manage_flavors():
    """Manage seasonal flavor offerings."""
    conn = connect_db()
    c = conn.cursor()

    if request.method == 'POST':
        name = request.json['name']
        season = request.json['season']
        c.execute('INSERT INTO flavors (name, season) VALUES (?, ?)', (name, season))
        conn.commit()
        return jsonify({'status': 'Flavor added'}), 201

    c.execute('SELECT * FROM flavors')
    flavors = c.fetchall()
    return jsonify(flavors)

@app.route('/inventory', methods=['GET', 'POST'])
def manage_inventory():
    """Manage ingredient inventory."""
    conn = connect_db()
    c = conn.cursor()

    if request.method == 'POST':
        ingredient = request.json['ingredient']
        quantity = request.json['quantity']
        c.execute('INSERT INTO inventory (ingredient, quantity) VALUES (?, ?)', (ingredient, quantity))
        conn.commit()
        return jsonify({'status': 'Ingredient added'}), 201

    c.execute('SELECT * FROM inventory')
    inventory = c.fetchall()
    return jsonify(inventory)

@app.route('/suggestions', methods=['POST'])
def add_suggestion():
    """Add customer flavor suggestions."""
    conn = connect_db()
    c = conn.cursor()

    flavor_suggestion = request.json['flavor_suggestion']
    customer_id = request.json['customer_id']
    c.execute('INSERT INTO suggestions (flavor_suggestion, customer_id) VALUES (?, ?)', (flavor_suggestion, customer_id))
    conn.commit()
    return jsonify({'status': 'Suggestion added'}), 201

@app.route('/allergies', methods=['GET', 'POST'])
def manage_allergies():
    """Manage customer allergy concerns."""
    conn = connect_db()
    c = conn.cursor()

    if request.method == 'POST':
        allergen = request.json['allergen']
        customer_id = request.json['customer_id']
        c.execute('INSERT INTO allergies (allergen, customer_id) VALUES (?, ?)', (allergen, customer_id))
        conn.commit()
        return jsonify({'status': 'Allergen added'}), 201

    c.execute('SELECT * FROM allergies')
    allergies = c.fetchall()
    return jsonify(allergies)

@app.route('/cart', methods=['GET', 'POST', 'DELETE'])
def manage_cart():
    """Manage cart operations."""
    conn = connect_db()
    c = conn.cursor()

    if request.method == 'POST':
        product = request.json['product']
        quantity = request.json['quantity']
        c.execute('INSERT INTO cart (product, quantity) VALUES (?, ?)', (product, quantity))
        conn.commit()
        return jsonify({'status': 'Product added to cart'}), 201

    if request.method == 'DELETE':
        product = request.json['product']
        c.execute('DELETE FROM cart WHERE product = ?', (product,))
        conn.commit()
        return jsonify({'status': 'Product removed from cart'}), 200

    c.execute('SELECT * FROM cart')
    cart = c.fetchall()
    return jsonify(cart)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
