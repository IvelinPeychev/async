from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo=500)

    page = browser.new_page()
    page.set_viewport_size({'width': 922, 'height': 950})
    page.goto('http://account.google.com')

    page.get_by_role('link', name='Go to your Google Account').first.click()

    email = page.get_by_label('Email or phone')
    email.fill('email@test.com')
    page.get_by_role('button', name='Next').click()

    password = page.get_by_label('Enter your password')
    page.get_by_role('button', name='Next').click()






