from datetime import datetime

def log_to_file(message, filename="data/history.txt"):
    """Append messages to a file with timestamp.

    Creates the target directory if it doesn't already exist, so the
    caller doesn't need to worry about it (the simple example app often
    runs in a fresh checkout).
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # make sure the parent directory exists
    import os

    parent = os.path.dirname(filename)
    if parent and not os.path.exists(parent):
        os.makedirs(parent, exist_ok=True)

    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def format_temperature(temp_celsius):
    """Return temperature string with both Celsius and Fahrenheit.

    The API provides the temperature in Celsius; we convert to Fahrenheit
    for users who prefer that unit.  The output looks like:

        21.3°C / 70.3°F
    """
    fahrenheit = temp_celsius * 9 / 5 + 32
    return f"{temp_celsius:.1f}°C / {fahrenheit:.1f}°F"
