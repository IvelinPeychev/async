from playwright.sync_api import sync_playwright, expect


def test_ajax_data():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://uitestingplayground.com/")
        page.get_by_role('link', name='AJAX Data').click()
        page.get_by_role("button", name="Button Triggering AJAX Request").click()

        text = page.locator("p.bg-success")
        text.wait_for()
        expect(text).to_be_visible()


