import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)

    # Create a new page
    page = browser.new_page()

    # Visit the playwright page
    page.goto('https://playwright.dev/python')

    # Locate a link element with 'Docs' text
    docs_btn = page.get_by_role('link', name='Get started')
    docs_btn.click()

    # Get the url
    print('Docs:', page.url)

    # Close the browser
    browser.close()