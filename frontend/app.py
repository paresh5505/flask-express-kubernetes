from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def home():
    try:
        res = requests.get("http://express-service:3000/")
        return f"<h2>Flask Frontend</h2><p>Response from Backend: {res.text}</p>"
    except:
        return "Unable to reach backend"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
