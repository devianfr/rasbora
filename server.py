from flask import Flask, jsonify, request, render_template
import sellorder
import buyorder

app = Flask(__name__, static_folder='dashboard', template_folder='dashboard')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/buyfno', methods=['POST'])
def buyorderfno():
    try:
        data = request.json
        order_type = data.get("order_type", "LIMIT")
        limit_price = float(data.get("limit_price", 0))  # Default to 0 if not provided
        order_status = buyorder.fno_buy_order(order_type, limit_price)
        return jsonify({"status": "success", "order_status": order_status})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/sellfno', methods=['POST'])
def sellorderfno():
    try:
        data = request.json  # ✅ Extract JSON data
        if not data:
            return jsonify({"status": "error", "message": "Invalid request data"}), 400

        order_type = data.get("order_type", "LIMIT")
        limit_price = float(data.get("limit_price", 0))

        order_status = sellorder.fno_sell_order(order_type, limit_price)  # ✅ Pass values properly
        return jsonify({"status": "success", "order_status": order_status})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/modify', methods=['POST'])
def modifyorderfno():
    try:
        response = sellorder.modify_order()
        return jsonify({"status": "success", "message": response})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
