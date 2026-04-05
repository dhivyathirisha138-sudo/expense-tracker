from flask import Flask, request, jsonify

app = Flask(__name__)
expenses = []

@app.route('/add', methods=['POST'])
def add_expense():
    data = request.json
    expenses.append(data)
    return jsonify({"message": "Expense added", "data": data})

@app.route('/')
def home():
    return "Expense Tracker v1 - Add only"

app.run(host='0.0.0.0', port=5000)