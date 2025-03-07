from dhanhq import dhanhq
import stockiddata

# Initialize Dhan API client
client_id = stockiddata.client_id
access_token = stockiddata.access_token
dhan = dhanhq(client_id, access_token)

def get_realized_profit():
    """Fetches current positions and calculates total realized profit."""
    try:
        positions = dhan.get_positions()  # Fetch all positions
        print("API Response:", positions)  # Debugging line to check response structure

        if not isinstance(positions, dict) or "data" not in positions:
            return {"status": "error", "message": "Invalid response format from API"}

        total_realized_profit = 0

        for position in positions["data"]:  
            if not isinstance(position, dict):  # Ensure it's a dictionary
                continue  
            
            # Ensure key exists before accessing it
            realized_profit = position.get("realizedProfit", "0")
            try:
                total_realized_profit += float(realized_profit)
            except ValueError:
                return {"status": "error", "message": f"Invalid profit value: {realized_profit}"}

        return {"status": "success", "realized_profit": round(total_realized_profit, 2)}

    except Exception as e:
        return {"status": "error", "message": str(e)}
