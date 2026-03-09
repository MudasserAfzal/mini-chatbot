async function sendMessage() {
    let input = document.getElementById("message");
    let message = input.value;

    let res = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({message: message})
    });

    let data = await res.json();

    let chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += "<p><b>You:</b> " + message + "</p>";
    chatbox.innerHTML += "<p><b>Bot:</b> " + data.response + "</p>";

    input.value = "";
}