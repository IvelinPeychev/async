from playwright.sync_api import Page, expect


def test_run_class_attribute(page: Page) -> None:
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("http://uitestingplayground.com/")

    page.get_by_role("link", name="Class Attribute").click()

    primary_btn = page.get_by_role("button", name="Button").first # with codegen
    primary_btn = page.locator('button.btn-primary') # css
    primary_btn = page.locator('//button[ contains(@class, "btn-primary")]') # xpath
    expect(primary_btn).to_be_visible()
    primary_btn.click()

    page.get_by_role("button", name="Button").nth(1).click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Button").nth(2).click()

    # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
