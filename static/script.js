const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

function appendMessage(sender, text, buttons = []) {
    const msg = document.createElement("div");
    msg.className = `message ${sender}`;
    msg.innerHTML = `<p>${text}</p>`;

    if (sender === "bot" && buttons.length > 0) {
        const btnContainer = document.createElement("div");
        btnContainer.className = "inline-buttons";
        buttons.forEach(btn => {
            const button = document.createElement("button");
            button.textContent = btn;
            button.onclick = () => sendMessage(btn);
            btnContainer.appendChild(button);
        });
        msg.appendChild(btnContainer);
    }

    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage(message = null) {
    const text = message || userInput.value.trim();
    if (!text) return;

    appendMessage("user", text);
    userInput.value = "";

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: text })
    })
    .then(res => res.json())
    .then(data => {
        appendMessage("bot", data.response, data.buttons);
    });
}

// Auto-start chat with welcome message
window.onload = () => {
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: "start" })
    })
    .then(res => res.json())
    .then(data => {
        appendMessage("bot", data.response, data.buttons);
    });
};
