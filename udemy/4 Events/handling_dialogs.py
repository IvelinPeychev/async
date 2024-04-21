from playwright.sync_api import sync_playwright

def on_dialog(dialog):
    print("Dialog opened", dialog)
    dialog.accept() # Click Ok
    # dialog.dismiss() # Click Cancel

def on_prompt(prompt):
    print("Prompt opened", prompt)
    prompt.accept('Playwright is cool') # Fill text then click Ok
    # prompt.dismiss() # Click Cancel

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=10000
    )

    page = browser.new_page()
    page.goto('https://testpages.herokuapp.com/styled/alerts/alert-test.html')

    # page.on('dialog',on_dialog)
    page.on('dialog',on_prompt)

    # confirm_btn = page.get_by_text('Show confirm box')
    # confirm_btn.click()

    promt_btn = page.get_by_text('Show prompt box')
    promt_btn.click()

    browser.close()