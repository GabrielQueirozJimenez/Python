#-------------------------------Exerc-16-----------------------------------------------------------
n = float(input('Dígite um número: '))
print(f'A parte inteira eh {n:.0f}')

#-------------------------------Exerc-17-----------------------------------------------------------

b = float(input('Qual o tamanho da base? '))
h = float(input('Qual a altura? '))
print(f'Se o triangulo tem a base {b}m e a altura {h}m, logo a hipotenusa vale {((b**2)+(h**2))**(1/2)}')

#-------------------------------Exerc-18-----------------------------------------------------------

from math import sin, cos, tan, radians
a = float(input('Valor do ângulo: '))
print(f"""Sin({sin(radians(a))})
Cos({cos(radians(a))})
Tan({tan(radians(a))})""")

#-------------------------------Exerc-19-----------------------------------------------------------

from random import choice
p = str(input('Qual o nome do primeiro aluno? '))
s = str(input('Qual o nome do segundo? '))
t = str(input('Terceiro: '))
q = str(input('Quarto: '))
e = [p,s,t,q]
print(f'O aluno/a sorteado foi {choice(e)}')

#-------------------------------Exerc-20-----------------------------------------------------------

from random import shuffle
p = str(input('Nome do primeiro aluno/a: '))
s = str(input('Segundo/a: '))
t = str(input('Terceiro/a: '))
q = str(input('Quarto/a: '))
e = [p,s,t,q]
shuffle(e)
print(f'A ordem da apresentação será\n{e}')

#-------------------------------Exerc-21-----------------------------------------------------------
#MP3
