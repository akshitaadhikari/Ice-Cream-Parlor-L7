# Ice Cream Parlor API

## Overview
This is a simple API for an Ice Cream Parlor, allowing management of seasonal flavors, inventory, customer suggestions, allergies, and cart operations.

## Prerequisites
- Python 3.8+
- Flask
- SQLite

## Setup Instructions
### Steps to Run

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_name>
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Initialize the database:
    ```sh
    python init_db.py
    ```

4. Run the application:
    ```sh
    python app.py
    ```

5. Access the application at `http://127.0.0.1:5001`.

### Docker Setup
1. **Build the Docker Image**
    ```sh
    docker build -t icecream-parlor .
    ```

2. **Run the Docker Container**
    ```sh
    docker run -p 5001:5001 icecream-parlor
    ```

3. **Access the Application**
    Open your browser and go to `http://127.0.0.1:5001`

## API Endpoints

- **GET /**: Welcome message and list of available endpoints
- **GET /flavors**: List all flavors
- **POST /flavors**: Add a new flavor
- **GET /inventory**: List all inventory items
- **POST /inventory**: Add a new inventory item
- **POST /suggestions**: Add a new flavor suggestion
- **GET /allergies**: List all allergies
- **POST /allergies**: Add a new allergy
- **GET /cart**: List all cart items
- **POST /cart**: Add an item to the cart
- **DELETE /cart**: Remove an item from the cart

## Testing Instructions
1. **Test Flavors Endpoint**
    - Add a new flavor:
    ```sh
    curl -X POST http://127.0.0.1:5001/flavors -H "Content-Type: application/json" -d '{"name": "Vanilla", "season": "Summer"}'
    ```

    - Get all flavors:
    ```sh
    curl http://127.0.0.1:5001/flavors
    ```

2. **Test Inventory Endpoint**
    - Add a new inventory item:
    ```sh
    curl -X POST http://127.0.0.1:5001/inventory -H "Content-Type: application/json" -d '{"ingredient": "Milk", "quantity": 10}'
    ```

    - Get all inventory items:
    ```sh
    curl http://127.0.0.1:5001/inventory
    ```

3. **Test Suggestions Endpoint**
    - Add a new suggestion:
    ```sh
    curl -X POST http://127.0.0.1:5001/suggestions -H "Content-Type: application/json" -d '{"flavor_suggestion": "Mango", "customer_id": 1}'
    ```

4. **Test Allergies Endpoint**
    - Add a new allergy:
    ```sh
    curl -X POST http://127.0.0.1:5001/allergies -H "Content-Type: application/json" -d '{"allergen": "Peanuts", "customer_id": 1}'
    ```

5. **Test Cart Endpoint**
    - Add an item to the cart:
    ```sh
    curl -X POST http://127.0.0.1:5001/cart -H "Content-Type: application/json" -d '{"product": "Ice Cream", "quantity": 2}'
    ```

    - Remove an item from the cart:
    ```sh
    curl -X DELETE http://127.0.0.1:5001/cart -H "Content-Type: application/json" -d '{"product": "Ice Cream"}'
    ```

## SQL Queries

### Create Tables
```sql
CREATE TABLE flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    season TEXT
);

CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT,
    quantity INTEGER
);

CREATE TABLE suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_suggestion TEXT,
    customer_id INTEGER
);

CREATE TABLE allergies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    allergen TEXT,
    customer_id INTEGER
);

CREATE TABLE cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER
);
