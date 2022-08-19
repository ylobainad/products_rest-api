from crypt import methods
from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"message": "Product's list", "products": products})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    for product in products:
        if product["name"] == product_name:
            return jsonify({"product":product})
        else:
            return jsonify({"message": "Product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.get_json()["name"],
        "price": request.get_json()["price"],
        "quantity": request.get_json()["quantity"]
        }
    products.append(new_product)
    return jsonify({"message": "Product added successfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editeProduct(product_name):

    data = request.get_json()

    name = data["name"]
    price = data["price"]
    quantity = data["quantity"]

    for product in products:
        if product["name"] == product_name:
            product["name"] = name
            product["price"] = price
            product["quantity"] = quantity
            return jsonify({"message": "Product update succesfully", "products":product})

    return jsonify({"message": "Product not found"}), 400

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):

    for product in products:
        if product["name"] == product_name:
            products.remove(product)
            return jsonify({"message": "Product deleted", "products":product})

    return jsonify({"message": "Product not found"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)