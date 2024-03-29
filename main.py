import requests
from bs4 import BeautifulSoup

# URL of the Table of Contents
toc_url = 'https://wanderinginn.com/table-of-contents/'

# Function to get the list of chapter URLs
def get_chapter_urls(toc_url):
    # Add headers with a User-Agent
    headers = {
        'User-Agent': 'My Web Scraper 1.0 (your_email@example.com)'
    }

    response = requests.get(toc_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    chapter_urls = []
    for div in soup.find_all('div', class_='body-web'):
        a_tag = div.find('a')
        if a_tag and a_tag.get('href'):
            chapter_urls.append(a_tag.get('href'))
            if len(chapter_urls) >= 5:  # Limiting to the first 5 chapters for testing
                break

    return chapter_urls


# Function to scrape a chapter
def scrape_chapter(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # TODO: Extract the title and content of the chapter
    # You need to inspect the structure of a chapter's page
    title = ""  # Extract title
    content = ""  # Extract content

    return title, content

# Function to save content to a file
def save_content(title, content, filename):
    with open(filename, 'w') as file:
        file.write(title + "\n\n")
        file.write(content)

# Main function
def main():
    chapter_urls = get_chapter_urls(toc_url)
    for url in chapter_urls:
        title, content = scrape_chapter(url)
        filename = title.replace(" ", "_") + ".txt"  # Example filename
        save_content(title, content, filename)

if __name__ == '__main__':
    main()
