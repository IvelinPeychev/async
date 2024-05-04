from playwright.sync_api import TimeoutError, Page,expect


def test_input_field(page: Page):
    page.goto("http://uitestingplayground.com/textinput")
    
    query = 'great stuff'

    input = page.get_by_label('Set New Button Name')
    input.fill(query)

    btn = page.locator('button.btn-primary')
    btn.click()

    expect(btn).to_have_text(query)