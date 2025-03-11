from dhanhq import dhanhq
import stockiddata  # Import get_position function

client_id = stockiddata.client_id
access_token = stockiddata.access_token

dhan = dhanhq(client_id, access_token)

def modify_order():
    response = dhan.get_order_list()

    if not response or "data" not in response:
        print("Error: Failed to fetch orders")  # Print error to terminal
        return {"status": "error", "message": "Failed to fetch orders"}
    
    pending_order_id = None
    price=None
    trigger_price=None
    validity=None
    legName=None
    netQty=None
    for order in response["data"]:
        if order["orderStatus"] == "PENDING":
            pending_order_id = order["orderId"]
            price = order["price"]
            trigger_price = order["triggerPrice"]
            validity = order["validity"]
            legName =order["legName"]
            netQty= order["quantity"]
            break  # Exit loop after finding the first pending order
        
    if pending_order_id:
        print("Pending Order ID:", pending_order_id, price, trigger_price)
    else:
        print("No pending orders found")
        
    price += 1
    trigger_price +=1
    
    order = dhan.modify_order(
        order_id=pending_order_id, 
        order_type=dhan.SL, 
        quantity=netQty, 
        price=price, 
        trigger_price= trigger_price, 
        disclosed_quantity=0,
        validity=validity,
        leg_name=legName
        )
    print("new price",price,trigger_price)
      
    

    # Filter only pending orders