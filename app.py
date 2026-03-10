from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def simple_bot_response(message: str) -> str:
    """
    Generate a response using the OpenAI Chat Completions API.
    Falls back to a friendly error message if the API call fails.
    """
    try:
        completion = client.chat.completions.create(
            model="gpt-5.3-instant",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a friendly, concise assistant embedded in a simple web "
                        "chatbot. Keep responses short and easy to read."
                    ),
                },
                {"role": "user", "content": message},
            ],
            max_tokens=200,
        )
        return completion.choices[0].message.content.strip()
    except Exception:
        return "Sorry, I had trouble talking to the AI service. Please try again."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()
    if not user_message:
        return jsonify({"response": "Please type a message first."}), 400

    response = simple_bot_response(user_message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)