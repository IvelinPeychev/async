from playwright.sync_api import sync_playwright
import re

def product_review():
    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(headless=False)  # Consider headless=True for automation
            page = browser.new_page()
            page.goto('https://www.imdb.com/')
            page.fill('#suggestion-search', 'die hard 2')
            page.press('#suggestion-search', 'Enter')
            # Ensure you have the correct selector for the first search result
            first_result_selector = '.ipc-metadata-list-summary-item__t'
            page.click(first_result_selector)
            page.wait_for_load_state('domcontentloaded')  # Ensure movie page is loaded
            page.screenshot(path='imbd.png')
            title = page.title()
            name = ""
            year = ""
            match = re.match(r"(.+?)\s+\(\d{4}\)", title)
            if match:
                name = match.group(1)
            year_match = re.search(r'\b(\d{4})\b', title)
            if year_match:
                year = year_match.group(1)
            print(f'The name of the movie is: {name} \nThe year of the movie is: {year}')
        except Exception as e:
            print(f'An error occurred: {e}')

if __name__ == '__main__':
    product_review()

