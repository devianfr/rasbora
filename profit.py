from dhanhq import dhanhq
import stockiddata

# Initialize DhanHQ client
client_id = stockiddata.client_id
access_token = stockiddata.access_token
dhan = dhanhq(client_id, access_token)

# Fetch positions
positions = dhan.get_positions()

# Check if the response is valid
if positions.get('status') == 'success' and 'data' in positions:
    total_realized_profit = sum(pos.get('realizedProfit', 0) for pos in positions['data'])
    print(f"Total Realized Profit: {total_realized_profit}")
else:
    print("Failed to fetch positions or no data available.")
