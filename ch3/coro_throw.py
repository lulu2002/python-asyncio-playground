async def f():
    return 3


coro = f()
coro.send(None)
coro.throw(Exception, "blah")
