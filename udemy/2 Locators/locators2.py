from playwright.sync_api import sync_playwright


playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=1500)
page = browser.new_page()
url = 'https://bootswatch.com/default'
page.goto(url)

# get by role
btn = page.get_by_role('button', name='Default button')
btn.highlight()
heading = page.get_by_role('heading', name='Heading 2')
heading.highlight()
radio_btn = page.get_by_role('radio', name="Option one is this and that—be sure to include why it's great")
radio_btn.highlight()
checkbox = page.get_by_role('checkbox', name='Default checkbox')
checkbox.highlight()
checkbox.check()

# get by label
email_input = page.get_by_label('Email address')
email_input.highlight()
page.get_by_label('Example textarea').highlight()

# get by placeholder
page.get_by_placeholder('Enter email').highlight()
page.get_by_placeholder('Password').highlight()

# get by text
page.get_by_text('with faded secondary').highlight()
page.get_by_text('Middle').highlight()
page.get_by_text('fine print').highlight() # it will mark if contains
page.get_by_text('fine print', exact=True).highlight() # it will mark if only is the same

# get by alt text (for images)
page.goto('http://unsplash.com')
page.get_by_alt_text('a skateboard sitting on top of a blue and red ramp').highlight()

#get by title
page.goto(url)
page.get_by_title('attribute').highlight()

# CSS
page.locator('css=h1').highlight() # tag name
page.locator('footer').highlight() # tag name
page.locator('button.btn-outline-success').highlight() # class with .
page.locator('button#btnGroupDrop1').highlight() # id with #
page.locator('input[readonly]').highlight() # input with 'readonly' attribute
page.locator('input[value="correct value"]').highlight() # input with exact attibute value

# CSS hierarchy
page.locator('nav.bg-dark').highlight()
page.locator('nav.bg-dark a.nav-link.active').highlight()

# CSS pseudo classes
page.locator('h1:text("Navbars")').highlight()
page.locator('h1:text("Nav")').highlight() # select 2 as there are 2 that has it
page.locator('h1:text-is("Nav")').highlight() # select 0 as it is looking for exact text
page.locator('h1:text-is("Navs")').highlight() # select 1 as it is found

page.locator('div.dropdown-menu').highlight() # it will select all elements
page.locator('div.dropdown-menu:visible').highlight() # it will select just the visible (open) drop down at the moment

page.locator('button.btn-primary').highlight() # found 76 elements
page.locator(':nth-match(button.btn-primary, 5)').highlight() # click on the exact 5th element

page.locator(':nth-match(button:text("Primary"), 1)').highlight()

# Xpath
page.locator('xpath=//h1').highlight()
page.locator('//h1').highlight()
page.locator('//h1[@id="navbars"]').highlight() # using in id attribute
page.locator('//input[@readonly]').highlight() # using readonly attribute
page.locator('//input[@value="wrong value"]').highlight() # using attribute's value of the value attribute


# Xpath functions
page.locator('//h1[text() = "Heading 1"]').highlight() # using text()
page.locator('//h1[contains(text(), "Head")]').highlight() # using 'contains' func to call 'text' func to check for 'Head' text
page.locator('//button[contains(@class, "btn-outline-primary")]').highlight() # using 'class' attribute with 'contains' func
page.locator('//input[contains(@value, "correct")]').highlight() # using 'contains' with 'value' attribute containing 'correct'

#Other locators
page.get_by_role('button', name='Primary').locator('nth=0').highlight() #select 1st element when more are found
page.locator('button').locator('nth=18').highlight() # locate the 19th button on the page
page.get_by_label('Email address').locator('..').highlight() # locate the parent element of Email address
page.locator('id=btnGroupDrop1').highlight() # directly using id
page.locator('div.dropdown-menu').highlight()

page.locator('div.dropdown-menu').highlight() # shows all dropdown menus
page.locator('div.dropdown-menu').locator('visible=true').highlight() # show only the visible one

page.get_by_role('heading').highlight() # show the all heading
page.get_by_role('heading').filter(has_text="Heading").highlight()  # only if has text Heading

page.locator('div.bs-component').highlight()
page.locator('div.bs-component').filter(has=page.get_by_label('Password')).highlight()

