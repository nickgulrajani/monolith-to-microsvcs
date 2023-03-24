from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def get_products():
    # Retrieve product information from the database
    products = [
        {'id': 1, 'name': 'Product 1', 'description': 'Description 1', 'price': 10.0, 'vendor': 'Vendor 1'},
        {'id': 2, 'name': 'Product 2', 'description': 'Description 2', 'price': 20.0, 'vendor': 'Vendor 2'},
        {'id': 3, 'name': 'Product 3', 'description': 'Description 3', 'price': 30.0, 'vendor': 'Vendor 3'}
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

