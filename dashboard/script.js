function sendRequest(endpoint) {
    const orderType = document.querySelector('input[name="orderType"]:checked').value;
    let limitPrice = parseFloat(document.getElementById("limitPrice").value);

    if (isNaN(limitPrice)) {
        limitPrice = 0;  // Default to 0 for safety
    }

    fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ order_type: orderType, limit_price: limitPrice })
    })
    .then(response => response.json())
    .then(data => {
        const message = data.status === "success" ? "Success: " + JSON.stringify(data) : "Error: " + data.message;
        logToTerminal(message);
    })
    .catch(error => logToTerminal("Error: " + error));
}
function logToTerminal(message) {
    const terminal = document.getElementById("terminal");
    const newMessage = document.createElement("div");
    newMessage.textContent = "> " + message;
    newMessage.classList.add("terminal-message");
    terminal.appendChild(newMessage);
    terminal.scrollTop = terminal.scrollHeight;  // Auto-scroll to the latest message
}

function fetchRealizedProfit() {
    fetch("/realized_profit")  // Call API
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            let profit = data.realized_profit.toFixed(2);
            let profitElement = document.getElementById("realized-profit");

            // Update UI
            profitElement.textContent = `${profit}`;
            profitElement.style.color = profit >= 0 ? "green" : "red";
        } else {
            console.error("Error fetching profit:", data.message);
        }
    })
    .catch(error => console.error("Error:", error));
}

// Attach event listener to button
document.getElementById("refresh-profit").addEventListener("click", fetchRealizedProfit);


