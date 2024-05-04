from playwright.sync_api import Page,expect


def test_hidden_layer(page: Page):
    page.goto("http://uitestingplayground.com/scrollbars")

    btn = page.get_by_role('button', name='Hiding Button')
    btn.scroll_into_view_if_needed()

    expect(btn).to_be_visible()


