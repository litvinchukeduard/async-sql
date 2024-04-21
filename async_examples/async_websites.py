import aiohttp
import asyncio

websites = ['http://python.org', 'http://google.com', 'http://github.com']

async def get_info(url):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:# async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print(len(html))

async def main():
    calls = []
    for website_url in websites:
        calls.append(get_info(website_url))
    await asyncio.gather(*calls)

asyncio.run(main())
