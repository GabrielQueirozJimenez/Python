#-------------------------------Exerc-113-----------------------------------------------------------
def leiaInt(num):
   while True:
       try:
           n=int(input(f'\033[m{num}\033[m'))
       except (ValueError, TypeError):
           print('\033[1;31mERROR, this is not a int number, try again ')
           continue
       except (KeyboardInterrupt):      #<----  DOES NOT WORK
           print('Programa interrompido')
           return 0
       else:
           return n

def leiaFloat(num):
   while True:
       try:
           n=float(input(f'\033[m{num}\033[m'))
       except ValueError:
           print('\033[1;31mERROR, this is not a float number, try again ')
       else:
           return n

int=leiaInt('Int: ')
float=leiaFloat('Float: ')
print(f'Você digitou {int} como inteiro e {float} como real')

#-------------------------------Exerc-114-----------------------------------------------------------

from urllib.request import urlopen
try:
   site=urlopen('https://www.virustotal.com/')
except:
   print('Site out of service (Try your internet connection)')
else:
   print('URL opened with success')
finally:
   print(site.read())

#-------------------------------Exerc-115-----------------------------------------------------------

from exer115.A import *
from exer115.B import *

arc='CADASTRO.txt'
if not folder(arc):
   CreateFolder(arc)

title("MAIN MENU")
while True:
   try:
       q=body()
   except (ValueError, TypeError):
       print('\033[31mPlease, insert a valid option\033[m')
   else:
       if q == 1:
           op_1(arc)
       elif q == 2:
           op_2()
       elif q == 3:
           break
       else:
           print('Error, please inform a valid value')
           print('-'*30)
