import requests

# Define the URL of the FastAPI backend's root endpoint
# This assumes the FastAPI service is running and accessible via docker-compose networking
# or directly if running locally.
# If using docker-compose, 'api' can be used as hostname: http://api:8000/
# For local testing before docker-compose up, it might be http://localhost:8000/
API_URL = "http://localhost:8000/"

def query_fastapi_backend():
    """
    Sends a GET request to the FastAPI backend's root endpoint and prints the response.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        print("Response from FastAPI backend:")
        # Assuming the backend returns JSON, like {"message": "Welcome..."}
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to FastAPI backend at {API_URL}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print(f"Attempting to query FastAPI backend at {API_URL}...")
    query_fastapi_backend()
