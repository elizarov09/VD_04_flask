from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current Date and Time</h1><p>{current_time}</p>"

if __name__ == '__main__':
    app.run(debug=True)
