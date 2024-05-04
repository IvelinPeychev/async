from playwright.sync_api import Page,BrowserContext, expect

DOCS_URL = 'https://playwright.dev/python/docs/intro'


def test_page_has_docs_link(context: BrowserContext, page: Page):
    # BrowserContext can be used for additional setup
    context.add_cookies()
    context.grant_permissions('notifications')
    page = context.new_page()
    page.goto('https://playwright.dev/python')

    link = page.get_by_role('link', name='Docs')

    assert link.is_visible()


def test_get_started_visits_docs(page: Page):
    page.goto('https://playwright.dev/python')
    link = page.get_by_role('link', name='GET STARTED')
    link.click()

    assert page.url == DOCS_URL
