from playwright.sync_api import sync_playwright
import time
import re


def fill_form():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.imdb.com/")
        page.fill("#suggestion-search", "Inception")
        page.press("#suggestion-search","Enter")
        page.click(".ipc-metadata-list-summary-item__t")
        print(page.title())
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
        director = page.locator('xpath=/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[2]/div/ul/li[1]/div')
        print(director.text_content())

        browser.close()


if __name__ == "__main__":
    fill_form()