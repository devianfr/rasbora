from flask import Flask, jsonify, request, render_template
import sell_fno

app = Flask(__name__, static_folder='dashboard', template_folder='dashboard')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sell', methods=['POST'])
def sell():
    try:
        order_id = sell_fno.place_sell_order()
        return jsonify({"status": "success", "order_id": order_id})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/modify', methods=['POST'])
def modify():
    try:
        response = sell_fno.modify_order()
        return jsonify({"status": "success", "message": response})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
