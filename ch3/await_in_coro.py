import asyncio


async def f():
    await asyncio.sleep(1)
    return 3


async def main():
    print(await f())


asyncio.run(main())
