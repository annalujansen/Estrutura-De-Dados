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
       if e == "(":
          p.push(e)
       elif e == ")":
          if p.isEmpty() or p.peek() != "(":
            return False
          p.pop()
    return p.isEmpty()
 
def posfixa(equacao):
    p = Stack()
    saida = []
    for e in equacao: 
       if e == "+" or e == "-" or e =="*" or e == "/": #operador
          if e == "+" or e == "-": # + ou -
             while (not p.isEmpty()) and (p.peek() != "("):
                saida.append(p.pop())
          else: # * ou /
             while (not p.isEmpty()) and (p.peek() == "*" or p.peek() == "/"):
                saida.append(p.pop())
          p.push(e)
       elif e == "(":
          p.push("(")
       elif e == ")":
          while p.peek() != "(":
            saida.append(p.pop())
            #x = p.pop()
            #saida.append(x)
          p.pop()
       else: #operando
          saida.append(e)
    while not p.isEmpty():
        saida.append(p.pop())
    return saida

def calcula(posfixa):
    p = Stack()
    for e in posfixa:
       if e == "+":
           op2 = p.pop()
           op1 = p.pop()
           r = int(op1)+int(op2)
           p.push(r)
       elif e == "-":
           op2 = p.pop()
           op1 = p.pop()
           r = int(op1)-int(op2)
           p.push(r)
       elif e == "*":
           op2 = p.pop()
           op1 = p.pop()
           r = int(op1)*int(op2)
           p.push(r)
       elif e == "/":
           op2 = p.pop()
           op1 = p.pop()
           r = int(op1)/int(op2)
           p.push(r)
       else:
          p.push(e)
    return p.pop()   

eq = input()
if valida(eq):
   pos = posfixa(eq)
   print(pos)
   print("Resultado: ",calcula(pos))
else:
   print("Equação inválida")




         
