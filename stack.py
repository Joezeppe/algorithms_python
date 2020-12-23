
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

        
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None
    

    def peek(self):
        if self.top:
            return self.top.data
        return None


def check_brackets(statement):
    stack = Stack()
    for el in statement:
        if el in ("{","[","("):
             stack.push(el)
        if el in ("}","]",")"):
            last = stack.pop()
            if last is '{' and el is '}':
                continue
            elif last is '[' and el is ']':
                continue
            elif last is '(' and el is ')':
                continue
            else:
                return False
       
    # empty stack means all brackets have counter parts
    if stack.size > 0:
        return False

    return True


s0 = (
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test))"
)

for s in s0:
 m = check_brackets(s)
 print("{}: {}".format(s, m))
