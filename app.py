import os
from flask import Flask

app = Flask(__name__)

# Get Secret
api_key = os.getenv("BITFORGE_SECRET", "No-Key-Found")

@app.route('/')
def home():
    return f"""
    <h1>BitForge Agency Tool v6 !!!!!!!!!!! GLOBAL AWS LAUNCH</h1>
    <p>Status: <b>ONLINE</b></p>
    <p>Secret Key Used: {api_key}</p>
    <p>Scanning active...</p>
    """

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    # Listen on 0.0.0.0 (All interfaces) on port 5000
    print("Starting Web Server...")
    app.run(host='0.0.0.0', port=5000)
