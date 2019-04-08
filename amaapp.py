import asyncio
import aiohttp

BASE_URL = 'https://test.api.amadeus.com'


async def fetch(session, url, PARAMS):
    async with session.get(BASE_URL + url, headers={'Authorization': 'Bearer gHARAtpAyAJQHVVcQbxwBvMik0Op'},
                           params=PARAMS) as resp:
        return await resp.text()


async def main():
    """
    Demonstrate usage of simple async request
    """
    # endpoints = ['/v1/reference-data/airlines']
    collected_data = []
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, '/v1/reference-data/airlines', {'airlineCodes':"BA"})
        collected_data.append(html)

async def main2():
    """
    Demonstrate several tasks running concurrently
    """
    tasks = []
    async with aiohttp.ClientSession() as session:
        tasks.append(asyncio.create_task(fetch(session, '/v1/reference-data/airlines', {'airlineCodes':"BA"})))
        tasks.append(asyncio.create_task(fetch(session, '/v1/reference-data/airlines', {'airlineCodes':"AA"})))
        tasks.append(asyncio.create_task(fetch(session, '/v1/reference-data/airlines', {'airlineCodes':"AZ"})))
        tasks.append(asyncio.create_task(fetch(session, '/v1/reference-data/airlines', {'airlineCodes':"AF"})))

        responses = await asyncio.gather(*tasks)
        print(responses)


# # Old way before python 3.7
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# asyncio.run(main())
asyncio.run(main2())
