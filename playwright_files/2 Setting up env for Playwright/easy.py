from playwright.sync_api import sync_playwright

def navigate():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        print(page.title())
        print("Navigation Successful")
        browser.close()

if __name__ == "__main__":
    navigate()