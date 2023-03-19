import inspect


def yield_fun():
    for i in range(10):
        yield i


print(f"Return Value of yield_fun(): {yield_fun()}")
print(f"Type of yield_fun(): {type(yield_fun())}")
print(f"Is Generator Fun {inspect.isgeneratorfunction(yield_fun)}")
