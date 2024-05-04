from playwright.sync_api import *
DOCS_URL = 'https://playwright.dev/python/docs/intro'


def test_page_has_docs_link(playwright: Playwright, browser: Browser,
                            browser_type: BrowserType, browser_name: str,
                            browser_channel: str, is_firefox: bool, is_chromium: bool):
    page = browser.new_page()
    # BrowserContext can be used for additional setup
    page = browser.new_page()

    if browser_type == playwright.chromium:
        print("Browser type is chromium")
        pass # perform chromium specific code
    elif browser_type == playwright.firefox:
        pass # firefox specific code

    if is_chromium:
        print("the browser is chromium")


    page.goto('https://playwright.dev/python')
    link = page.get_by_role('link', name='Docs')

    assert link.is_visible()


def test_get_started_visits_docs(browser, page: Page):
    # browser will be the same browser used in the previous test function
    page.goto('https://playwright.dev/python')
    link = page.get_by_role('link', name='GET STARTED')
    link.click()

    assert page.url == DOCS_URL