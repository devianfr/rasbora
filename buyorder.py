from dhanhq import dhanhq
import stockiddata

client_id = stockiddata.client_id
access_token = stockiddata.access_token

dhan = dhanhq(client_id, access_token)


securityId ='45546'
netbuyQty = 75


def fno_buy_order(order_type="LIMIT", limit_price=0):
    global securityId, netbuyQty

    # Determine order type dynamically
    order_type_enum = dhan.MARKET if order_type == "MARKET" else dhan.LIMIT

    # Calculate trigger price only if it's a LIMIT order
    trigger_price = limit_price - 0.20 if order_type == "LIMIT" else 0

    order = dhan.place_order(
        security_id=securityId,
        exchange_segment=dhan.NSE_FNO,
        transaction_type=dhan.BUY,
        quantity=netbuyQty,
        order_type=order_type_enum,
        product_type=dhan.INTRA,
        price=limit_price if order_type == "LIMIT" else 0,  # No price for MARKET orders
        trigger_price=trigger_price  # No trigger for MARKET orders
    )

    order_status = order.get('data', {})
    return order_status if order_status else "Order placement failed"
    