""" 
    
    Written as a little "test drive" of the Beautiful Soup package that can be used
    for screen scraping. You will need to make sure BeautifulSoup has been installed
    e.g. pip3 install beautifulsoup4
    
    Author: KEN
    Date:   2023.04.27

 """

import requests
from bs4 import BeautifulSoup


# This is an example of scraping from a FORMATTED website where you know the structure

url = 'http://quotes.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        quote_text = quote.find('span', class_='text').text
        quote_author = quote.find('small', class_='author').text
        print(f"\n\n*** FORMATTED SCREENSCRAPING *** \n")
        print(f"Quote: {quote_text}\nAuthor: {quote_author}\n")
else:
    print(f"Error: Unable to fetch data from the website. Status code: {response.status_code}")


# This is an example of scraping from an UNFORMATTED website where you know the structure

import requests
from bs4 import BeautifulSoup, Comment

def extract_text_from_page(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove script and style elements
        for element in soup(['script', 'style']):
            element.decompose()

        # Remove comments
        for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()

        # Extract text from the remaining elements
        text = soup.get_text(separator=' ')

        # Replace consecutive whitespace characters with a single space
        clean_text = ' '.join(text.split())

        return clean_text
    else:
        print(f"Error: Unable to fetch data from the website. Status code: {response.status_code}")
        return None

url = 'https://ritley.com/blog'
text_content = extract_text_from_page(url)

if text_content:
    print(f"\n\n*** UNFORMATTED SCREENSCRAPING *** \n")
    print(text_content)
