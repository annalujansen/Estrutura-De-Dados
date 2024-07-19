class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
        
class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
       return self.head == None
       
    def addInicio(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp   
    
    def addFinal(self,item):
        temp = Node(item)
        if self.head == None:
           self.head = temp
        else:
           ultimo = self.head
           while ultimo.getNext() != None:
               ultimo = ultimo.getNext()  
           ultimo.setNext(temp) # ultimo.next = temp
    
    def remover(self, pos):
        if self.head == None or pos < 0:
            return None
        removido = self.head
        anterior = None
        count = 0
        while count < pos and removido != None:
            count +=1
            anterior = removido
            removido = removido.getNext()
        if removido == None:
           return None
        if anterior == None:
           self.head = removido.getNext()
           return removido.getData()
        else:
            anterior.setNext(removido.getNext())
            return removido.getData()
       
    def removerDado(self, dado):
        if self.head == None or dado == None:
            return None
        removido = self.head
        anterior = None
        while removido != None and removido.getData() != dado:
            anterior = removido
            removido = removido.getNext()
        if removido == None:
           return None
        if anterior == None:
           self.head = removido.getNext()
           return removido.getData()
        else:
            anterior.setNext(removido.getNext())
            return removido.getData()   
       
       
    def imprimir(self):
        atual = self.head
        s = ""
        while atual != None:   
             s = s + " " + str(atual.getData())
             atual = atual.getNext() # atual = atual.next
        print(s) 
       
    def size(self):
        #atual = self.head
        #count = 0
        #while atual != None:   
        #     count +=1
        #     atual = atual.getNext() # atual = atual.next
        #return count
        def sizeRec(n):
           if n == None:
              return 0
           else:
              return 1 + sizeRec(n.getNext())

        return sizeRec(self.head)
       
lista = UnorderedList()
lista.addInicio(10)       
lista.addInicio(0) 
lista.addFinal(20)       
lista.imprimir() 
print("Tamanho:",lista.size()) 
print("Valor removido: ",lista.removerDado(20))
lista.imprimir() 
print("Tamanho:",lista.size()) 

'''
Classe Node
A classe Node representa um único nó em uma lista ligada. Cada nó possui dois atributos:

data: armazena o dado do nó.
next: referência para o próximo nó na lista.

Métodos da Classe Node
1 __init__(self, initdata):
Inicializa o nó com o dado (initdata) e define o próximo nó como None.

2 getData(self):
Retorna o dado armazenado no nó.

3 getNext(self):
Retorna a referência para o próximo nó na lista.

4 setData(self, newdata):
Define um novo valor para o dado do nó.

5 setNext(self, newnext):
Define a referência para o próximo nó na lista.

Classe UnorderedList
A classe UnorderedList representa uma lista ligada não ordenada. Possui um atributo:

head: referência para o primeiro nó da lista (ou None se a lista estiver vazia).

Métodos da Classe UnorderedList

__init__(self):
Inicializa a lista com head definido como None.

isEmpty(self):
Retorna True se a lista estiver vazia (ou seja, head é None).

addInicio(self, item):
Adiciona um novo nó com o dado item no início da lista.
Cria um novo nó (temp).
Define o next do novo nó como o nó atual head.
Atualiza head para o novo nó.

addFinal(self, item):
Adiciona um novo nó com o dado item no final da lista.
Cria um novo nó (temp).
Se a lista estiver vazia (head é None), define head como o novo nó.
Caso contrário, percorre a lista até o último nó e define o next do último nó para o novo nó.

remover(self, pos):
Remove o nó na posição pos.
Se a lista estiver vazia ou a posição for inválida (pos < 0), retorna None.
Percorre a lista até a posição desejada.
Atualiza as referências para remover o nó na posição pos.
Retorna o dado do nó removido.

removerDado(self, dado):
Remove o primeiro nó que contém o dado dado.
Se a lista estiver vazia ou o dado for None, retorna None.
Percorre a lista até encontrar o nó com o dado desejado.
Atualiza as referências para remover o nó.
Retorna o dado do nó removido.

imprimir(self):
Imprime todos os dados da lista em uma única linha.
Percorre a lista e concatena os dados em uma string s.
Imprime a string s.

size(self):
Retorna o tamanho da lista utilizando uma função recursiva interna (sizeRec).
A função sizeRec(n) retorna 0 se n for None, ou 1 + sizeRec(n.getNext()) caso contrário.
Chama sizeRec com o nó head.

Implementação

Vamos analisar a implementação do código fora das classes:


Cria uma nova instância de UnorderedList chamada lista.
lista.addInicio(10):

Adiciona o valor 10 no início da lista.
lista.addInicio(0):

Adiciona o valor 0 no início da lista.
lista.addFinal(20):

Adiciona o valor 20 no final da lista.
lista.imprimir():

Imprime os elementos da lista: "0 10 20".
print("Tamanho:", lista.size()):

Imprime o tamanho da lista: 3.
print("Valor removido: ", lista.removerDado(20)):

Remove o nó que contém o valor 20 e imprime o valor removido: 20.
lista.imprimir():

Imprime os elementos restantes da lista: "0 10".
print("Tamanho:", lista.size()):

Imprime o tamanho atual da lista: 2.
Essa implementação mostra como adicionar elementos no início e no final da lista, remover elementos por valor e imprimir o conteúdo da lista, além de verificar o tamanho antes e depois de uma remoção.

'''


       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
