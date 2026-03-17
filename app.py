from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from google import genai
from google.genai.types import GenerateContentConfig
from google.genai.errors import ClientError
import traceback

load_dotenv()

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

SYSTEM_INSTRUCTION = """You are a helpful travel assistant that designs practical travel itineraries.

Goals:
- Create a day-by-day itinerary for the requested number of days.
- Respect transport preferences (walk/metro/car/train/flight), pace (relaxed/standard/packed), and budget.
- Include realistic travel time/sequence, and group nearby attractions together.
- Suggest meals/local food, and at least 1 flexible option per day (backup).

When details are missing, ask up to 3 short clarifying questions first.

Output format:
1) Trip summary (destination(s), days, pace, transport)
2) Day-by-day plan (Day 1..N) with morning/afternoon/evening
3) Transport plan (how to move each day)
4) Tips (tickets, safety, weather, local etiquette)
Keep it concise and scannable.
"""


def travel_bot_response(message: str) -> str:
    if not client:
        return (
            "Missing GEMINI_API_KEY. Add it to your .env file as GEMINI_API_KEY=... "
            "and restart the server."
        )

    try:
        result = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=message,
            config=GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION),
        )
        text = getattr(result, "text", "") or ""
        text = text.strip()
        return text or "I couldn’t generate a response. Please try again."
    except ClientError as e:
        # Common: 429 RESOURCE_EXHAUSTED (quota/billing/rate limit)
        details = ""
        try:
            details = getattr(e, "message", "") or ""
        except Exception:
            details = ""

        print("Gemini ClientError:", repr(e))
        print(traceback.format_exc())

        if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):
            return (
                "Gemini API quota exceeded for this project/key. "
                "Check your plan/billing and rate limits, then try again."
            )

        return "Gemini API request failed. Please check your API key and try again."
    except Exception:
        print("Gemini unexpected error:")
        print(traceback.format_exc())
        return "Sorry, I had trouble talking to Gemini. Please try again."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()
    if not user_message:
        return jsonify({"response": "Please type a message first."}), 400

    response = travel_bot_response(user_message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)