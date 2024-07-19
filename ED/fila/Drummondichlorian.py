class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def peek(self):
        return self.items[0] if self.items else None

    def is_empty(self):
        return len(self.items) == 0


class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        # Insert the item and keep the list sorted in descending order
        self.items.append(item)
        self.items.sort(reverse=True)

    def pop(self):
        return self.items.pop(0) if self.items else None

    def peek(self):
        return self.items[0] if self.items else None

    def is_empty(self):
        return len(self.items) == 0


def identify_structure(cases):
    results = []

    for operations in cases:
        n = operations[0]
        operations = operations[1:]

        stack = Stack()
        queue = Queue()
        priority_queue = PriorityQueue()
        
        is_stack = True
        is_queue = True
        is_priority_queue = True

        for op in operations:
            action, x = op.split()
            x = int(x)

            if action == 'in':
                if is_stack:
                    stack.push(x)
                if is_queue:
                    queue.enqueue(x)
                if is_priority_queue:
                    priority_queue.push(x)
            elif action == 'out':
                if is_stack:
                    if stack.peek() == x:
                        stack.pop()
                    else:
                        is_stack = False
                if is_queue:
                    if queue.peek() == x:
                        queue.dequeue()
                    else:
                        is_queue = False
                if is_priority_queue:
                    if priority_queue.peek() == x:
                        priority_queue.pop()
                    else:
                        is_priority_queue = False

        if sum([is_stack, is_queue, is_priority_queue]) > 1:
            results.append("uai?")
        elif is_stack:
            results.append("LIFO")
        elif is_queue:
            results.append("FIFO")
        elif is_priority_queue:
            results.append("AIPO")
        else:
            results.append("no hay!")

    return results

cases = []
i = 0
while i < 5:
    n = int(input())
    operations = [n]
    for _ in range(n):
        instrucao = input()
        operations.append(instrucao)
    cases.append(operations)
    i += 1

result = identify_structure(cases)
for i in result:
    print(i)