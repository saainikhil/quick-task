import os
import sys
from flask import Flask

PORT = os.getenv("PORT")
if not PORT:
    print("ERROR: PORT environment variable is not set")
    sys.exit(1)

app = Flask(__name__)

@app.route("/")
def home():
    return f"App is working"

@app.route("/health")
def health():
    return "UP"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(PORT))

