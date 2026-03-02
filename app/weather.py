import requests

#API_KEY = "YOUR_API_KEY_HERE"  # replace with your OpenWeather key
API_KEY = "e5c227d27e78efb665e88af7db435e52"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data from API"""

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        # Raise error for bad responses (like 404, 500)
        response.raise_for_status()

        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }

    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error: {http_err}"}

    except requests.exceptions.ConnectionError:
        return {"error": "Connection error. Check internet."}

    except requests.exceptions.Timeout:
        return {"error": "Request timed out."}

    except Exception as e:
        return {"error": f"Unexpected error: {e}"}
