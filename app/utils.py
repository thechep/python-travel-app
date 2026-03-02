from datetime import datetime

def log_to_file(message, filename="data/history.txt"):
    """Append messages to a file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def format_temperature(temp_celsius):
    return f"{temp_celsius:.1f}°C"
