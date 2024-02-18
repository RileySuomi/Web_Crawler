
from bs4 import BeautifulSoup
import requests



def parse(url):
    # Fetch the HTML content of the webpage
    url_current = 'https://example.com'
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all 'a' tags which contain href attributes
    hrefs = soup.find_all('a', href=True)

    # Extract and print the href values
    for href in hrefs:
        print(href['href'])




def main():

    pass

if __name__ == "main":
    main()

