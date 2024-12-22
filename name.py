from playwright.async_api import async_playwright
import asyncio


async def async_work():
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://whatmyuseragent.com/')
        await page.screenshot(path='./demo2.png')
        await browser.close()


asyncio.run(async_work())
