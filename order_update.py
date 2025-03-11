from dhanhq import orderupdate
from dhanhq import dhanhq
import time
import stockiddata

client_id       = stockiddata.client_id
access_token    = stockiddata.access_token
stock_id        = stockiddata.securityId

dhan = dhanhq(client_id, access_token)

# Add your Dhan Client ID and Access Token
client_id = client_id
access_token = access_token

def run_position_update():
    position_update = dhan.get_positions()
    return position_update

def run_order_update():
    order_client = orderupdate.OrderSocket(client_id, access_token)
   
    while True:
        try:
            order_client.connect_to_dhan_websocket_sync()
        except Exception as e:
            print(f"Error connecting to Dhan WebSocket: {e}. Reconnecting in 5 seconds...")
            time.sleep(5)
            

run_order_update()