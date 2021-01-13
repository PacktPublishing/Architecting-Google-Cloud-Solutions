from flask import Flask
import json

app = Flask(__name__)

with open('data/orders.json') as f:
    orders = json.load(f)

@app.route('/orders')
def get_orders():
    """Return all orders"""
    return json.dumps(orders, indent = 4)   

@app.route('/orders/<int:order_id>')
def get_order(order_id):
    """Return all orders"""
    return json.dumps([order for order in orders['orders'] if order['id'] == str(order_id)], indent = 4)   
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)