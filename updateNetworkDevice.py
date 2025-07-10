import os
import json
import requests
import addTicket


API_BASE_URL = os.environ.get('API_BASE_URL', 'http://localhost:58000/api/v1')


def main():
    serviceTicket = addTicket.get_service_ticket()
    api_url = f"{API_BASE_URL}/network-device"

    headers = {
        "X-Auth-Token": serviceTicket,
        "content-type": "application/json"
    }

    body_json = {
        "ipAddress": "11.1.1.1",
        "globalCredentialId": "cisco"
    }

    response = requests.put(api_url, json.dumps(body_json), headers=headers)

    result = f"Ticket request status: {response.status_code}\n"
    try:
        response_json = response.json()
        result += json.dumps(response_json, indent=4)
    except Exception as e:
        result += f"Error parsing response: {e}"

    return result


if __name__ == "__main__":
    print(main())