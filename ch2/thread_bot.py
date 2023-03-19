import queue
import threading

from attr import attrs, attrib


@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)

    def give(self, to: 'Cutlery', knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        self.knives += knives
        self.forks += forks


class ThreadBot(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manage_table)
        self.cultery = kitchen
        self.tasks = queue.Queue()

    def manage_table(self):
        while True:
            task = self.tasks.get()

            if task == 'prepare table':
                kitchen.give(to=self.cultery, knives=4, forks=4)
            elif task == 'clear table':
                self.cultery.give(to=kitchen, knives=4, forks=4)
            elif task == 'shutdown':
                return


kitchen = Cutlery(knives=100, forks=100)
bots = [ThreadBot() for _ in range(10)]

print("Kitchen inventory before service:", kitchen)

import sys

for bot in bots:
    for i in range(int(sys.argv[1])):
        bot.tasks.put('prepare table')
        bot.tasks.put('clear table')
    bot.tasks.put('shutdown')
    bot.start()

for bot in bots:
    bot.join()

print("Kitchen inventory after service:", kitchen)

# wried, should cause race condition, but it doesn't
