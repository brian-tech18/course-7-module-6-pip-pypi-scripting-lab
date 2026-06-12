import requests
from datetime import datetime

def generate_log(log_data):
    # Ensure it is a list type
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    # Use the exact f-string filename pattern from instructions
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write contents exactly matching the template format
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # Match the exact print string format
    print(f"Log written to {filename}")

def fetch_data():
    # Fixed: Assigned the requests output directly to the response variable
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    post = fetch_data()
    post_title = post.get("title", "No title found")
    print("Fetched Post Title:", post_title)

    default_logs = [
        "User logged in", 
        "User updated profile", 
        "Report exported",
        f"API Data: {post_title}"
    ]
    
    generate_log(default_logs)
