class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()

    def enqueue(self, data):
        self.inbound_stack.append(data)


queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
print(queue.inbound_stack)
queue.dequeue()
print(queue.inbound_stack)
print(queue.outbound_stack)
queue.dequeue()
print(queue.outbound_stack)

"""
import time
start_time = time.time()
for i in range(100000):
    #print i
    array_queue.enqueue(i)
for i in range(100000):
    #print i
    array_queue.dequeue()
print("--- %s seconds ---" % (time.time() - start_time))



import time
start_time = time.time()
for i in range(10000):
    for j in range(100):
        array_queue.push(i)
    for k in range(10):
        array_queue.pop()
print("--- %s seconds ---" % (time.time() - start_time))
"""