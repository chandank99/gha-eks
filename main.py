from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: white;
                text-align: center;
                padding-top: 100px;
            }

            .card {
                background: rgba(255,255,255,0.15);
                padding: 40px;
                border-radius: 20px;
                width: 400px;
                margin: auto;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            }

            button {
                background: white;
                color: #0077ff;
                border: none;
                padding: 12px 20px;
                border-radius: 10px;
                cursor: pointer;
                font-size: 16px;
                margin-top: 20px;
            }

            button:hover {
                background: #f1f1f1;
            }

            #message {
                margin-top: 20px;
                font-size: 20px;
                font-weight: bold;
            }

            a {
                color: yellow;
                text-decoration: none;
            }
        </style>
    </head>

    <body>

        <div class="card">
            <h1>🚀 Flask App Running on Kubernetes</h1>

            <p id="clock"></p>

            <button onclick="showMessage()">
                Click Me
            </button>

            <div id="message"></div>

            <p>
                Health Check:
                <a href="/health">/health</a>
            </p>
        </div>

        <script>
            function showMessage() {
                document.getElementById("message").innerHTML =
                    "✅ Your Flask app is working perfectly!";
            }

            function updateClock() {
                const now = new Date();
                document.getElementById("clock").innerHTML =
                    "🕒 " + now.toLocaleTimeString();
            }

            setInterval(updateClock, 1000);
            updateClock();
        </script>

    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
