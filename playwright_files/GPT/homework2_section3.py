from playwright.sync_api import sync_playwright
import re


def product_review():
    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(headless=True)
            # for headless usage we have to use the user agent from new_context before creating a page instance
            context = browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36')
            page = context.new_page()
            page.goto('https://www.imdb.com/')
            page.fill('#suggestion-search', 'die hard3')
            page.press('#suggestion-search','Enter')
            page.click('.ipc-metadata-list-summary-item__t')
            page.screenshot(path='imbd.png')
            title = page.title()
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