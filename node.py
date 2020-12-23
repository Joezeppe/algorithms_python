class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


n1 = Node('a')
n2 = Node('b')
n3 = Node('c')

n1.next = n2
n2.next = n3

current = n1

while current:
    print(current)
    current = current.next
