# Mini Chatbot

An elegant, single-page AI chatbot built with **Flask** on the backend and a modern, animated UI on the frontend.  
User messages are sent to the **OpenAI ChatGPT API** (via `gpt-4.1-mini` by default) and streamed back to the browser in a chat-style interface.

## Preview

```markdown
![static/ui-screenshot.png]
```

## Features

- **AI-powered conversations** using the OpenAI Chat Completions API
- **Clean, modern UI** with gradient background and glassmorphism card
- **Smooth animations** for page load and message bubbles
- **Typing indicator** so users can see when the bot is “thinking”
- **Keyboard-friendly**: press Enter to send messages
- Simple, minimal **Python/Flask** code that is easy to extend

## Tech Stack

- **Backend**: Python, Flask
- **AI**: OpenAI ChatGPT API (`gpt-4.1-mini`)
- **Frontend**: HTML, vanilla JavaScript, CSS (DM Sans, glassmorphism, animations)

## Prerequisites

- Python 3.9+
- An OpenAI API key

## Setup

1. **Create environment file**

   In the project root, create a `.env` file and add your API key:

   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the App (Development)

From the project root:

```bash
python app.py
```

The app will start on `http://127.0.0.1:5000`. Open it in your browser and start chatting.

## Production Notes

- Use a proper WSGI server such as **gunicorn** or **uWSGI** (behind Nginx or another reverse proxy) instead of `app.run(debug=True)` for production deployments.
- Set `debug=False` and configure `host`/`port` appropriately when running in production.
- Store your `OPENAI_API_KEY` securely using environment variables or a secrets manager, not committed to source control.

## Customization

- **Model**: Change the `model` name in `app.py` (`gpt-4.1-mini`) to another model that fits your use case and quota.
- **Persona**: Update the system message in `app.py` to adjust the chatbot’s tone and behavior (e.g., more formal, more friendly, domain-specific, etc.).
- **Styling**: Edit `static/style.css` to tweak colors, animations, spacing, or to add branding for your own product.

## License

This project is provided as a simple reference implementation. Add your preferred license here (e.g., MIT, Apache 2.0) if you plan to publish it.
