from flask import Flask, request, jsonify

app = Flask(__name__)

expenses = []

# Home
@app.route('/')
def home():
    return "Expense Tracker v3 Running"

# Add Expense
@app.route('/add', methods=['POST'])
def add_expense():
    data = request.get_json()
    expense = {
        "name": data.get("name"),
        "amount": data.get("amount")
    }
    expenses.append(expense)
    return jsonify({"message": "Added", "data": expense})

# View Expenses
@app.route('/view', methods=['GET'])
def view_expenses():
    return jsonify(expenses)

# ✅ NEW FEATURE (v3)
# Total Expense
@app.route('/total', methods=['GET'])
def total_expense():
    total = sum(item["amount"] for item in expenses)
    return jsonify({"total": total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)