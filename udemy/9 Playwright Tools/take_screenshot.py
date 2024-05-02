from playwright.sync_api import Page


def test_page_has_get_started_link(page: Page):
    # Navigate to the Playwright documentation for Python
    page.goto("https://playwright.dev/python")

    page.screenshot(path='playwright.png')

    # Find the link with role 'link' and text 'GET STARTED'
    link = page.get_by_role(role='link', name='GET STARTED')

    # Click on the found link
    link.click()

    page.screenshot(path='docs.png', full_page=True)

    # Verify that the URL is as expected after the click
    assert page.url == "https://playwright.dev/python/docs/intro"
