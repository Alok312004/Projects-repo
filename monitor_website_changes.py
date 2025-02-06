import requests
import time

def monitor_website(url, check_interval=60):
    previous_content = None

    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            current_content = response.text

            if previous_content is not None and current_content != previous_content:
                print(f"Change detected on {url}!")
            else:
                print(f"No changes detected on {url}.")

            previous_content = current_content
            time.sleep(check_interval)  # Wait for the specified interval

        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            time.sleep(check_interval)

if __name__ == "__main__":
    url_to_monitor = "https://www.aajtak.in/"  # Replace with the desired URL
    monitor_website(url_to_monitor)
