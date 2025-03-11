from dhanhq import orderupdate
from dhanhq import dhanhq
import time
import stockiddata

client_id       = stockiddata.client_id
access_token    = stockiddata.access_token
stock_id        = stockiddata.securityId

dhan = dhanhq(client_id, access_token)

response= dhan.get_positions()
print(response)

if not response or "data" not in response:
    print("Error: Failed to fetch orders")  # Print error to terminal
    
netQty=None
for order in response["data"]:
    if order["positionType"] == "CLOSED":
        netQty= order["buyQty"]
        break  # Exit loop after finding the first pending order
        
if netQty:
    print("qty", netQty)
else:
    print("No pending orders found")