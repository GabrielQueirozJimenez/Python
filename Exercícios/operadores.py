#-------------------------------Exerc-5------------------------------------------------------------
n = int(input('Choose a number: '))
print(f'O antecessor de {n} eh {n-1} e o sucessor eh {n+1}')

#-------------------------------Exerc-6------------------------------------------------------------

n = float(input('Choose another number:' ))
print(f'This number 2 times is {n*2}, 3 times... {n*3}, and its square root is {n**(1/2)}')

#-------------------------------Exerc-7------------------------------------------------------------

f=float(input("What's the first grade? "))
s=float(input("The second one? "))
print(f'This student got {(f+s)/2}')

#-------------------------------Exerc-8------------------------------------------------------------

m=float(input("What's the distance in meters? "))
print(f'So the distance can be shown as {m*100}cm and/or {m*1000}mm, right?')

#-------------------------------Exerc-9------------------------------------------------------------

n=int(input('Escolha um número para ver sua tabuada: '))
for m in range (1,11):
   print(f'{n} * {m} = {n*m}')

#-------------------------------Exerc-10-----------------------------------------------------------

d=float(input('Quanto de dinheiro você tem?\nR$ '))
print(f'Convertendo para dolar, você possui USD${d/3.27:.2f}')

#-------------------------------Exerc-11-----------------------------------------------------------

b=float(input("What's the leght in meters? "))
h=float(input("What's the height in meters? "))
print(f'Your area is {b*h} meters, and you will need {(b*h)/2} l de tinta')

#-------------------------------Exerc-12-----------------------------------------------------------

b = float(input('??Cual es lo preço original? '))
print(f'Lo nuevo preço con 5% de desconto es {b*0.95:.2f}')

#-------------------------------Exerc-13-----------------------------------------------------------

s= float(input("What's your salary?\n£ "))
print(f'Your new salary is £{s*1.15:.2f}')

#-------------------------------Exerc-14-----------------------------------------------------------

c = float(input('Qual a temperatura atual? '))
print(f'A temperatura de {c}°, equivale a {((9*c)/5)+32}° fahrenheit...')

#-------------------------------Exerc-15-----------------------------------------------------------

k = float(input('Qual a distância percorrida? Km '))
d = int(input('Quantos dias? '))
print(f'Sua taxa final a pagar eh de R${(60*d)+(k*0.15):.2f}')
