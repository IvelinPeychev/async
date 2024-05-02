from playwright.sync_api import Page, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role(role='link', name='GET STARTED')
    expect(link).to_be_enabled()

    link = page.get_by_role(role='link', name='GET Python')
    expect(link).not_to_be_visible()
    expect(link).to_be_hidden()
