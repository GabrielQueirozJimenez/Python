#-------------------------------Exerc-90-----------------------------------------------------------
d={}
d['nome']=str(input('Nome: ')).strip().title()
d['média']=float(input(f'Qual a média de {d["nome"]}? '))
if d['média']>=7:
   d['situação']='Boa'
else:
   d['situação']='Ruim'
print(f"Nome == {d['nome']}\nMédia == {d['média']}\nSituação == {d['situação']}")

#-------------------------------Exerc-91-----------------------------------------------------------

from random import randint
from operator import itemgetter
d={}
f={}
l=[]
for c in range(0,4):
   for v in range(0,2):
       l.append(randint(1,6))
       d[f'Jogador{c+1}']=l[:]
   l.clear()
for c in d.values():
   C=0
   for v in c:
       C+=v
       for c in range(3,9,3):
           d[c]=C
   print(c,C)
print(f)
########################################################
game={'Player_1':randint(1,6),
     'Player_2':randint(1,6),
     'Player_3':randint(1,6),
     'Player_4':randint(1,6)}
rank={}
for k,v in game.items():
   print(f'{k} tirou {v}')
rank=sorted(game.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(rank):                                ###TRATAMENTO DE LISTA
   print(f'{i+1}° Lugar {v[0]}: {v[1]}')

#-------------------------------Exerc-92-----------------------------------------------------------

from datetime import date
d={}
d['name']=str(input('Name: '))
d['age']=int(input('Year you have born: '))
d['age']=date.today().year-d['age']#datetime.now().year
d['work']=int(input('carteira de trabalho: [número, 0 caso não haja] '))
if d['work']!=0:
   d['hired']=int(input('When did you are hire?'))
   d['salary']=float(input('How much is your salary? '))
   m=(-date.today().year)+d['hired']+35+d['age']
   print(f'anata no namae wa {d["name"]} desu. soshite\nTienes {d["age"]} años y\n'
         f'Sua carteira de trabalho possui os seguintes números de série... {d["work"]} e\n'
         f'You were hired in {d["hired"]}, what means you will retire with {m} years\n'
         f'Your salary is {d["salary"]}')
else:
   print(f'name = {d["name"]}\nage = {d["age"]}\n You do not work yet...')

#-------------------------------Exerc-93-----------------------------------------------------------

d={}
l=[]
m=0
d['nombre']=str(input('Cual es el nombre: '))
d['partidas']= int(input(f'Cuantas partidas {d["nombre"]} he jugado? '))
for c in range(0,d['partidas']):
   l.append(int(input(f'Quantos puntos {d["nombre"]}, ha hecho en la {c+1}° partida? ')))
for v in l:
   m+=v
d['puntos']=l      #d['puntos'] = sum(l)
print('-='*25)
print(f'Nombre del competidor: {d["nombre"]}\n'
     f'{d["nombre"]} ha participado de {d["partidas"]} partidas\n'
     f'Y ha conseguido {m} puntos')
print('=-'*25)
for k in range(0,len(d['puntos'])):
   print(f"En la {k+1}° --- {d['puntos'][k]}")
print(f'Total de {m} puntos')

#-------------------------------Exerc-94-----------------------------------------------------------

d={}
l=[]
f=[]
i=[]
c=0
while True:
   d['nome']=str(input('Nome: ')).strip().title()
   d['gender']=str(input("What's your gender? "))
   d['age']= int(input('How old are you? '))
   c+=d['age']
   l.append(d.copy())
   if d['gender'] in 'Ff':
       f.append(d.copy())
   a=str(input('Would you like to proceed? [Y/N] ')).strip().lower()[0]
   print('-'*20)
   if a in 'n':
       break
for k in l:
   if k['age']>(c/(len(l))):
       i.append(k.copy())
print(f'A) {len(l)}\nB) {c/len(l)}\nC) {f}\nD) {i}')

#-------------------------------Exerc-95/93-----------------------------------------------------------

d={}                   ###REFAZER
l=[]
d2=[]
m=0
while True:
   d['namae']=str(input('Namae wa: ')).strip().title()
   d['assault'] = int(input('How many assaults: '))
   for c in range(0,d['assault']):
       l.append(int(input(f'How much score at the {c+1}° assault? ')))
   for c in l:
       m+=c
   m=m/len(l)
   d['final']=m
   a=str(input('Would you like to add more one? '))
   d['score']=l[:]
   l.clear()
   d2.append(d.copy())
   if a in 'Nn':
       break
print(f"N°      Name        Score              Final")
for c in range(0,len(d2)):
   print(f"{c}     {d2[c]['namae']}        {d2[c]['score']}        {d2[c]['final']}")
while True:
   q=int(input('Who would you like to see the information about? '))
   if q == 999:
       break
   print(f"name = {d2[q]['namae']}\nAssault = {d2[q]['assault']}\n")
   for c in range(0,len(d2[q]['score'])):
       print(f"On the {c+1}° it gots {d2[c]['score']}")
