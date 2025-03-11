from dhanhq import dhanhq
import stockiddata

client_id = stockiddata.client_id
access_token = stockiddata.access_token
securityId = stockiddata.securityId

dhan = dhanhq(client_id, access_token)



def fno_sell_order(order_type="LIMIT", limit_price=0):
    
    global securityId
    
    # ------------------------------------------------------------------- get quantity data from position 
    
    response = dhan.get_positions()

    if not response or "data" not in response:
        print("Error: Failed to fetch orders")  # Print error to terminal
        return {"status": "error", "message": "Failed to fetch orders"}
    
    
    buynetQty=None
    for order in response["data"]:
        if ((order["positionType"] == "LONG") and (order["exchangeSegment"] == "NSE_FNO")):
            buynetQty = order["netQty"]
            break  # Exit loop after finding the first pending order
    
    # -----------------------------------------------------------------------------  Do not modify anything below works fine 
    
    
    # ------------------------------------------------------------------------------sets the limit and trigger price  
    
    # Determine order type dynamically
    order_type_enum = dhan.MARKET if order_type == "MARKET" else dhan.SL

    limit_price = limit_price + 1
    # Calculate trigger price only if it's a LIMIT order
    trigger_price = limit_price + 0.20 if order_type == "LIMIT" else 0
    
    #-----------------------------------------------------------------------------------place order

    order = dhan.place_order(
        security_id=securityId,
        exchange_segment=dhan.NSE_FNO,
        transaction_type=dhan.SELL,
        quantity=buynetQty,
        order_type=order_type_enum,
        product_type=dhan.INTRA,
        price=limit_price if order_type == "LIMIT" else 0,  # No price for MARKET orders
        trigger_price=trigger_price  # No trigger for MARKET orders
    )

    order_status = order.get('data', {})
    return order_status if order_status else "Order placement failed"
    