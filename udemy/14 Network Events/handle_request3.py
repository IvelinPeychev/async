from playwright.sync_api import Request, Response, Page, Route,  expect


# route is page navigation object
# In this example we don't want to load any image type
def on_route(route: Route):
    if route.request.resource_type == 'image':
        route.abort()
    else:
        route.continue_()



def test_docs_link(page: Page):
    page.route('**', on_route)

    page.goto('https://playwright.dev/python')

    page.screenshot(path='playwright3.png',full_page=True)