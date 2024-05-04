from playwright.sync_api import Request, Response, Page, Route,  expect


# route is page navigation object
# we fulfill the request with custom response
def on_route(route: Route):
    route.fulfill(
        status=200,
        body='<html><body><h1>Custom Response!</h1></body></html>'
    )


def test_docs_link(page: Page):
    page.route('https://playwright.dev/python', on_route)
    page.goto('https://playwright.dev/python')
    page.pause()