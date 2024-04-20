from playwright.sync_api import sync_playwright

def interact_with_iframe():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://www.littlewebhut.com/articles/simple_web_page/")

        # Wait for the iframe to be loaded
        iframe_element_handle = page.wait_for_selector('iframe[src="/php/samples/xhtml_article_simple_web_page.php"]')

        # Check if the iframe was found
        if not iframe_element_handle:
            print("No iframe found")
            browser.close()
            return

        # Get the frame object from the iframe element handle
        frame = iframe_element_handle.content_frame()

        if not frame:
            print("No content frame found")
            browser.close()
            return

        # Interact with elements within the iframe
        # Ensure you're using selectors that are valid within the iframe's document
        frame.click('text="One"')

        print("Clicked 'One' inside iframe.")

        browser.close()

if __name__ == "__main__":
    interact_with_iframe()
