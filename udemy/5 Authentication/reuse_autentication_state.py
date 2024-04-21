from playwright.sync_api import sync_playwright

YOUR_EMAIL = 'peychev.vn@gmail.com'
YOUR_PASSWORD = 'Somepassword'

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(
        storage_state="playwright/.auth/storage_state.json" # first use save auth script and save the auth state
    )

    page = context.new_page()

    # Visit google accounts
    page.goto("https://accounts.google.com")
    page.pause()
    browser.close()