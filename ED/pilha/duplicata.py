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

def duplicado(exp,a,f):
    # a = abre
    # f = fecha
    p = Stack()
    for c in exp:
        if c == f:
            if not p.isEmpty() and p.peek() == a:
                return True 
            while p.peek() != a:
                p.pop()
            p.pop()
        else:
            p.push(c)
    return False

n=int(input())
for _ in range(n):
    expressao = input()
    if duplicado(expressao,'(',')') or duplicado(expressao,'[',']') or duplicado(expressao,'{','}'):
        print('A expressão possui duplicata.')
    else:
        print('A expressão não possui duplicata.')