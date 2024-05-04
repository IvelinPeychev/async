from playwright.sync_api import *


USERS_API_URL = "https://dummyjson.com/users/1"


def on_api_call(route: Route):
    # # will return the sample data below as a response as we modify the response by mocking the API
    # route.fulfill(
    #     json={
    #         'firstName': 'Damien',
    #         'lastName': 'Smith'
    #     }
    # )

    response = route.fetch()
    user_data = response.json()

    user_data["lastName"] = "Smith"
    user_data["age"] = 20

    route.fulfill(
        response=response,
        json=user_data,
    )


def test_user_api(page: Page):
    page.route(USERS_API_URL, on_api_call)

    response = page.goto(USERS_API_URL)
    print("Got data:", response.json())