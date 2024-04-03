import requests
import os
from bs4 import BeautifulSoup
from testing import scrape_chapter, save_to_markdown

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

    # Get existing filenames in TheWanderingInn directory
    existing_files = os.listdir("TheWanderingInn")
    existing_titles = [filename.split(".")[0] for filename in existing_files]

    for div in soup.find_all('div', class_='body-web'):
        a_tag = div.find('a')
        if a_tag and a_tag.get('href'):
            chapter_url = a_tag.get('href')
            title, _ = scrape_chapter(chapter_url)
            
            # Check if title already exists in downloaded chapters
            if title not in existing_titles:
                chapter_urls.append(chapter_url)
                existing_titles.append(title)  # Add title to existing titles list
                if len(chapter_urls) >= 10:  # Stop at chapter 10
                    break

    return chapter_urls

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

# Function to save title and content to a Markdown file in TheWanderingInn directory
def save_to_markdown(title, content, filename):
    # Ensure TheWanderingInn directory exists, create it if it doesn't
    directory = "TheWanderingInn"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Join the directory path with the filename
    filepath = os.path.join(directory, filename)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(f"# {title}\n\n")
        file.write(content)
        
# Main function
def main():
    chapter_urls = get_chapter_urls(toc_url)
    for idx, url in enumerate(chapter_urls, start=1):
        title, content = scrape_chapter(url)
        filename = f'chapter_{idx}.md'
        save_to_markdown(title, content, filename)

if __name__ == '__main__':
    main()
