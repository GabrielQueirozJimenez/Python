from time import sleep
name=input("What's your name?\n")
age=input('How old are you?\n')
weight=input("How much do you weigh?\nKg: ")
print("Let's see...")
sleep(1)
print(f'So, Your name is {name}, you are {age} years old and your weigh is {weight}kg...')
sleep(2)
print('Right?')

print('-='*20)

n=int(input('Elige un número: '))
m=int(input('Ahora otro '))
b=n+m
print(f'La soma de {n} y {m} es {b}')

print('-+'*20)

n=input('Escriba algo: ')
print('Analisando...')
sleep(1)
print(f'{n}, Es un número?')
sleep(0.8)
print(n.isnumeric())
print('-+'*10)
sleep(0.8)
print(f'{n}, Es una Stream?')
sleep(0.8)
print(n.isalpha())
print('-+'*10)
sleep(0.8)
print(f'{n}, Es un alphanumerico?')
sleep(0.8)
print(n.isalnum())