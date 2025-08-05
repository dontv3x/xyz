import requests

SERVER_URL = "https://xyz-u6do.onrender.com"  # Replace with your real URL

def main():
    print("🛰️ Private Messaging Client\n")
    sender = input("Your name: ")
    recipient = input("Send messages to: ")

    print(f"\nStart chatting with {recipient}. Press Ctrl+C to quit.\n")
    while True:
        try:
            message = input("> ")
            data = {
                "from": sender,
                "to": recipient,
                "message": message
            }
            response = requests.post(f"{SERVER_URL}/api/send", json=data)
            if response.status_code != 200:
                print("❌ Error:", response.json())
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
