import requests

SERVER_URL = "https://xyz-u6do.onrender.com"  # replace this with your deployed server URL

def main():
    print("🛰️ Python Client\n")
    name = input("Enter your name: ")

    print("\nStart typing messages. Press Ctrl+C to quit.\n")
    while True:
        try:
            message = input("> ")
            data = {"name": name, "message": message}
            response = requests.post(f"{SERVER_URL}/api/send", json=data)
            if response.status_code != 200:
                print("❌ Error sending message:", response.json())
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
