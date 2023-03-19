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


class Analyzer:

    def __init__(self, cache: Cache, observable: Observable):
        self.cache = cache
        self.observable = observable

    async def start(self):
        while True:
            await self.observable.update(-1)
            await asyncio.sleep(1.1)


class AnalyzerSubscriber(Observer):

    def __init__(self, cache: Cache):
        self.cache = cache

    async def on_update(self, value):
        print(f"AnalyzerSubscriber - get cache value: {self.cache.get()}")
        await asyncio.sleep(1)


cache = Cache()
device = Device()
reader_observable = Observable()
reader = Reader(cache, device, reader_observable)

reader_observable.add_observer(ObserverA())
reader_observable.add_observer(ObserverB())

analyzer_observable = Observable()
analyzer = Analyzer(cache, analyzer_observable)
analyzer_subscriber = AnalyzerSubscriber(cache)
analyzer_observable.add_observer(analyzer_subscriber)


async def main():
    tasks = [
        asyncio.create_task(reader.start()),
        asyncio.create_task(analyzer.start())
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
