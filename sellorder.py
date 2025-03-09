from dhanhq import dhanhq
import stockiddata

client_id = stockiddata.client_id
access_token = stockiddata.access_token

dhan = dhanhq(client_id, access_token)

securityId = '11915'
netbuyQty = 1

def fno_sell_order(order_type="LIMIT", limit_price=0):
    global securityId, netbuyQty

    order_type_enum = dhan.MARKET if order_type == "MARKET" else dhan.SL
    trigger_price = limit_price + 0.20 if order_type == "LIMIT" else 0

    try:
        order = dhan.place_order(
            security_id=securityId,
            exchange_segment=dhan.NSE_FNO,
            transaction_type=dhan.SELL,
            quantity=netbuyQty,
            order_type=order_type_enum,
            product_type=dhan.INTRA,
            price=limit_price if order_type == "LIMIT" else 0,
            trigger_price=trigger_price if order_type == "LIMIT" else 0
        )
        

        return order.get('data', {}) or "Order placement failed"
    except Exception as e:
        return str(e)
