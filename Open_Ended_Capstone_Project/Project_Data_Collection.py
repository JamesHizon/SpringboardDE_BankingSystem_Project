# Web Scraping using Python to scrape data from website:

# Steps:
# 1) Use requests package to run an HTTP request to retrieve HTML data.
# - This will allow the server to send back and store the data inside a Python object.

import requests
from bs4 import BeautifulSoup

# Use mainly to get information about the list of files present:
URL = 'http://data.gdeltproject.org/gkg/index.html'
page = requests.get(URL)
# print(page)

# Note that all of the data is in the form of links.

# Next:
# - Parse through the structured data using BeautifulSoup.

soup = BeautifulSoup(page.content, 'html.parser')

# - Here, we created a Beautiful Soup object that takes the HTML content scraped earlier
# as its input.
# - When you instantiate the object, you also instruct Beautiful Soup to use
# the appropriate parser.

# Next:
# - Filter out data to only obtain first 14 links and download the data.

# Should look something like:

base_url = 'http://data.gdeltproject.org/gkg/'

for link in soup.find_all('a')[2:16]:
    file_link = link.get('href')
    if link.has_attr('href'):
        file = link.attrs['href']
        download_url = f"{base_url}{file}"
        with open(f"{file}", 'wb') as file:
            response = requests.get(download_url)
            file.write(response.content)





