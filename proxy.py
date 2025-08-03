from flask import Flask, Response
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/calendar")
def calendar():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
            context = browser.new_context(
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/115.0.0.0 Safari/537.36"
                ),
                java_script_enabled=True,
                viewport={"width": 1280, "height": 800},
                locale="en-US"
            )
            page = context.new_page()

            # Stealth tricks to bypass bot detection
            page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
                window.chrome = { runtime: {} };
                Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
                Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
            """)

            print("🌐 Visiting ForexFactory...")
            page.goto("https://www.forexfactory.com/calendar", timeout=60000)
            page.wait_for_selector("table.calendar__table", timeout=30000)

            html = page.content()
            browser.close()
            return Response(html, mimetype='text/html')
    except Exception as e:
        return Response(f"❌ Proxy error: {str(e)}", status=500)

if __name__ == "__main__":
    print("🔌 Proxy running on http://0.0.0.0:8081/calendar")
    app.run(host="0.0.0.0", port=8081)
