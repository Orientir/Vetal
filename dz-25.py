import asyncio
from requests_html import HTMLSession

async def coro1():
    while True:
        await asyncio.sleep(0.02)
        print("Coro 1 Working!")


async def coro2():
    while True:
        await asyncio.sleep(0.01)
        print("Coro 22222222 Working!")

async def coro3():
    while True:
        await asyncio.sleep(0.03)
        session = HTMLSession()
        response = session.get('https://py4you.com')
        print("Coro 333333333 Working! Title is ", response.html.xpath('//title')[0].text)

async def main():
    task1 = coro1()
    task2 = coro2()
    task3 = coro3()
    await asyncio.gather(task1, task2, task3)


asyncio.run(main())