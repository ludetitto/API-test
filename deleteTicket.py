import os
import json
import requests
import addTicket

API_BASE_URL = os.environ.get('API_BASE_URL', 'http://localhost:58000/api/v1')

def main():
    serviceTicket = addTicket.get_service_ticket()
    api_url = f"{API_BASE_URL}/ticket/{serviceTicket}"
    headers = {
        "X-Auth-Token": serviceTicket,
        "content-type": "application/json"
    }
    response = requests.delete(api_url, headers=headers)
    result = f"Ticket delete status: {response.status_code}\n"
    try:
        response_json = response.json()
        result += json.dumps(response_json, indent=4)
    except Exception as e:
        result += f"Error parsing response: {e}"
    return result

if __name__ == "__main__":
    print(main())