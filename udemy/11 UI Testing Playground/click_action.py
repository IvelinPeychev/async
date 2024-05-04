from playwright.sync_api import TimeoutError, Page,expect


def test_hidden_layer(page: Page):
    page.goto("http://uitestingplayground.com/click")

    btn = page.get_by_role('button', name='Button That Ignores DOM Click')
    btn.click()

    expect(btn).to_have_class('btn btn-success')