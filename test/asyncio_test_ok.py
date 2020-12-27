import asyncio
from functools import wraps, partial


def async_wrap(func):
    """https://dev.to/0xbf/turn-sync-function-to-async-python-tips-58nn"""
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run


def fib_sync(term):
    if term <= 1:
        return term
    else:
        rs = fib_sync(term - 1) + fib_sync(term - 2)
        return rs


@async_wrap
def fib_wrapper_async(term):
    return fib_sync(term)


async def hello():
    print('Hello ...')
    # await asyncio.sleep(5)
    await fib_wrapper_async(31)
    print('... World!')


async def main():
    await asyncio.gather(hello(), hello())


if __name__ == '__main__':
    asyncio.run(main())

"""
python test/asyncio_test_ok.py
python -m test.asyncio_test_ok
"""
