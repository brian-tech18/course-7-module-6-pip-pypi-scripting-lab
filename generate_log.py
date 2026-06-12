import requests
from datetime import datetime

def fetch_data():
    # Fetching placeholder data from the public testing endpoint
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    # 1. Fetch data from the API
    post = fetch_data()
    post_title = post.get("title", "No title found")
    print("Fetched Post Title:", post_title)

    # 2. Make our log contents list
    log_data = [
        "User logged in", 
        "User updated profile", 
        "Report exported",
        "API Data: " + post_title
    ]
    
    # 3. Format the text file with a date timestamp
    date_string = datetime.now().strftime('%Y%m%d')
    filename = "log_" + date_string + ".txt"

    # 4. Write data to the text file using File I/O loop
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(entry + "\n")

    print("Log written to " + filename)
