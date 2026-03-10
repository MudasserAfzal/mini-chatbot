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

    // Typing indicator while waiting for the AI
    const typingWrapper = document.createElement("div");
    typingWrapper.className = "typing-indicator-wrapper";

    const typingLabel = document.createElement("span");
    typingLabel.className = "typing-indicator-label";
    typingLabel.textContent = "Chatbot is thinking";

    const typing = document.createElement("div");
    typing.className = "typing-indicator";

    for (let i = 0; i < 3; i++) {
        const dot = document.createElement("span");
        dot.className = "typing-dot";
        typing.appendChild(dot);
    }

    typingWrapper.appendChild(typingLabel);
    typingWrapper.appendChild(typing);
    chatbox.appendChild(typingWrapper);

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

        // Remove typing indicator
        typingWrapper.remove();

        const botMsg = document.createElement("div");
        botMsg.className = "message bot";
        botMsg.textContent = data.response;
        chatbox.appendChild(botMsg);

        chatbox.scrollTop = chatbox.scrollHeight;
    } catch (err) {
        // Remove typing indicator if still there
        if (typingWrapper.isConnected) {
            typingWrapper.remove();
        }

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
