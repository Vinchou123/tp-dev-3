import asyncio

async def sleep_and_print():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    await asyncio.gather(sleep_and_print(), sleep_and_print())

asyncio.run(main())