async function sendMessage() {
const input = document.getElementById("user-input");
const message = input.value.trim();
if (!message) return;


addMessage(message, "user");
input.value = "";


const response = await fetch("http://localhost:8000/chat", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify({ message })
});


const data = await response.json();
addMessage(data.reply, "bot");
}


function addMessage(text, sender) {
const chatBox = document.getElementById("chat-box");
const msgDiv = document.createElement("div");
msgDiv.classList.add("message", sender);
msgDiv.textContent = text;
chatBox.appendChild(msgDiv);
chatBox.scrollTop = chatBox.scrollHeight;
}