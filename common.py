import requests
import json

def sendRequest(url, payload):
    # API endpoint (replace with your actual endpoint)
    # url = "https://api.example.com/endpoint"

    # # JSON payload to send
    # payload = {
    #     "name": "John Doe",
    #     "age": 30,
    #     "email": "johndoe@example.com"
    # }

    try:
        # Adding headers to specify JSON content
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        # Making the POST request
        response = requests.post(
            url=url,
            json=payload,  # requests will automatically serialize the dictionary to JSON
            headers=headers
        )

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        response_data = response.json()

        # Print the response
        # print("Response status code:", response.status_code)
        # print("Response data:", json.dumps(response_data, indent=2))

        return response_data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

