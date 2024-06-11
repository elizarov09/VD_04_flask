from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    current_time = now.strftime("%H:%M:%S")
    return f"<h1 style='font-family: Montserrat;'>Current Date and Time</h1><p style='font-family: Montserrat; font-size: 24px;'>{current_date}</p><p style='font-family: Montserrat; font-size: 24px;'>{current_time}</p>"

if __name__ == '__main__':
    app.run(debug=True)
