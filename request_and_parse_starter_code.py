# import relevant libraries
import requests
from bs4 import BeautifulSoup

# define the url
# FILL IN before running the code
url = "https://www.feedbooks.com/search?query=feedbooks"

# send a request to get html code from that url
# uncomment the following line and replace with your code
response = requests.get(url, headers={"Accept": "text/html"})

# parse the response
# uncomment the following line and replace with your code
parsed_response = BeautifulSoup(response.text, "html.parser")

titles = parsed_response.find_all("a", class_="block__item-title")

for title in titles:
    print(title.text)