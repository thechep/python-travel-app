from weather import get_weather
from utils import log_to_file, format_temperature


def display_weather(data):
    """Print formatted weather info"""

    if "error" in data:
        print("❌ Error:", data["error"])
        return

    print("\n🌤 Weather Info")
    print("------------------")
    print(f"City: {data['city']}")
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
