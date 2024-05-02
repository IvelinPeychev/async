from playwright.sync_api import Page, expect

DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role(role='link', name='GET STARTED')
    link.click()

    # assert page.url == DOCS_URL
    expect(page).to_have_url(DOCS_URL) # expect is the API for assertion
    expect(page).to_have_title("Installation | Playwright Python")
