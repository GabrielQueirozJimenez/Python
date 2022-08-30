#-------------------------------Exerc-66-----------------------------------------------------------
s=c=0
while True:
   n = int(input('Digite um número: ''[999 = STOP]'))
   if n == 999:
       break
   s+=1
   c+=n
print(f'Você digitou {s} números e a soma de todos eh de {c}')

#-------------------------------Exerc-67-----------------------------------------------------------

while True:
   n = int(input('Tábuada de qual número? '))
   if n<0:
       break
   print('- - '*5)
   for c in range(1,11):
       print(f'{n} * {c} = ',n*c)
   print('- - '*5)
print('Fim')

#-------------------------------Exerc-68-----------------------------------------------------------

from random import randint
c=0
while True:
   r = str(input('Par ou Ímpar? ')).strip().title()
   n = int(input('Escolha um número '))
   m = randint(0,9)
   c+=1
   print('-='*20)
   print(f"""YOU                   MACHINE
{n}                     {m}""")
   if r in 'Par':
       if (n+m)%2==0:
           print(f'\033[1;32mGANHOU \033[1;34m{c}x\033[m')
           print('-='*20)
       else:
           print('\033[1;31mPERDEU\033[m')
           break
   elif r in 'Impar':
       if (n+m)%2!=0:
           print(f'\033[1;32mGANHOU \033[1;34m{c}x\033[m')
           print('-='*20)
       else:
           print('\033[1;31mPERDEU\033[m')
           break

#-------------------------------Exerc-69-----------------------------------------------------------

c=c2=c3=0
while True:
   age = int(input('How old are you? '))
   gender = str(input("What's your gender? [M/F]\n")).strip().upper()
   if age>=18:
       c+=1
   if gender in 'M':
       c2+=1
   if gender in 'F':
       if age<=20:
           c3+=1
   w=str(input('Would you like to continue? [Y/N]')).strip().upper()
   if w in 'N':
       break
print(f'We have {c} people higher than 18 years old\n{c2} Man\n{c3} Girls with less than 20 years')

#-------------------------------Exerc-70-----------------------------------------------------------

c=c2=c3=0
a=()   #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< NECESSARIO????
while True:
   nome=str(input('Nome do produto: ')).strip().title()
   custo=float(input(f'Custo do {nome}: £'))
   c+=custo
   if custo>=1000:
       c2+=1
   if c3>custo:
       a=nome
   c3=custo
   r=str(input('QUER CONTINUAR? [S/N]')).strip().lower()
   if r in 'n':
       break
print('-'*30)
print(f'Ao todo você gastou £{c}\nE temos {c2} produtos com valor maior que £1000\nE o produto mais barato eh {a}')

#-------------------------------Exerc-71-----------------------------------------------------------

saque=int(input('Quanto gostaria de sacar?\nR$'))               #ANALISAR...
t=saque
d=50
td=0
while True:
   if t>=d:
       t-=d
       td+=1
   else:
       if td>0:
           print(f'{td}x{d}')
       if d==50:
           d=20
       elif d==20:
           d=10
       elif d==10:
           d=1
       td=0
       if t==0:
           break