#-------------------------------Exerc-28-----------------------------------------------------------
from random import randint
n = randint(0,5)
a = int(input('Qual número a máquina pensou (0-5)? '))
print(f"Acertou, {n}" if a==n else f'Errou, {n}')

#-------------------------------Exerc-29-----------------------------------------------------------

d = float(input('Qual a distância percorrida pelo veiculo?\n'))
t = float(input('Quanto tempo ele levou para percorrer essa distância?\n'))
v = d/t
if v > 80:
   print(f'Você foi multado e terá que pagar uma multa de R${(v-80)*7:.2f}')
print('Dirija com cuidado')

#-------------------------------Exerc-30-----------------------------------------------------------

n = int(input('Choose a number: '))
print(f'{n} é Par' if (n%2) == 0 else f'{n} é Ímpar')

#-------------------------------Exerc-31-----------------------------------------------------------

d=float(input('Qual a distância da viagem?\nKm:'))
print(f'A viagem irá custar ${d*0.5:.2f}' if d<=200 else f'A viagem irá custar ${d*0.45:.2f}')

#-------------------------------Exerc-32-----------------------------------------------------------

from datetime import date
a = int(input('Qual ano gostaria de saber se é bissexto? [0] caso queira saber sobre o ano atual: '))
if a == 0:
   a = date.today().year
print(f'O ano {a} é bissexto' if (a%4==0) and ((a%100!=0) or (a%400==0)) else f'O ano {a} não é bissexto')

#-------------------------------Exerc-33-----------------------------------------------------------

p=float(input('Choose a number: '))
s=float(input('Another one: '))
t=float(input('The last one: '))
m=p
M=p
if s<p and s<t:
   m=s
if t<s and t<p:
   m=t
if s>p and s>t:
   M=s
if t>s and t>p:
   M=t
print(f'O maior número digitado foi {M}, e o menor foi {m}')

#-------------------------------Exerc-34-----------------------------------------------------------

s=float(input("What's your salary? "))
print(f"You got a extra of 10% {s*1.1:.2f}" if s>1250 else f"You got a extra of 15% {s*1.15:.2f}")

#-------------------------------Exerc-35-----------------------------------------------------------

r1 = float(input('What is the length of the first straight?\n'))
r2 = float(input('What is the length of the second one?\n'))
r3 = float(input('The third?\n'))
if (r1+r2)>r3 and (r1+r3)>r2 and (r2+r3)>r1:
   print(f' The straight {r1},{r2} and {r3} can be a triangle')
else:
   print(f'The straight {r1},{r2} and {r3} cannot be triangle')
