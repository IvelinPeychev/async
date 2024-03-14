from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright


def homework():
    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto('https://www.wikipedia.org/')
            page.fill('#searchInput','aspirin')
            page.press('#searchInput', key='Enter')
            page.screenshot(path='result.png')
            extracted_info = page.text_content('#firstHeading')
            print(extracted_info)
        except Exception as e:
            print(f'An error occurred: {e}')


if __name__ == '__main__':
    homework()


