async function sendMessage() {
    const input = document.getElementById("message");
    const message = input.value.trim();
    if (!message) return;

    const chatbox = document.getElementById("chatbox");

    // Add user message bubble
    const userMsg = document.createElement("div");
    userMsg.className = "message user";
    userMsg.textContent = message;
    chatbox.appendChild(userMsg);

    input.value = "";
    chatbox.scrollTop = chatbox.scrollHeight;

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await res.json();

        const botMsg = document.createElement("div");
        botMsg.className = "message bot";
        botMsg.textContent = data.response;
        chatbox.appendChild(botMsg);

        chatbox.scrollTop = chatbox.scrollHeight;
    } catch (err) {
        const errMsg = document.createElement("div");
        errMsg.className = "message bot";
        errMsg.textContent = "Sorry, something went wrong.";
        chatbox.appendChild(errMsg);
        chatbox.scrollTop = chatbox.scrollHeight;
    }
}

// Send on Enter
document.getElementById("message").addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});
