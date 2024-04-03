# import requests
# from bs4 import BeautifulSoup
# import time
# from main import get_chapter_urls

# def test_chapter_scraping(url):
#     print(f"Testing scraping for: {url}")
#     # Example of fetching and processing a chapter page
#     headers = {
#         'User-Agent': 'My Web Scraper 1.0 (your_email@example.com)'
#     }
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # TODO: Extract the relevant data from the chapter page
#     # For example, get the title and content
#     # This will depend on the specific structure of the chapter pages
#     # title = soup.find(....)
#     # content = soup.find(....)

#     # For now, just print the first 100 characters of the page
#     print("Content preview:", soup.text[:100])

# def main():
#     print("Testing chapter URL fetching...")
#     chapter_urls = get_chapter_urls('https://wanderinginn.com/table-of-contents/')
#     for url in chapter_urls[:5]:  # Testing with first 5 chapters
#         test_chapter_scraping(url)
#         time.sleep(2)  # Be polite and don't overload the server

# if __name__ == '__main__':
#     main()
import requests
from bs4 import BeautifulSoup

# Function to scrape chapter title and content from a given URL
def scrape_chapter(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract chapter title
    title_tag = soup.find('h1', class_='entry-title')
    if title_tag:
        title = title_tag.text.strip()
    else:
        title = "Title not found"  # Placeholder if title is not found

    # Extract chapter content
    content_div = soup.find('div', class_='entry-content')
    if content_div:
        paragraphs = content_div.find_all('p')
        content = '\n'.join([p.get_text() for p in paragraphs])
    else:
        content = "Chapter content not found"  # Placeholder if content is not found

    return title, content

# Function to save title and content to a Markdown file
def save_to_markdown(title, content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"# {title}\n\n")
        file.write(content)

# Main function to scrape and save first two chapters
def main():
    base_url = 'https://wanderinginn.com/2023/03/03/rw1-01/'
    for chapter_num in range(1, 3):
        chapter_url = f'{base_url}chapter-{chapter_num}/'
        title, content = scrape_chapter(chapter_url)
        save_to_markdown(title, content, f'chapter_{chapter_num}.md')

if __name__ == "__main__":
    main()
