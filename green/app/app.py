from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>Blue-Green App</title></head>
    <body style="background-color: green; color: white; text-align: center; font-family: Arial;">
        <h1>Welcome to the GREEN Deployment!</h1>
        <p>This page is served from the GREEN version of the app.</p>
    </body>
    </html>
    """

@app.route("/version")
def version():
    return "This is the GREEN version!"  # Change to BLUE in the blue image

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
