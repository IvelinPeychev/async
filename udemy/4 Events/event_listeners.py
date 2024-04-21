from playwright.sync_api import sync_playwright
from time import perf_counter


def on_load(page_object):
    print('Page loaded:', page_object)

def on_request(request):
    print('Request sent:', request)
def on_filechooser(file_chooser):
    print('File chooser is opened')
    file_chooser.set_files('test.txt')



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=500
    )

    page = browser.new_page()

    # Listener should be called before the action, not all events are shown, just few examples

    page.on('load', on_load) # listen for page load event and trigger the func when the event occurs (when the page is loaded)
    page.once('load', on_load) # listen for page load event and trigger the func when the event occurs ONCE, no need to close it with remove_listner after

    # page.on('domcontentloaded', on_load)
    # page.on('close', on_load)
    # page.on('response', on_load)
    page.on('request', on_request) # listen for request event, and trigger the function when occurs
    page.on('filechooser', on_filechooser) # listen for filechooser event, and trigger the func when occurs

    page.goto('https://bootswatch.com/default')
    input_field = page.get_by_label('Default file input example')
    input_field.click()

    page.remove_listener('load', on_load)   # Good practice is to remove the listener once it is called

    browser.close()