from flask import Flask, request, jsonify

app = Flask(__name__)
expenses = []

@app.route('/add', methods=['POST'])
def add_expense():
    data = request.json
    expenses.append(data)
    return jsonify({"message": "Added", "data": data})

@app.route('/view', methods=['GET'])
def view_expenses():
    return jsonify(expenses)

@app.route('/')
def home():
    return "Expense Tracker v2 - Add + View"

app.run(host='0.0.0.0', port=5000)