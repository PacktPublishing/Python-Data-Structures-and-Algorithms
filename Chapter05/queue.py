
class ListQueue:

    def __init__(self):
        self.items = []
        self.size = 0

    def empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

    def size(self):
        return self.size



list_queue = ListQueue()

import time
start_time = time.time()
for i in range(100000):
    #print(i)
    list_queue.enqueue(i)
for i in range(100000):
    list_queue.dequeue()
print("--- %s seconds ---" % (time.time() - start_time))


"""
import time
start_time = time.time()
for i in range(1000):
    for j in range(100):
        array_queue.enqueue(i)
    for k in range(10):
        array_queue.dequeue()
print("--- %s seconds ---" % (time.time() - start_time))
"""
