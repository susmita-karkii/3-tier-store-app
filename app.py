from flask import Flask, render_template, request, jsonify
from businesslogic import ProductLogic

app = Flask(__name__)
product_logic = ProductLogic()

@app.route('/buy', methods=['POST'])
def buy():
    data = request.get_json()
    first_name = data['firstName']
    last_name = data['lastName']
    product_name = data['productName']

    product_logic.insert_product(first_name, last_name, product_name)

    return jsonify({'message': 'Purchase successful'})

@app.route('/show', methods=['GET'])
def show():
    purchases = product_logic.get_purchases()

    return jsonify(purchases)

@app.route('/purchaseHistory', methods=['POST'])
def purchase_history():
    data = request.get_json()
    full_name = data['fullName']

    history = product_logic.get_purchase_history(full_name)

    return jsonify(history)

if __name__ == '__main__':
    app.run()
def index():
    return render_template('index.html')
