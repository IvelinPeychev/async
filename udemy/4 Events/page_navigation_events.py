from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=500
    )

    page = browser.new_page()
    print('Page loading...')
    start_time = perf_counter()

    page.goto('https://bootswatch.com/default',
              # wait_until='load'  # wait for all items of the page to load - images, icons, just all - 1.35 seconds
              # wait_until="domcontentloaded" # wait for the HTML content to load, don't wait for images, icons - 1.28 seconds
              # wait_until="commit" # wait for HTML response call from the server, not wait for the HTML is loaded/displayed - 1.06 seconds
              wait_until="networkidle" # wait for all network events if there are such (analytics or other) - 2.39 seconds 
            )

    time_taken = perf_counter() - start_time
    print(f'...Page is loaded for {round(time_taken, 2)} seconds')

    browser.close()
