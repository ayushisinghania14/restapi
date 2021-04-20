from flask import Flask,jsonify

app = Flask(__name__)

items = [{'name': "top",'itemno':"4",'des':"blue"},
        {'name': "jeans",'itemno':"1",'des':"dark blue"},
        {'name': "dress",'itemno':"2",'des':"black"},
        {'name': "junksuit",'itemno':"5",'des':"multicolour"}]

cart = []

@app.route('/')
def index():
    return "!!WELCOME TO THE MISHKA'S SHOPPING!!"

#to view the items in the itemlist
@app.route("/items",methods=['GET'])
def show():
    return jsonify({'items':items})

#to view the items in the cart
@app.route("/cart",methods=['GET'])
def get():
    return jsonify({'items':cart})

#to view a particular item in the itemlist
@app.route("/items/<int:itemno>",methods=['GET'])
def get_item(itemno):
    return jsonify({'items':items[itemno]})

#adding item to the cart
@app.route("/cart",methods=['ADD'])
def create():
    item = {'name': "toppp",'itemno':"5",'des':"yellow"}
    cart.append(item)
    return jsonify({'created': item})

#To delete a particular item from the itemlist
@app.route("/items/<int:itemno>",methods=['DELETE'])
def delete(itemno):
    items.remove(items[itemno])
    return jsonify({'results':True})

#To delete  an item from the cart
@app.route("/cart/<int:cartno>",methods=['REMOVE'])
def ex(cartno):
    cart.remove(cart[cartno])
    return jsonify({'results':True})

if __name__ == "__main__":
    app.run(debug=True)
