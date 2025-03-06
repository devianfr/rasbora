from dhanhq import dhanhq
import stockiddata

client_id = stockiddata.client_id
access_token = stockiddata.access_token

dhan = dhanhq(client_id, access_token)


securityId = stockiddata.securityId
netQty = stockiddata.netQty
sell_price = 0.5
sell_trigger_price = 0.55


sell_trigger_value = stockiddata.sell_trigger_value
sell_trigger_price = stockiddata.sell_trigger_price
order_id = None

def place_sell_order():
    global order_id, sell_price, sell_trigger_price, securityId
    
    order = dhan.place_order(
        security_id=securityId,  
        exchange_segment=dhan.NSE_FNO,
        transaction_type=dhan.SELL,
        quantity=netQty,
        order_type=dhan.SL,
        product_type=dhan.INTRA,
        price=sell_price,
        trigger_price=sell_trigger_price
    )
    order_id = order.get('data', {}).get('orderId')
    return order_id if order_id else "Order placement failed"

def modify_order():
    global sell_price, sell_trigger_price, order_id, netQty
    
    if order_id:
        sell_price += sell_trigger_price
        sell_trigger_price += sell_trigger_value
        response = dhan.modify_order(
            order_id=order_id,
            order_type=dhan.SL,
            leg_name=None,
            quantity=netQty,
            price=sell_price,
            trigger_price=sell_trigger_price,
            disclosed_quantity=0,
            validity=dhan.DAY
        )
        return f"Order modified: New Price {sell_price}, New Trigger {sell_trigger_price}"
    return "No order to modify."
