def fetch_data_from_api(api_url, params=None):
    import requests

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None


def post_data_to_api(api_url, data):
    import requests

    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error posting data to API: {e}")
        return None


def update_data_in_api(api_url, data):
    import requests

    try:
        response = requests.put(api_url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error updating data in API: {e}")
        return None


def delete_data_from_api(api_url):
    import requests

    try:
        response = requests.delete(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error deleting data from API: {e}")
        return None