#-------------------------------Exerc-96-----------------------------------------------------------
def area(b,h):
   print(f'A área do terreno, eh de {b*h}m²')
b=float(input('Qual o valor da largura? '))
h=float(input('Qual o valor do comprimento? '))
area(b,h)

#-------------------------------Exerc-97-----------------------------------------------------------

def write(txt):
   print('~'*(len(txt)+4))
   print(f'  {txt}')
   print('~'*(len(txt)+4))
a=str(input('Digite algo: '))
write(a)

#-------------------------------Exerc-98-----------------------------------------------------------

def lin():
   print('-'*25)
def contador():
   for c in range(1,11):
       print(c,end=' ')# end=' ', ##flush=True
   print()
   lin()
   for c in range(10,-1,-2):
       print(c,end=' ')
   print()
   lin()
   i=int(input('Start: '))
   f=int(input('Final: '))
   s=int(input('Jump: '))
   if i>f and s>0:
       s=-s
   elif i>f and s==0:
       s=-1
   elif i<f and s<0:
       s*=-1
   elif i<f and s==0:
       s=1
   for c in range(i,f,s):
       print(c,end=' ')
contador()

#-------------------------------Exerc-99-----------------------------------------------------------

def maior(*val):
   a=t=0
   print('Os números digitados foram, ',end='')
   for c in val:
       print(c,end=' ')
       if t==0:
           a=c
       elif c>a:
               a=c
       t+=1
   print(f', e o maior valor foi {a}')
   print('-='*25)
maior(9,5,3,6,2,0,8)
maior(0,1,2,3)
maior(5)
maior()

#-------------------------------Exerc-100-----------------------------------------------------------

from random import randint
l=[]
def sorteia(l):
   for c in range(0,5):
       l.append(randint(0,10))
   print(f'Os números sorteados foram...',end=' ')
   print(l)
def somaPar(m):
   a=0
   for c in m:
       if c%2==0:
           a+=c
   print(a)
sorteia(l)
somaPar(l)

#-----------------------------Aula-21--Exerc-101-----------------------------------------------------------

def vote(year):
   from datetime import date
   if (date.today().year-year)<=17:
       return f'Você tem {date.today().year-year} anos. AINDA NÃO PODE VOTAR'
   elif (date.today().year-year)<=65:
       return f'Você tem {date.today().year-year} anos. SEU VOTO É OBRIGATÓRIO'
   else:
       return f'Você tem {date.today().year-year} anos. VOCÊ TEM A OPÇÃO DE VOTAR'
a=int(input('Em que ano você nasceu? '))
print(vote(a))

#-------------------------------Exerc-102-----------------------------------------------------------

def factory(num,show=False):
   """
   This function has the purpose to calculate the factorial of a number
   :param num: Here, you put the number
   :param show: That's a optional function to show the process (nothing and False, won't show anything but True)
   :return: The factorial of the number
   """
   v=1
   for c in range(num,0,-1):
       if show:
           print(c, end='')
           if c>1:
               print(' * ',end='')
           else:
               print('= ',end='')
       v*=c
   return v
print(factory(5,True))
print('END')

#-------------------------------Exerc-103-----------------------------------------------------------

def ficha(nome='<Unkown>',score=0):           #Sei lá, mais ou menos
   print(f'{nome} has made {score}')
#ficha(input('Name '),(input('Score ')))
name=str(input('Name: ')).strip().title()
score=bool(input('Score: '))                 #Testar caso seja escrito um valor (3,três,...)
if bool(name)==False:
   name='<Unkown>'
if score==False:
   score=0
ficha(name,score)

#-------------------------------Exerc-104-----------------------------------------------------------

def leiaint(num):
   while True:
       n=str(input(f'\033[m{num}'))
       if n.isnumeric():
           break
       else:
           print('\033[1;31mERROR, this is not a int number, try again ')
   return n
n=leiaint('Digite un numero: ')
print(f'\033[mHa digitado el numero {n}')

#-------------------------------Exerc-105-----------------------------------------------------------

def notas(*notes,sit=False):
   '''
   Sei lá
   :param notes: All the grades
   :param sit: (Optional)
   :return: Some situations
   '''
   d={}
   d['Total']=len(notes)
   d['Higher']=max(notes)
   d['lower']=min(notes)
   d['"Media"']=sum(notes)/len(notes)
   if sit:
       if d['"Media"']>=7:
           d['Situation']='Good'
       elif d['"Media"']>=5:
           d['Situation']='Regular'
       else:
           d['Situation']='Bad'
#    return d
   l=[]
   n=0
   r=''
   for c in notes:
       l.append(c)
       n+=c
   if sit==True:
       if n/len(l)<=5:
           r='Ruim'
       elif n/len(l)<=8:
           r='Boa'
       else:
           r='Excelente'
   return print(f'We got {len(l)+1}\nHighest note was {max(l)}, lowest {min(l)}\n'
         f'The "media" {n/len(l):.2f} {r}')
resp=notas(6,7,8,5.5,3,10,sit=True)
print(resp)

#-------------------------------Exerc-106-----------------------------------------------------------

def ayuda():
   while True:
       n=input('\033[1;35mQuieres ayuda con cual comando?: \033[m')
       if n == 'Fim' or n == 'fim':
           break
       print(f'\033[7m{n.__doc__}\033[m')
#        print(f'\033[7m{help(n)}\033[m')
ayuda()
