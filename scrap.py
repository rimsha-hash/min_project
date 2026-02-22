import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website
url = "https://www.python.org"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract specific data
# For example, let's extract all the <h1> tags
headings = soup.find_all('h2')

# Step 4: Print the extracted data
#print("\nH1 Headings found on the page:\n")
for heading in headings:
    print(heading.text.strip())