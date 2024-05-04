import pytest
from playwright.sync_api import *

DOCS_URL = 'https://playwright.dev/python/docs/intro'

# Instead of using it like this:

# def test_page_has_docs_link(browser_name: str, page: Page):
#     if browser_name != 'firefox':
#         page.goto('https://playwright.dev/python')
#         link = page.get_by_role('link', name='Docs')
#
#         assert link.is_visible()
#
#
# def test_get_started_visits_docs(is_firefox: bool, page: Page):
#     if is_firefox:
#         page.goto('https://playwright.dev/python')
#         link = page.get_by_role('link', name='GET STARTED')
#         link.click()
#
#         assert page.url == DOCS_URL


# We will use pytest decorators to set conditions of test running based on the browser
@pytest.mark.skip_browser('firefox')
def test_page_has_docs_link(page: Page):
    page.goto('https://playwright.dev/python')
    link = page.get_by_role('link', name='Docs')

    assert link.is_visible()

@pytest.mark.only_browser('firefox')
def test_get_started_visits_docs( page: Page):
    page.goto('https://playwright.dev/python')
    link = page.get_by_role('link', name='GET STARTED')
    link.click()

    assert page.url == DOCS_URL

