from playwright.sync_api import Playwright, Page,sync_playwright, expect


# def test_dynamic_id(playwright: Playwright) -> None:
def test_dynamic_id(page: Page) -> None:
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("http://uitestingplayground.com/")
    page.get_by_role("link", name="Dynamic ID").click()
    dynamic_btn = page.get_by_role("button", name="Button with Dynamic ID")

    expect(dynamic_btn).to_be_visible()
    dynamic_btn.click(button="right")

    # ---------------------
    # context.close()
    # browser.close()

