def search(lista,item):
    anterior = None
    atual = lista.head
    while atual != None and atual.getData() != item:
        anterior = atual
        atual = atual.getNext()
    if atual == None: #não encontrou
        return None
    if anterior == None: #encontrou e é o primeiro
        return atual.getData()
    anterior.setNext(atual.getNext)
    atual.setNext(lista.head)
    
    return atual.getData()
