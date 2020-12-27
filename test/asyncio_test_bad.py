import asyncio


async def fib_async(term):
    if term <= 1:
        return term
    else:
        rs = await fib_async(term - 1) + await fib_async(term - 2)
        return rs


async def hello():
    print('Hello ...')
    # await asyncio.sleep(5)
    await fib_async(31)
    print('... World!')


async def main():
    await asyncio.gather(hello(), hello())


if __name__ == '__main__':
    asyncio.run(main())

"""
python test/asyncio_test_bad.py
python -m test.asyncio_test_bad
"""
