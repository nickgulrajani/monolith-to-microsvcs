from flask import Flask, jsonify, request, render_template
from models import db, Order, OrderItem, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('order.html')

@app.route('/orders')
def get_orders():
    orders = Order.query.all()
    order_list = []
    for order in orders:
        order_data = {
            'id': order.id,
            'customer_name': order.customer_name,
            'customer_email': order.customer_email,
            'order_date': order.order_date.isoformat(),
            'total_price': order.total_price,
            'items': []
        }
        for item in order.items:
            product_data = {
                'id': item.product.id,
                'name': item.product.name,
                'description': item.product.description,
                'price': item.price,
                'quantity': item.quantity
            }
            order_data['items'].append(product_data)
        order_list.append(order_data)
    return jsonify(order_list)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    customer_name = data.get('customer_name')
    customer_email = data.get('customer_email')
    product_ids = data.get('product_ids')
    quantities = data.get('quantities')

    # Calculate total price
    total_price = 0
    for i in range(len(product_ids)):
        product = Product.query.get(product_ids[i])
        if product:
            total_price += product.price * quantities[i]
        else:
            return jsonify({'error': 'Product not found'}), 404

    # Create order
    order = Order(customer_name=customer_name, customer_email=customer_email, total_price=total_price)
    db.session.add(order)

    # Create order items
    for i in range(len(product_ids)):
        product = Product.query.get(product_ids[i])
        if product:
            item = OrderItem(order=order, product=product, quantity=quantities[i], price=product.price)
            db.session.add(item)
        else:
            return jsonify({'error': 'Product not found'}), 404

    db.session.commit()

    order_data = {
        'id': order.id,
        'customer_name': order.customer_name,
        'customer_email': order.customer_email,
        'order_date': order.order_date.isoformat(),
        'total_price': order.total_price,
        'items': []
    }
    for item in order.items:
        product_data = {
            'id': item.product.id,
            'name': item.product.name,
            'description': item.product.description,
            'price': item.price,
            'quantity': item.quantity
        }
        order_data['items'].append(product_data)

    return jsonify(order_data), 201

if __name__ == '__main__':
    app.run(debug=True)

