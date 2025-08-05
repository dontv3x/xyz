from flask import Flask, request, render_template
from collections import defaultdict
import os

app = Flask(__name__)

# recipient_messages: { recipient_name: [ (sender, message), ... ] }
recipient_messages = defaultdict(list)

@app.route('/')
def home():
    return render_template('index.html', recipient_messages=recipient_messages)

@app.route('/api/send', methods=['POST'])
def send_message():
    data = request.json
    sender = data.get("from")
    recipient = data.get("to")
    message = data.get("message")

    if sender and recipient and message:
        recipient_messages[recipient].append((sender, message))
        return {"status": "success"}
    return {"status": "error", "detail": "Missing from/to/message"}, 400



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
