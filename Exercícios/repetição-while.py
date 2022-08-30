#-------------------------------Exerc-57-----------------------------------------------------------
s = str(input('Qual o seu sexo?: ')).strip()[0]
while s not in 'FfMm':
   s = str(input('Sexo INVÁLIDO, tente novamente [F/M]\n')).strip().upper()[0]
print('Fim')

#-------------------------------Exerc-58/28--------------------------------------------------------

from random import randint
w = 0
c = randint(0,10)
q = int(input('A maquina pensou em um número entre 0 e 10, qual número você acha que ela pensou?\n'))
if q != c:
   print('Errou, continue tentando...')
while c != q:
   c = randint(0,10)
   q = int(input('Número: '))
   w+=1
   if c != q:
       print(f'Errou, {c}')
print(f'PARABÉNS, você levou {w} tentativas')

#-------------------------------Exerc-59-----------------------------------------------------------

a = 9
n1 = float(input('Digite um valor: '))
n2 = float(input('Mais um valor: '))
a = 9
while a != 0:
   a = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novo Valor
[0] SAIR\n'''))
   print('-='*20)
   if a == 1:
       print(n1+n2)
   elif a == 2:
       print(n1*n2)
   elif a == 3:
       print(n1 if n1>n2 else n2)
   elif a == 4:
       n1 = float(input('Novo valor: '))
       n2 = float(input('Novo valor²: '))
print('The End')

#-------------------------------Exerc-60-----------------------------------------------------------

n = int(input('Número que você deseja saber o fatorial: '))
c = n
f=1
while c>0:
   print(f'{c} ',end = '')
   print('x ' if c>1 else f'= {f}', end='')
   f*=c
   c-=1

#-------------------------------Exerc-61/51-----------------------------------------------------------

p = int(input('Qual o primeiro termo? '))
s = int(input('De quanto será o salto? '))
c = 0
while c<10:
   print(p, end=' ')
   p+=s
   c+=1
print('Fin')

#-------------------------------Exerc-62/61-----------------------------------------------------------

p = int(input('Qual o primeiro termo? '))
s = int(input('De quanto será o salto? '))
c = 0
ç = False
while c<10:
   print(p, end=' ')
   p+=s
   c+=1
while ç == False:
   a = int(input('\nQuer ver mais quantos termos? '))
   for ab in range(0,a):
       print(p,end=' ')
       p+=s
   if a == 0:
       ç=True
print('Fin')

#-------------------------------Exerc-63-----------------------------------------------------------

p1=0
p2=1
c=3
termo = int(input('Quantos termos gostaria de ver da sequencia de Fibonacci?\n'))
print(f'{p1} {p2}', end=' ')
while c<=termo:
   p3=p1+p2
   print(p3, end=' ')
   p1=p2
   p2=p3
   c+=1
print('\nEND')

#-------------------------------Exerc-64-----------------------------------------------------------

n=m=c=0
n = int(input('Número '))
while n != 999:
   m+=n
   c+=1
   n = int(input('Número '))
print(f'Ao todo você digitou {c} números e, a soma de todos eles, foi de {m}')

#-------------------------------Exerc-65-----------------------------------------------------------

c=m=p=g=0
r='S'
while r == 'S':
   w = int(input('Número: '))
   m+=w
   if c==0:
       p = w
       g = w
   elif p<w:
       p=w
   elif g>w:
       g=w
   c+=1
   r = str(input('Quer continuar? ')).strip().upper()[0]
print(f'Média = {m/c}\n O maior eh {p}\n O menor eh {g}')
