from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

#List of publisher index page
DETIK_NEWS = "https://news.detik.com/indeks"

# Fetch the URL data using requests.get(url),
request_result = requests.get(DETIK_NEWS).text

def get_parent_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain.startswith('www.'):
        domain = domain[4:]  # Remove 'www.' from the beginning if present

    # Split the domain into its parts
    domain_parts = domain.split('.')

    # Check if the domain has more than two parts
    if len(domain_parts) > 2:
        parent_domain = '.'.join(domain_parts[-3:])
    else:
        parent_domain = domain

    return parent_domain

#Data Constructor
# dict = {
#     'source': source,
#     'title': title,
#     'published': publish,
#     'link': link
# }

# Creating soup from the fetched request
soup = BeautifulSoup(request_result, 'html.parser')

# # soup.find.all( h3 ) to grab
# all major headings of our search result,
articles = soup.find_all('article')

for article in articles:
    title = article.find('h3').getText()
    link = article.find('a')['href']
    source = get_parent_domain(link)
    time_published = article.find(class_="media__date")
    print(title)
    print(link)
    print(source)
    print(time_published)
