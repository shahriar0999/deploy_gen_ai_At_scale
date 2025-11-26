from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv(override=True)
api_key = os.getenv('GROQ_API_KEY')

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("gsk_"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def instant():
    # Initialize Groq client with API key from environment variable
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    message = """
You are on a website that has just been deployed to production for the first time!
Please reply with an enthusiastic announcement to welcome visitors to the site, explaining that it is live on production for the first time!
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": message}]
    )

    reply = response.choices[0].message.content.replace("\n", "<br/>")

    html = f"""
    <html>
        <head><title>Live in an Instant!</title></head>
        <body><p>{reply}</p></body>
    </html>
    """

    return html
