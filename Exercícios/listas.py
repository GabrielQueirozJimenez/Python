#-------------------------------Exerc-78-----------------------------------------------------------
l=[]
for c in range(0,5):
   l.append(int(input(f'{c+1}° valor: ')))
print(f'{l}\nO maior valor foi {max(l)} na posição', end=' ')
for i,c in enumerate(l):
   if c==max(l):
       print(f'{i+1},',end=' ')
print(f'\nO menor, {min(l)} na posição {l.index(min(l))+1}',end=' ')
for i,c in enumerate(l):
   if c==min(l):
       print(f'{i+1}, ',end=' ')

#-------------------------------Exerc-79-----------------------------------------------------------

l=[]
while True:
   for c in range(0,3):
       n = int(input('Digite um número: '))
       if n not in l:
           l.append(n)
       elif n in l:
           print('Esse número, já existe na Lista')
   a = str(input('Would you like to proceed? ')).strip().lower()[0]
   if a in 'Nn':
       break
print(sorted(l))

#-------------------------------Exerc-80-----------------------------------------------------------

l=[]
for c in range (0,5):
   n = int(input(f'{c+1} número: '))
   if c==0 or n>l[-1]:
       l.append(n)
   else:
       pos=0
       while pos < len(l):
           if n<=l[pos]:
               l.insert(pos,n)
               break
           pos+=1
print(l)

#-------------------------------Exerc-81-----------------------------------------------------------

l=[]
while True:
   for c in range(0,3):
       l.append(int(input('Digite um valor:\n')))
   ans = str(input('Mais números? ')).strip().upper()[0]
   if ans =='N':
       break
l.sort(reverse=True)
print(f"""A) {len(l)}
B) {l}
C) O número 5, está na posição...{l.index(5) if 5 in l else 'Esse valor não existe'}""")

#-------------------------------Exerc-82-----------------------------------------------------------

l=[]
while True:
   l.append(int(input('Digite um valor: ')))
   a=str(input('Quer continuar? ')).strip().lower()
   if a in 'Nn':
       break
p=l[:]
i=l[:]
for c in p:
   if c%2!=0:
       p.remove(c)
for c in i:
   if c%2==0:
       i.remove(c)
print(f'Lista complet: {l}\nLista Ímpar: {i}\nLista Par: {p}')

#-------------------------------Exerc-83-----------------------------------------------------------

l=[]
test=str(input('\033[1;35mDIGITE A EQUAÇÃO\n\033[36m'))
for c in test:
   if c == '(':
       l.append(c)
   elif c==')':
       if len(l)>0:
           l.pop()
       else:
           l.append(')')
           break
print('CORRETA') if len(l)==0 else print('ERRADA')

#-----------------------------Aula-18--Exerc-84-----------------------------------------------------------

l1=[]
l2=[]                                          #Considerou os maiores e menores digitados... (não 100 ou 70...)
l3=[]
l4=[]
while True:
   l1.append(str(input('Nome: ')).strip().title())
   l1.append(float(input(f'Peso de {l1[0]}: ')))
   l2.append(l1[:])
   l1.clear()
   r = str(input('Quer continuar? [Y/N] '))
   if r in 'Nn':
       break
print(f"1) {len(l2)} pessoas cadastradas...")
for c in l2:
   if c[:][1] <= 70:
       l3.append(c[0])
   elif c[:][1]>=100:
       l4.append(c[0])
   elif 70 < c[:][1] < 100:
       l1.append(c[0])
print(f'2) As pessoas mais pesadas são {l4}\nAs mais leves... {l3}\n3) E as com pesos ideais...{l1}')

#-------------------------------Exerc-85-----------------------------------------------------------

l=[[],[]]                              #l=[]
for o in range(0,7):
   n=int(input(f'Digite o {o+1}° valor: '))
   if n%2==0:
       l[0].append(n)
   else:
       l[1].append(n)
l[0],l[1].sort()
print(f'Lista Par ==> {l[0]}\nLista Ímpar ==> {l[1]}\nLista Completa... {l}')

#-------------------------------Exerc-86-----------------------------------------------------------

l=[[0,0,0],[0,0,0],[0,0,0]]
for c in range (0,3):
   for v in range(0,3):
       l[c][v]=int(input(f'Valor para a posição [{c+1},{v+1}]'))
for c in l:
   for v in c:
       print(f'[{v:^5}]',end=' ')
   print()

#-------------------------------Exerc-87/86-----------------------------------------------------------

l=[[0,0,0],[0,0,0],[0,0,0]]
par=col=tin=0
for c in range(0,3):
   for v in range(0,3):
       l[c][v]=int(input(f'Número para ocupar a posição [{c+1},{v+1}]: '))
for c in range(0,3):
   for v in range(0,3):
       print(f'[{l[c][v]:^5}] ',end='')
       if l[c][v]%2==0:
           par+=l[c][v]
   col+=l[c][2]
   if tin<l[1][c]:
       tin=l[1][c]
   print()
###########################################
for c in l:
   for v in c:
       if v in c[2]:
           col+=v
       if c[1]:
           if tin<v:
               tin=v
###########################################
print(f'A) {par}\nB) {col}\nC) {tin}')

#-------------------------------Exerc-88-----------------------------------------------------------

from random import randint
l=[]
a=int(input('Quantos jogos, você gostaria de sortear? '))
for c in range(0,a):
   while len(l)<6:
       m = randint(0,60)
       if m not in l:
           l.append(m)
   print(f'{c+1}° jogo: {l}')
   l.clear()

#-------------------------------Exerc-89-----------------------------------------------------------

l=[]
f=[]
while True:
   l.append(str(input('Nome: ')).strip().title())
   l.append(float(input(f'1° Nota de {l[0]}: ')))
   l.append(float(input(f'2° Nota de {l[0]}: ')))
   f.append(l[:])
   l.clear()
   a = str(input('Quer continuar? '))
   if a in 'Nn':
       break
print(f'{"-="*25}\nINFO.    ID.    MÉDIA\n{"_"*25}')
for c in range(0,len(f)):
   print(f'{c}      {f[c][0]}    {((f[c][1])+(f[c][2]))/2:.2f}', end="\n")
print('_'*25)
while True:
   a = int(input('Gostaria de ver as informações de quem? [999 to stop] '))
   if a == 999:
       break
   print(f'{f[a][0]} gets the grades {f[a][1]} and {f[a][2]}\n{"_"*40}')
print('PROGRAMA FECHADO')
