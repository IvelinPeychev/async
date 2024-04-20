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


# fill input fields
inp_f = page.get_by_label('Email address') # 2 fields
inp_f = page.get_by_placeholder('Enter email') # the exact one
inp_f.fill("test")
inp_f.clear()
inp_f.type('my#difds.fdsfsdfs', delay=500) # we can simulate human typing with type and delay
valid = page.get_by_label('Valid input').first
valid.input_value() # return value of the field

# Radios, checkboxes and switches
radio_btn = page.get_by_role(role='radio',name="Option one is this and that—be sure to include why it's great")
radio_btn.check()

checkbox = page.get_by_role(role='checkbox', name='Default checkbox')
checkbox.check()
checkbox.uncheck()
checkbox.is_checked() # assertion
checkbox.click()

# Option menu
opt_menu = page.get_by_label('Example select')
opt_menu.select_option('3') # Select option 3 from the select

multi_select = page.get_by_label('Example multiple select')
multi_select.select_option(['2','4']) # select two options


# drop-down
drp_dwn = page.locator('button#btnGroupDrop1')
drp_dwn.click()

link = page.locator('div.dropdown-menu:visible a:text("Dropdown link)')
link.first.click()

#upload files
file_input = page.get_by_label("Default file input example")
file_input.set_input_files('file.txt')

# for files that has to be selected from the machine
file_input = page.get_by_label("Default file input example")
with page.expect_file_chooser() as fc_info: # we are catching the fc_ingo
    file_input.click()

file_chooser = fc_info.value
file_input.set_input_files('file.txt')

# Keyboard shortcuts
textarea = page.get_by_label('Example textarea')
textarea.fill('word')
textarea.clear()
textarea.press('KeyW')
textarea.press('KeyM')
textarea.press('Shift+KeyD') # capital D
textarea.press('Control+ArrowLeft')  # move arrow top left
textarea.press('ArrowRight') # move the arrow one spot to the right



