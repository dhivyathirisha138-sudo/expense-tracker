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

@app.route('/total', methods=['GET'])
def total():
    total_amount = sum(item['amount'] for item in expenses)
    return jsonify({"total": total_amount})

@app.route('/')
def home():
    return "Expense Tracker v3 - Full Features"

app.run(host='0.0.0.0', port=5000)