from playwright.sync_api import Page


# as a result of pytest-playwright
def test_page_has_get_started_link(page: Page):
    # Navigate to the Playwright documentation for Python
    page.goto("https://playwright.dev/python")

    # Find the link with role 'link' and text 'GET STARTED'
    link = page.get_by_role(role='link', name='GET STARTED')

    # Click on the found link
    link.click()

    # Verify that the URL is as expected after the click
    assert page.url == "https://playwright.dev/python/docs/intro"
