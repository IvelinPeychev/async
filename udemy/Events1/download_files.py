from playwright.sync_api import sync_playwright

def on_download(download):
    print("Download received!")
    download.save_as('moon.png')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False, slow_mo=1000
    )

    page = browser.new_page()
    page.goto('https://unsplash.com/photos/qe2RkzzMx9A')

    page.once('download', on_download)

    dwn_btn = page.get_by_role('link', name='Download free')

    with page.expect_download() as download_info:
        dwn_btn.click()

    # download = download_info.value
    #
    # # If you want to save the file after Playwright stops (they are temporary)
    # download.save_as('file.png')

    browser.close()


