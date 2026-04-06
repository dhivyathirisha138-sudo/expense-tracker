from flask import Flask, request, jsonify

app = Flask(__name__)

# Store expenses in a list
expenses = []

# Home route
@app.route('/')
def home():
    return "Expense Tracker v2 Running"

# 1️⃣ Add Expense
@app.route('/add', methods=['POST'])
def add_expense():
    data = request.get_json()
    
    expense = {
        "name": data.get("name"),
        "amount": data.get("amount")
    }
    
    expenses.append(expense)
    
    return jsonify({"message": "Expense added successfully", "data": expense})

# 2️⃣ View Expenses
@app.route('/view', methods=['GET'])
def view_expenses():
    return jsonify(expenses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)