import time
import os
import sys
from datetime import datetime # Add this import!

# ... (Keep the top part with the API key check exactly the same) ...
print("--- BITFORGE AGENCY TOOL v3 ---")

# ... (Keep the API Key validation logic) ...
api_key = os.getenv("BITFORGE_SECRET")
if api_key != "super-secret-password":
    sys.exit(1)

print("Server started. Saving data to /data/leads.txt")

# Ensure the folder exists inside the container
os.makedirs("/data", exist_ok=True)

while True:
    # Create a timestamp string
    now = datetime.now().strftime("%H:%M:%S")
    log_entry = f"[{now}] Found client using key: {api_key}\n"

    # Write to file
    with open("/data/leads.txt", "a") as file:
        file.write(log_entry)

    print(f"Log saved: {log_entry.strip()}")
    time.sleep(5)
