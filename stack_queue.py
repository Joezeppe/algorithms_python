
# Eww slow implementation

class ListQueue(object):

    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size +=1

    def dequeue(self):
        data_to_return = self.items.pop()
        self.size -=1
        return data_to_return


# Stack queues

class Queue:

    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()

    def get_count(self):
        return len(self.inbound_stack) + len(self.outbound_stack)

# Implement Queue Example


q = Queue()


q.enqueue(5)
q.enqueue(6)
q.enqueue(7)

print(q.inbound_stack, q.outbound_stack, q.get_count())

q.dequeue()

print(q.inbound_stack, q.outbound_stack, q.get_count())

q.dequeue()

print(q.inbound_stack, q.outbound_stack, q.get_count())

q.enqueue(8)

print(q.inbound_stack, q.outbound_stack, q.get_count())

q.dequeue()

print(q.inbound_stack, q.outbound_stack, q.get_count())
