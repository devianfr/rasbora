from dhanhq import dhanhq
import stockiddata  # Import get_position function

client_id = stockiddata.client_id
access_token = stockiddata.access_token

dhan = dhanhq(client_id, access_token)

def cancel_order():
    response = dhan.get_order_list()

    if not response or "data" not in response:
        print("Error: Failed to fetch orders")  # Print error to terminal
        return {"status": "error", "message": "Failed to fetch orders"}
    
    pending_order_id = None

    for order in response["data"]:
        if order["orderStatus"] == "PENDING":
            pending_order_id = order["orderId"]
            break  # Exit loop after finding the first pending order
        
    if pending_order_id:
        print("canceled order:", pending_order_id)
    else:
        print("No pending orders found")

    order = dhan.cancel_order(
        order_id=pending_order_id
        )
