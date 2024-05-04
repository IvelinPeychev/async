import json
from playwright.sync_api import *


def test_users_api(page: Page):
    response = page.goto('https://dummyjson.com/users/1')

    user_data = response.json()

    assert "firstName" in user_data.keys()
    assert "Terry" in user_data['firstName']

