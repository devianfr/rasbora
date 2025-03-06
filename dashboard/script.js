function sendRequest(endpoint) {
    fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
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
