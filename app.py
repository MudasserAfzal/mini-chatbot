from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def simple_bot_response(message):
    message = message.lower()

    if "hello" in message:
        return "Hi there!"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing great!"
    elif "bye" in message:
        return "Goodbye!"
    else:
        return "I don't understand that yet."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = simple_bot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)