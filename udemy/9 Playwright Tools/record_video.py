import pytest
from playwright.sync_api import Browser, Page


@pytest.fixture()
def record_video(browser: Browser):
    context = browser.new_context(
        record_video_dir='video/'
    )
    page = context.new_page()
    yield page
    page.close()


def test_page_has_get_started_link(page: Browser):
    # Navigate to the Playwright documentation for Python
    page.goto("https://playwright.dev/python")

    theme_btn = page.get_by_title('Switch between dark and light mode (currently dark mode)')
    theme_btn.click()

    # Find the link with role 'link' and text 'GET STARTED'
    link = page.get_by_role(role='link', name='GET STARTED')

    # Click on the found link
    link.click()

    # Verify that the URL is as expected after the click
    assert page.url == "https://playwright.dev/python/docs/intro"
