from playwright.sync_api import Request, Response, Page, Route,  expect


# route is page navigation object
# In this example we don't want to load any png files from the playwright page
def on_route(route: Route):
    print('Request aborted:', route.request)
    route.abort()


def test_docs_link(page: Page):
    page.route('**/*.png', on_route)

    page.goto('https://playwright.dev/python')

    page.screenshot(path='playwright2.png',full_page=True)