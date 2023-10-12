from bs4 import BeautifulSoup
# import requests

# Replace 'your_html_url' with the URL of the HTML page or provide the HTML content directly
# You can also use 'open' to read from a local HTML file.
# html_url = 'your_html_url'
# response = requests.get(html_url)
# html_content = response.text


html_file_path = 'your_local_html_file.html'
# Read the HTML content from the local file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Define the keyword you want to search for
# keyword = 'reel'

class_name = "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"

# Find the HTML element containing the keyword
a_elements = soup.find_all('a', class_=class_name)

url_header = "https://www.instagram.com"
# Print or process the found element
for a in a_elements:
    href = a.get('href')
    if href:
        print(url_header+href)