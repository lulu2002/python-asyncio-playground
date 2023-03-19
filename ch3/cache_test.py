import asyncio


class Cache:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1

    def get(self):
        return self.value


class Device:

    def __init__(self, ):
        self.value = 0

    def read(self):
        self.value += 1

        if self.value % 10 == 0:
            return True


class Observer:

    async def on_update(self, value):
        pass


class Observable:

    def __init__(self):
        self.observers = []

    async def update(self, value):
        for observer in self.observers:
            await observer.on_update(value)

    def add_observer(self, observer):
        self.observers.append(observer)


class Reader:

    def __init__(self, cache: Cache, device: Device, observable: Observable):
        self.cache = cache
        self.device = device
        self.observable = observable

    async def start(self):
        while True:
            value = self.device.read()

            if value:
                self.cache.add()
                print("trigger")
                await self.observable.update(self.cache.get())
                print("trigger done")

            await asyncio.sleep(0.1)


class ObserverA(Observer):

    async def on_update(self, value):
        print(f"ObserverA: {value}")
        await asyncio.sleep(1)


class ObserverB(Observer):

    async def on_update(self, value):
        print(f"ObserverB: {value}")
        await asyncio.sleep(1)


cache = Cache()
device = Device()
observable = Observable()
reader = Reader(cache, device, observable)

observable.add_observer(ObserverA())
observable.add_observer(ObserverB())

asyncio.run(reader.start())
