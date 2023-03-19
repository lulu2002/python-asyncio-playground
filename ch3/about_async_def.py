import inspect


def break_line():
    print("")
    print('--------------------------------')
    print("")


async def async_def_fun():
    return 123


print(type(async_def_fun))
print(f"Is Coroutine Fun {inspect.iscoroutinefunction(async_def_fun)}")
print(f"Return value of f {async_def_fun()}")
print(f"Type of return value of f {type(async_def_fun())}")
print(f"Is Coroutine {inspect.iscoroutine(async_def_fun())}")

break_line()

coro = async_def_fun()
try:
    ret = coro.send(None)
except StopIteration as e:
    print('The answer is', e.value)
