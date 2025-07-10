import json
import requests

def get_service_ticket():
    api_url = "http://localhost:58000/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "cisco",
        "password": "cisco"
    }
    response = requests.post(api_url, json.dumps(body_json), headers=headers)
    response_json = response.json()
    return response_json["response"]["serviceTicket"]

def main():
    api_url = "http://localhost:58000/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "cisco",
        "password": "cisco"
    }
    response = requests.post(api_url, json.dumps(body_json), headers=headers)
    result = f"Ticket request status: {response.status_code}\n"
    try:
        response_json = response.json()
        result += json.dumps(response_json, indent=4) + "\n"
        serviceTicket = response_json["response"]["serviceTicket"]
        result += f"El Ticket es: {serviceTicket}"
    except Exception as e:
        result += f"Error parsing response: {e}"
    return result

if __name__ == "__main__":
    print(main())
