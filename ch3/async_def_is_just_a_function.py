import inspect


async def f():
    return 123


print(type(f))
print(f"Is Coroutine Fun {inspect.iscoroutinefunction(f)}")
