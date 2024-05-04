import pytest
from playwright.sync_api import Browser, Request, Response, Page, Route,  expect


@pytest.fixture()
def record_video(browser: Browser):
    context = browser.new_context(
        record_video_dir='video/'
    )
    page = context.new_page()
    yield page
    context.close()


# route is page navigation object
# we get the actual response and modify it
def on_route(route: Route):
    response = route.fetch()
    print('Response', response)
    body = response.text().replace(' enables reliable end-to-end testing for modern web apps.',
                                   ' is an awesome framework for web automation!')

    route.fulfill(
        response=response,
        body=body
    )


def test_docs_link(record_video: Browser):
    page = record_video
    page.route('https://playwright.dev/python', on_route)

    page.goto('https://playwright.dev/python')