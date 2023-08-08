import requests

def send_report(token, channel_id, message_id):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

    payload = {
        "version": "1.0",
        "variant": "3",
        "language": "en",
        "breadcrumbs": [3, 31],
        "elements": {},
        "name": "message",
        "channel_id": channel_id,
        "message_id": message_id
    }

    try:
        response = requests.post("https://discord.com/api/v9/reporting/message", headers=headers, json=payload)
        response.raise_for_status()

        if "report_id" in response.json():
            return True
        elif "Missing Access" in response.text:
            print("Missing Access.")
            return False
        else:
            print("Unknown response:", response.text)
            return False

    except requests.exceptions.RequestException as e:
        print("Error during API request:", e)
        return False

if __name__ == "__main__":
    print("\t Nhizz \n")
    token = input("Token > ")
    channel_id = input("ChannelID > ")
    message_id = input("MsgID > ")

    amt = 0

    for _ in range(5):
        if send_report(token, channel_id, message_id):
            amt += 1
            print(f"(+) Report Sent. [{amt}]")
        else:
            break
