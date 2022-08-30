#-------------------------------Exerc-36-----------------------------------------------------------
c = float(input('Quanto custa o imovel?\n'))
s = float(input('Quanto é o seu salário?\n'))
e = int(input('Pretende parcelar em meses [0], ou em anos [1]?\n'))
if e == 0:
   t = int(input('Em quantos meses pretende pagar:'))
   e = c/t
   print(f"A compra foi aprovada, e terá que pagar uma prestação de R${e:.2f}/mês" if e<=(s*0.3) else f"""A compra foi rejeitada.
Tenha um bom dia!!!""")
elif e == 1:
   t = int(input('Em quantos anos pretende parcelar?\n'))
   e = c/(t*12)
   print(f'A compra foi aprovada, e terá que pagar uma prestação de R${e:.2f}/ano' if e<=(s*0.3) else f'''A compra foi negada.''')

#-------------------------------Exerc-37-----------------------------------------------------------

n = int(input('Digie qualquer número: '))
c = int(input(f'Gostar de converter {n} para qual base?\n Binária[0], Octal [1] ou Hexadecimal [2]\nOpção: '))
if c == 0:
   print(f'O número {n} em Binário eh {bin(n)[2:]}')
elif c == 1:
   print(f'O número {n} em Octal eh igual a {oct(n)[2:]}')
elif c == 2:
   print(f'O número {n} na base hex, eh iqual a {hex(n)[2:]}')

#-------------------------------Exerc-38-----------------------------------------------------------

f = int(input('First number: '))
s = int(input('Second number: '))
if f == s:
   print('\033[1;31mThey are the same\033[m')
elif f>s:
   print(f'\033[7m{f} is bigger than {s}\033[m')
elif s>f:
   print(f'\033[1;35;47m{f} is smaller than {s}\033[m')

#-------------------------------Exerc-39-----------------------------------------------------------

from datetime import date
genre = str(input('Você é Homem ou Mulher???\n')).strip().lower()[0]
if genre == 'h':
   a = int(input("Em que ano você nasceu? "))
   t = date.today().year
   if t-a < 18:
       c = (a+18)-t
       print(f'Você terá que se alistar em {c} anos')
   elif t-a == 18:
       print('Você precisa se alista agora')
   else:
       c = (t-18)-a
       print(f'Você se alistou/ ou deveria ter se alistado há {c} anos')
elif genre == 'm':
   print('Você não precisa se alistar')

#-------------------------------Exerc-40-----------------------------------------------------------

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1+n2)/2
if m < 5:
   print(f'{m}\n\033[1;31mREPROVADO\n:(\033[m')
elif 5<m<=6.9:
   print(f'{m}\n\033[1;33mRECUPERAÇÃO\n:/\033[m')
elif m >=7:
   print(f'{m}\n\033[1;36mAPROVADO\n:)\033[m')

#-------------------------------Exerc-41-----------------------------------------------------------

from datetime import date
b = int(input('When did you born? '))
a = date.today().year
print('Sua caegoria é...')
if (a-b)<=9:
   print('MIRIM')
elif (a-b)<=14:
   print('INFANTIL')
elif (a-b)<=19:
   print('JUNIOR')
elif (a-b)<=20:
   print('SÊNIOR')
elif (a-b)>20:
   print('MASTER')

#-------------------------------Exerc-42/35-----------------------------------------------------------

f = float(input('1° reta: '))
s = float(input('2° reta: '))
t = float(input('3° reta: '))
if (f+s)>t and (t+f)>s and (s+t)>f:
   if f==s!=t or t==f!=s or s==t!=f:
       print('Triângulo Isósceles')
   elif f==s==t:
       print('Triângulo Equilátero')
   elif f!=s!=t!=f:
       print('Triângulo Escaleno')
else:
   print(f'As retas {f}, {s} e {t}, não formam um triângulo')
print('FIM!!!')

#-------------------------------Exerc-43-----------------------------------------------------------

w = float(input("What's your weight?\n"))
h = float(input("How much tall are you?\n"))
imc = w/(h**2)
if imc < 18.5:
   print('Você está abaixo do peso...')
elif 18.5<=imc<25:
   print('Você está com o peso ideal')
elif 25<=imc<30:
   print('Acima do peso')
elif 30<=imc<40:
   print('OBESIDADE')
elif 40<=imc:
   print('OBESIDADE MÓRBIDA')

#-------------------------------Exerc-44-----------------------------------------------------------

p = float(input('Qual o preço original do produto?\n$'))
e = int(input('Como pretende fazer o pagamento?\nDinheiro/Cheque [1]\nCartão [2]'))
if e == 2:
   e = int(input('2x no Cartão [1]\n3x ou mais no Cartão [2]\nÀ vista no Cartão [3]'))
   if e == 1:
       print(f'O valor eh ${p}, e irá ser pago por 2 parcelas de {p*0.5}')
   elif e == 2:
       e = int(input('Quantas vezes? '))
       print(f'Você irá pagar {e} parcelas de ${p/e*1.2}\nTOTAL:{p*1.2}')
   elif e == 3:
       print(f'O valor do produto eh de ${p*0.95}')
elif e == 1:
   print(f'O novo valor eh de ${p*0.9}')

#-------------------------------Exerc-45-----------------------------------------------------------

from random import choice
jokenpô = choice(['Pedra', 'Tesoura', 'Papel'])
challenger = str(input('Qual você escolhe?\nPedra, Tesoura, Papel\n')).strip().title()
print(f'''You               Machine
{challenger}                {jokenpô}''')
if jokenpô == 'Pedra':
   if challenger == 'Pedra':
       print('EMPATE')
   elif challenger=='Papel':
       print('CHALLENGER WIN')
   elif challenger=='Tesoura':
       print('MACHINE WIN')
elif jokenpô == 'Papel':
   if challenger == 'Pedra':
       print('MACHINE WIN')
   elif challenger == 'Papel':
       print('EMPATE')
   elif challenger == 'Tesoura':
       print('CHALLENGER WIN')
elif jokenpô == 'Tesoura':
   if challenger == 'Pedra':
       print('CHALLENGER WIN')
   elif challenger == 'Papel':
       print('MACHINE WIN')
   elif challenger == 'Tesoura':
       print('         EMPATE')
