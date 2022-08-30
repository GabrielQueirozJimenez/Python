#-------------------------------Exerc-72-----------------------------------------------------------
numero=('Maru', 'Hitotsu', 'Futatsu', 'Mitsu', 'Yotsu', 'Itsutsu', 'Mutsu', 'Nanatsu', 'Yatsu', 'Kokonotsu', 'Tomu',
'Jyuuichi', 'jyuuni', 'jyuusan', 'jyuuji', 'jyuugo', 'jyuuroku', 'jyuunana', 'jyuuhan', 'jyuukyuu', 'nijyuu')
u = int(input('Choose a number:  '))        #While True:
while 0>u or u>20:                          #   u=int(input('Choose a number))
   u = int(input('Try again:  '))          #   if 0<=u<=20:
print(numero[u])                            #        break

#-------------------------------Exerc-73-----------------------------------------------------------

p=('Ludwig','Sora','Logarius','Spider','Snake','Cockroach','Mox','Fox','Kenji','Yamada','Yamakawa','Kawada','Daisuki',
'Daikirai','Kute','Futon','Cobalt','Sapphire','Gaimond','Shiro')
print(f'1) {p[:5]}\n2) {p[-4:]}\n3) {sorted(p)}\n4) {p.index("Sapphire")+1}')

#-------------------------------Exerc-74-----------------------------------------------------------

from random import randint
n1=randint(0,9)
n2=randint(0,9)
n3=randint(0,9)
n4=randint(0,9)
n5=randint(0,9)
a=(n1,n2,n3,n4,n5)
print(f'{a}\nO Maior eh {max(a)} e o menor {min(a)}')

#-------------------------------Exerc-75-----------------------------------------------------------

c=0
b=False
tupla = ((int(input('1° Número '))),int(input('2° Número ')),int(input('3° Número ')),int(input('4° Número ')))
for a in tupla:                                               #print(f'O 9 apareceu {tupla.count(9)}x'}
   if a == 9:                                                #if 3 in tupla:
       c+=1                                                  #     print(f'O 3, apareceu na posição {tupla.index(3)}'
   if a == 3:                                                #else:
       b=True                                                #     print('Não há 3')
print(f'\nAo todo apareceram {c}x o número 9', end='\n')      #print(f'Os números pares são:',end=' ')
if b==True:                                                   #for a in tupla:
   print(f'O 3 está na posição {tupla.index(3)+1}')          #     if a%2==0:
else:                                                         #         print(a)
   print('Não há o número 3')
print(f'Os números pares são:',end=' ')
for a in tupla:
   if a%2==0:
       print(a,end=' ')

#-------------------------------Exerc-76-----------------------------------------------------------

s=('Maça',0.50,'Pão',2.00,'Laranja',1.50,'Banana',1.00,'Sorvete',2.50,'Leek',0.90,'Berinjela',3.00,'ETC',5.00)
print('-'*35)
for c in range(0,len(s)):
   if c%2==0:
       print(f'{s[c]:.<25}$',end='')
   else:
       print(f'{s[c]:>5.2f}')
print('-'*35)

#-------------------------------Exerc-77-----------------------------------------------------------

teste=('Deep','Sea','Hibikase','fukurou','Alphabet','XZY','Ventisilva')
for c in teste:
   print(f'\nA palavra {c}, possui as vogais: ', end='')
   for n in c:
       if n in 'AaIiUuEeOo':
           print(n, end=' ')
