#-------------------------------Exerc-46-----------------------------------------------------------
from time import sleep
for c in range(10,0,-1):
   print(c)
   sleep(0.5)
print('\033[1;34mBOM','\033[1;31mBOOM','\033[1;33mBUM')

#-------------------------------Exerc-47-----------------------------------------------------------

for c in range(0,51):       #Quanto mais processo, mais exige do processador (dica: range(2,51,2))
   if c%2==0:
       print(c, end=' ')

#-------------------------------Exerc-48-----------------------------------------------------------

s = 0
for c in range(1,501,2):
   if c % 3 == 0:
       s+=c
print(s)

#-------------------------------Exerc-49-----------------------------------------------------------

n = int(input('Qual número?\n'))
for c in range(1,11):
   print(f'{n}x{c}={n*c}')

#-------------------------------Exerc-50-----------------------------------------------------------

z = 0
for c in range(0,6):
   x = float(input(f'{c+1}° número:'))
   if x%2==0:
       z+=x
print(z)

#-------------------------------Exerc-51-----------------------------------------------------------

t = int(input('Ao o 1° Termo?'))        #ERROR
r = int(input('Qual a razão?'))    # m = t+(10-1)*r
for c in range(t,t+10):            #for c in range(t,m+r,r)
   t+=r
   print(t,end=' ')

#-------------------------------Exerc-52-----------------------------------------------------------

n = int(input('Qual número, você acha que é primo? '))
for c in range(1,n+1):
   if n%c==0:
       print(c)

#-------------------------------Exerc-53-----------------------------------------------------------

f = str(input('Frase palindromo: ')).strip().lower()
f2 = f.split()
f3 = ''.join(f2)
f4 = ''                            #|f4 = f3[::-1]// Não precisa do 'for'
for letra in range(len(f3)-1,-1,-1):
   f4 += f3[letra]
print(f3,'//',f4)
if f3 == f4:
   print('É um palindromo')
else:
   print('Não palindromo')

#-------------------------------Exerc-54-----------------------------------------------------------

from datetime import date
s=d=0
for c in range(0,8):
   a = int(input(f'Em que ano a {c}° pessoa nasceu? '))
   if (date.today().year - a) >= 21:
       s+=1
   elif (date.today().year - a) < 21:
       d+=1
print(f'Ao todo temos {s} pessoas maiores de idade e {d} menores')

#-------------------------------Exerc-55-----------------------------------------------------------

s=S=0
for c in range(0,5):
   p = float(input(f'Peso da {c+1}° pessoa: '))
   if c==1:
       s = p
       S = p
   else:
       if s < p:
           s=p
       if S > p:
           S=p
print(f'O maior peso eh de {s} e o menor, de {S}')

#-------------------------------Exerc-56-----------------------------------------------------------

q=w=f=0
o = 'aaaaaa'
for c in range(0,4):
   name = str(input('Su nombre:\n')).strip()
   edad = int(input(f'Qual es su edad {name}?\n'))
   sexo = str(input('Qual es su sexo, Man o Woman?\n')).strip().lower()[0]
   print('-='*20)
   q+=edad
   if sexo == 'm' or 'h':                  #sexo = 'Mm'
       if w<edad:
           w=edad
           o=name
   if sexo =='w' or 'f':
       if edad<20:
           f+=1
print('''Ao todo temos uma média de idade de {:.0f} anos.
O homem mais velho se chama {} e ele tem {} anos.
E temos {} mulheres com menos de 20 anos'''.format(q/4,o,w,f))
