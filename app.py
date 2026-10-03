from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
                background-color: #f4f4f4;
            }

            .container {
                background: white;
                width: 500px;
                margin: auto;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.2);
            }

            h1 {
                color: #333;
            }

            p {
                color: #666;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Python Application</h1>
            <p>Application deployed successfully!</p>
            <p>Jenkins + Docker + Python</p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return "Application is healthy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
