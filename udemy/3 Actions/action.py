from playwright.sync_api import sync_playwright


playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=1500)
page = browser.new_page()
url = 'https://bootswatch.com/default'
page.goto(url)

# Take the first or last button from a block
btn = page.get_by_role('button', name='Block button').first
page.get_by_role('button', name='Block button').last

btn.click()
btn.dblclick(delay=500) # add a delay between button clicks

btn.click(button="right") # it clicks right click of the mouse button over the button
btn.click(modifiers=['Shift', 'Control', 'Meta']) # we can select multiple keys to be pressed with modifiers list

outline_btn = page.locator('button.btn-outline-primary')
outline_btn.hover()

