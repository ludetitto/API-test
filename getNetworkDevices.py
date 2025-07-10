import json
import requests
import addTicket


def main():
    serviceTicket = addTicket.get_service_ticket()

    api_url = "http://localhost:58000/api/v1/network-device"

    headers = {
        "X-Auth-Token": serviceTicket,
        "content-type": "application/json"
    }

    response = requests.get(api_url, headers=headers)

    result = f"Ticket request status: {response.status_code}\n"

    try:
        response_json = response.json()
        result += json.dumps(response_json, indent=4)
    except Exception as e:
        result += f"Error parsing response: {e}"

    return result


if __name__ == "__main__":
    print(main())