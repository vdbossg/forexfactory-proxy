from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route("/calendar")
def calendar():
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/115.0.0.0 Safari/537.36"
            )
        }
        url = "https://www.forexfactory.com/calendar"
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            return Response(response.text, mimetype='text/html')
        else:
            return f"❌ Failed to fetch: {response.status_code}", 500
    except Exception as e:
        return f"❌ Proxy error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
