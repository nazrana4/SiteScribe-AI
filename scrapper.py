import requests
import os
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def sanitize_filename(name):
    return re.sub(r'[\/:*?"<>|]', '_', name)

def get_last_part_from_url(url):
    """
    Extract the last meaningful part of the URL path for use in filenames.
    Handles various edge cases to ensure valid extraction.
    """
    parsed_url = urlparse(url)
    return sanitize_filename(parsed_url.netloc)  # Use the domain name as a fallback

def extract_main_content(soup):
    """
    Extract the main content from the HTML, excluding navigation bars and headers.
    """
    # Remove nav, header, and footer sections from the soup
    for tag in soup(['nav', 'header']):
        tag.decompose()

    # Extract and return the body content
    body = soup.body
    return body.get_text(separator='\n') if body else soup.get_text(separator='\n')

def getData():
    url = input("Enter the URL of the website to scrape: ")
    try:
        # Validate and make the HTTP request
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string.strip() if soup.title else get_last_part_from_url(url)

    cleaned_text = extract_main_content(soup)

    cleaned_lines = [
        ' '.join(line.split())  # Normalize multiple spaces
        for line in cleaned_text.splitlines()  # Split into lines
        if line.strip()  # Exclude empty or whitespace-only lines
    ]
    cleaned_text = '\n'.join(cleaned_lines)

    # Ensure the content directory exists
    os.makedirs('./content', exist_ok=True)

    # Save cleaned content to a file
    sanitized_title = sanitize_filename(title)
    content_file_path = f'./content/{sanitized_title}.txt'
    with open(content_file_path, "w", encoding="utf-8") as writer:
        writer.write(cleaned_text)
        print("Content saved '")

def main():
    while True:
        try:
            choice = int(input("\n1. Scrape a site\n2. Exit\nEnter your choice: "))
            if choice == 2:
                print("Exiting...")
                break
            elif choice == 1:
                getData()
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
