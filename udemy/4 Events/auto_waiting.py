from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=500
    )

    page = browser.new_page()
    page.goto('https://bootswatch.com/default')


    link = page.locator('a.dropdown-item').first
    link.click(force= True, timeout=2_000) # force to click the button right away, timeout after 2000ms, use one or the othert

    browser.close()

