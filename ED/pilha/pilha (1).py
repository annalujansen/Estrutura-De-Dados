class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[-1]

     def size(self):
         return len(self.items)
         
def valida(equacao):
    p = Stack()
    for e in equacao:
       if e == "(" or e == "[" or e == "{":
          p.push(e)
       elif e == ")":
           if p.isEmpty() or p.peek() != "(":
              return False
           p.pop()
       elif e == "]":
           if p.isEmpty() or p.peek() != "[":
              return False
           p.pop()
       elif e == "}":
           if p.isEmpty() or p.peek() != "{":
              return False
           p.pop()
    return p.isEmpty()

eq = input()
print(valida(eq))
