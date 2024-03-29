import requests
from bs4 import BeautifulSoup
import time
from main import get_chapter_urls

def test_chapter_scraping(url):
    print(f"Testing scraping for: {url}")
    # Example of fetching and processing a chapter page
    headers = {
        'User-Agent': 'My Web Scraper 1.0 (your_email@example.com)'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # TODO: Extract the relevant data from the chapter page
    # For example, get the title and content
    # This will depend on the specific structure of the chapter pages
    # title = soup.find(....)
    # content = soup.find(....)

    # For now, just print the first 100 characters of the page
    print("Content preview:", soup.text[:100])

def main():
    print("Testing chapter URL fetching...")
    chapter_urls = get_chapter_urls('https://wanderinginn.com/table-of-contents/')
    for url in chapter_urls[:5]:  # Testing with first 5 chapters
        test_chapter_scraping(url)
        time.sleep(2)  # Be polite and don't overload the server

if __name__ == '__main__':
    main()
