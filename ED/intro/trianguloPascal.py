#def triangulo(n):
#    pascal = []
#    if n <= 0:
#        return pascal
#    pascal.append([1])
#    #print(f'Pascal antes do laço - {pascal}')
#    for i in range(1,n):
#        anterior = pascal[-1]
#        #print(f'anterior - {anterior}')
#        linha = [1]
#        #print(f'linha - {linha}')
#        for j in range(0,len(anterior)-1):
#            linha.append(anterior[j] + anterior[j+1])
#            #print(f'linha depois do laço j - {linha}')
#        linha.append(1)
#        #print(f'linha assim que sai do laço j - {linha}')
#        pascal.append(linha)
#        #print(f'resultado pascal - {pascal}')
#    return pascal
#
#n = int(input())
#print(triangulo(n))
#triangulo(n)


def triangulo(n):
    pascal = [[1]*(i+1) for i in range(n)]
    print(pascal)
    for i in range(n):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal

#n = int(input())
print(triangulo(5))