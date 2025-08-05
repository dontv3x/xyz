from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Store message temporarily
messages = []

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

@app.route('/api/send', methods=['POST'])
def receive_data():
    data = request.json
    messages.append(data.get("message", "No message"))
    return {"status": "success"}

@app.route('/api/from-website', methods=['POST'])
def from_website():
    message = request.form.get("info")
    messages.append(message)
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
