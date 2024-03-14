import asyncio
from playwright.async_api import async_playwright

urls = ['https://knigi-igri.bg/', 'https://chitanka.info/books/category/knigi-igri',
         'https://knizhen-pazar.net/books/categories/13-knigi-igri']

async def homework(items):
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch()
            page1 = await browser.new_page()
            page2 = await browser.new_page()
            page3 = await browser.new_page()
            pages = [page1, page2, page3 ]
            await asyncio.gather(*(page.goto(url) for page, url in zip(pages, items)))
            await asyncio.gather(*(page.screenshot(path=f'screenshot_page_{index}.png') for index, page in enumerate(pages)))

            await browser.close()

        except Exception as e:
            print(f'Error while script execution: {e}')



if __name__ == '__main__':
    asyncio.run(homework(urls))


