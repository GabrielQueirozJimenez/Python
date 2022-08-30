#-------------------------------Exerc-22-----------------------------------------------------------
name = str(input("What's your name? ")).strip()
nombre = name.split()
print(f'{name.upper()}\n{name.lower()}\n{len("".join(nombre))}\n{len(nombre[0])}')
##3° -> len(name)-name.count(' ')//4° -> name.find(' ')

#-------------------------------Exerc-23-----------------------------------------------------------

n = int(input('Choose a number among 0 to 9999: '))
print(f'Unidade = {n//1%10}\nDezena = {n//10%10}\nCentena = {n//100%10}\n Milhar = {n//1000%10}')

#-------------------------------Exerc-24-----------------------------------------------------------

c = str(input('Digit the name of any city: ')).upper().strip()
x = c.split()
print(f"The city's name start with Santo: {'SANTO' in x[0]}")
print(c[:5]=='SANTO')

#-------------------------------Exerc-25-----------------------------------------------------------

c = str(input('What is your name? ')).strip().lower()
print(f'Does have "Silva" in your name: {"silva" in c}')

#-------------------------------Exerc-26-----------------------------------------------------------

p = str(input('Write a phrase: ')).lower().strip()
print(f"""How many times the letter 'a' appear in your phrase: {p.count('a')}
it's the position: {p.find('a')+1}
The last 'a' in your name appear in the {p.rfind('a')+1}° position""")

#-------------------------------Exerc-27-----------------------------------------------------------

name = str(input("What's your name? ")).strip()
nombre = name.split()
print(f'Your first name is "{nombre[0]}" and your last name is "{nombre[-1]}"')
