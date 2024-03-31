from playwright.sync_api import sync_playwright

URLS = ["https://example.com", "https://example.org", "https://playwright.dev"]

def navigate():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        for url in URLS:
            page = browser.new_page()
            page.goto(f"{url}")
            image = page.screenshot(path=f"{url[8:]}.png")
        print("All navigations and screenshots successful")
        browser.close()

if __name__ == "__main__":
    navigate()