from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/orders', methods=['POST'])
def create_order():
    # Retrieve product information from the Product Catalog Service
    product_id = request.json['product_id']
    # Call Product Catalog Service API to retrieve product information
    product_info = {'id': product_id, 'name': 'Product 1', 'description': 'Description 1', 'price': 10.0, 'vendor': 'Vendor 1'}
    
    # Create a new order
    order = {'customer_name': request.json['customer_name'], 'product_info': product_info, 'status': 'New'}
    # Save order information to the database
    
    return jsonify(order)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

