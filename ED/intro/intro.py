import random

class Pessoa:
     
     def __init__(self,n,i,a):
         self.nome = n
         self.idade = i
         self.altura = a
        
     def __str__(self):
         return self.nome+" , idade: "+str(self.idade)
         
     def aniversario(self):
         self.idade +=1
         
     def maior(self,outra):
         if self.altura > outra.altura:
            return True
         else:
            return False


class Aluno(Pessoa):

     def __init__(self,na,ia,aa,m):
         Pessoa.__init__(self,na,ia,aa)
         self.matricula = m
         self.nota = 0
   
     def __str__(self):
         return self.nome+", idade: "+str(self.idade)+" , nota: "+str(self.nota)
      
     def fazProva(self):
         self.nota = random.randint(0,10)

class Professor(Pessoa):
     
      def __init__(self,np,ip,ap,d):
         Pessoa.__init__(self,np,ip,ap)
         self.disciplina = d
 
      def __str__(self):
         return self.nome+", idade: "+str(self.idade)+", disciplina: "+self.disciplina
 
edu = Professor("Eduardo", 42, 1.7,"ED")
p = Pessoa("Pedro", 25, 1.8)
i = Pessoa("Isabela", 30, 1.6)
j = Aluno("Joao",31,1.89,123456789)
l = Aluno("Leandro",25,1.85,987654321)
l.fazProva()
j.fazProva()
print(l)
print(j)
print(edu)
print(i)
print(p)

