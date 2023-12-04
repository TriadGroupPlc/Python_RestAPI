# This is a sample Python Project which aims at introducing Rest API with the help
# of a customer Form
# Write Customer
# Read Customer
# Get all customers
# with some simple Validations

from flask import Flask, jsonify, request

import getCustomer
import readAllCustomers
import saveCustomer


# Flask is one of the way to create Rest APIs in python
app = Flask(__name__)

customers = []
file = 'resources/Customers.json'


@app.route("/saveCustomer", methods=['POST'])
def save_customer():
    return saveCustomer.save_customer(request.get_json(), file), 200


@app.route('/getAllCustomer')
def get_customers():
    return jsonify(readAllCustomers.read_all_customer(file))


@app.route("/getCustomer", methods=['GET'])
def get_customer():
    df = getCustomer.get_customer(int(request.args['reference']), file)
    return df.to_json(orient='records'), 200
