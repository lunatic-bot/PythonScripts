## list implementation of queue 

# stock_price = []

# stock_price.insert(0, 131.10)
# stock_price.insert(0, 132.32)
# stock_price.insert(0, 135.20)

# print(stock_price)

# print(stock_price.pop())



# from collections import deque

# q = deque()

# q.appendleft(5)
# q.appendleft(10)
# q.appendleft(100)

# print(q.pop())



from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, element):
        self.buffer.appendleft(element)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})
    

print(pq.buffer)
print(pq.dequeue())
