from playwright.sync_api import sync_playwright
import time
import re


def split_on_uppercase(s, keep_compound=True):
    # Pattern explanation:
    # (?<=[a-z]) - positive lookbehind assertion, checks for lowercase letter before uppercase
    # (?=[A-Z]) - positive lookahead assertion, checks for uppercase letter ahead
    # This effectively inserts a space before each uppercase letter that follows a lowercase letter.
    pattern = r'(?<=[a-z])(?=[A-Z])'

    # If keep_compound is True, it won't split compound words like "Sci-Fi"
    if keep_compound:
        # This adjusts the pattern to avoid splitting in the middle of compound words like "Sci-Fi"
        pattern += r'(?<!-.)'

    # Splitting the string based on the pattern
    split_string = re.sub(pattern, ' ', s).split()

    return split_string


# Your string
s = "ActionAdventureSci-Fi"

# Splitting the string
split_s = split_on_uppercase(s)


def navigate_and_extract_details():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            page.goto("https://www.imdb.com/", timeout=10000)  # Added timeout for navigation

            # Using selectors that are less likely to change. Adjust as needed.
            search_selector = 'input[name="q"]'
            if not page.is_visible(search_selector):  # Checking if the search input is visible
                raise Exception("Search input not found on IMDb homepage.")

            page.fill(search_selector, "Inception")
            page.press(search_selector, "Enter")
            page.wait_for_selector(".ipc-metadata-list-summary-item__t", timeout=5000)  # Wait for search results

            # Clicking the first search result link
            page.click(".ipc-metadata-list-summary-item__t:first-child")

            # Extract and print movie details
            title = page.title()
            name, year = re.match(r"(.+?)\s+\((\d{4})\)", title).groups()
            print(f'The name of the movie is: {name} \nThe year of the movie is: {year}')

            # Extracting additional details using safer methods
            director = page.text_content('text=Director')  # Simplified for example; adjust selector as needed
            print(f"The Movie director is: {director.strip()}")

            # Handling elements that may not exist using conditional checks
            ratings_selector = 'xpath=/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]'
            if page.is_visible(ratings_selector):
                ratings = page.locator(ratings_selector).text_content()
                print(f"The movie rating is: {ratings.strip()}")
                page.locator(ratings_selector).screenshot(path='ratings.png')
            else:
                print("Ratings not found.")

            # Example of using the utility function
            genres_text = page.text_content('div[data-testid="genres"]')
            print(f"The list of genres are: {split_on_uppercase(genres_text)}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            browser.close()  # Ensures the browser closes even if an error occurs


if __name__ == "__main__":
    navigate_and_extract_details()

