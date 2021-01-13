from flask import Flask
import json

app = Flask(__name__)

with open('data/products.json') as f:
    products = json.load(f)


@app.route('/products')
def get_products():
    """Return all products"""
    return json.dumps(products, indent = 4)   

@app.route('/products/<int:product_id>')
def get_product(product_id):
    """Return all orders"""
    return json.dumps([product for product in products['products'] if product['id'] == str(product_id)], indent = 4)   

   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
