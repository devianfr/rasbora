from flask import Flask, jsonify, request, render_template
import sellorder
import buyorder
from profit import get_realized_profit
import modifyorder
import cancelorder

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
        data = request.json
        order_type = data.get("order_type", "LIMIT")
        limit_price = float(data.get("limit_price", 0))  # Default to 0 if not provided
        order_status = sellorder.fno_sell_order(order_type, limit_price)
        return jsonify({"status": "success", "order_status": order_status})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/modifyfno', methods=['POST'])
def modifyorderfno():
    try:
        order_status =modifyorder.modify_order()
        return jsonify({"status": "success", "order_status": order_status})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    
@app.route('/cancelallfno', methods=['POST'])
def cancelorderfno():
    try:
        order_status =cancelorder.cancel_order()
        return jsonify({"status": "success", "order_status": order_status})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route("/realized_profit", methods=["GET"])
def realized_profit():
    try:
        profit = get_realized_profit()
        
        # Ensure the return type is a proper JSON structure
        if isinstance(profit, (int, float)):  
            return jsonify({"status": "success", "realized_profit": profit})
        
        elif isinstance(profit, dict):  
            return jsonify(profit)  # If already a dict, return as-is
        
        else:  
            return jsonify({"status": "error", "message": "Invalid profit format"}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
