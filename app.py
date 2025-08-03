from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/calendar')
def proxy_calendar():
    url = "https://www.forexfactory.com/calendar"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
        "Referer": "https://www.google.com"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        return Response(response.content, content_type=response.headers.get('Content-Type'))
    except Exception as e:
        return f"❌ Proxy failed: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
