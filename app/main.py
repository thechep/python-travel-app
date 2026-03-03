from weather import get_weather
from utils import log_to_file, format_temperature


def display_weather(data):
    """Print formatted weather info.

    The open‑weather API returns a temperature in Celsius.  We call
    :func:`format_temperature` which now includes both Celsius and
    Fahrenheit so the user can see whichever unit they prefer.
    """

    if "error" in data:
        print("❌ Error:", data["error"])
        return

    print("\n🌤 Weather Info")
    print("------------------")
    print(f"City: {data['city']}")
    # format_temperature already includes both °C and °F
    print(f"Temperature: {format_temperature(data['temperature'])}")
    print(f"Condition: {data['description']}")


def main():
    print("=== Travel Weather App ===")

    while True:
        city = input("\nEnter city (or 'exit'): ").strip()

        if city.lower() == "exit":
            print("Goodbye!")
            break

        result = get_weather(city)

        display_weather(result)

        # Save to file
        log_to_file(f"{city} -> {result}")


if __name__ == "__main__":
    main()
