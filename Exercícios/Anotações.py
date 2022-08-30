#print('Test',5)    # Diferentes tipos (str, int)
#print('Test'+5)    # Mesmo tipo (int + int)
####################################################################
#q = 'whatever'
#print('Q gots {}'.format(q))
####################################################################
#int=-1,2,-3,4...
#float=1.2,3.4...
#bool=True,False  #If has something write in there, it's True. if not, False.
#str='a','b','c','d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
####################################################################
#for m in range(0,3):
#    n=input('Write anything ')
#    print(n.isnumeric())
#    print(n.isalpha())
#    print(n.isdecimal())
####################################################################
#+ = adição
#- = subtração
#* = multiplicação
#/ = divisão
#** = exponenciação ---> 4**3 == pow(4,3)
#// = divisão inteira
#% = resto da divisão
#sum(range(0,5))
####################################################################
#print('Normal: {}!!!'.format('TEKISUTO'))
#print('Teste de caracteres: {:20}!!!'.format('TEKISUTO'))
#print('Teste de caracteres: {:>20}!!!'.format('TEKISUTO'))
#print('Teste de caracteres: {:^20}!!!'.format('TEKISUTO'))
#print('Teste de caracteres {:_^20}!!!'.format('TEKISUTO'))
#s=1/3
#print('Normal {}'.format(s))
#print(f'Teste das casas decimais flutuantes {s:.3f}')
####################################################################
#print('fdfds\nfsfefsf\ndsfsd',end=' ')
#print('AAAAaaaaahhhhhhh')
#-------------------------------Aula-08--MÓDULO---------------------------------------------------------
#library(Ctrl+Space) [random(randint,random, choice(works with list), shuffle(embaralha)),math]
#datetime import date [date.today().year]
#from operator import itemgetter       #Escolhe um referencial...
#-------------------------------Aula-09-----------------------------------------------------------
#frase = 'Teste paRA MaNipuLação de TeXtos'
#print(frase[0:6])
#print(frase[0:31:2])
#print(f'{frase[:9]} \n {frase[9:]} \n {frase[7::4]}')
#print(f'{len(frase)}') #Quantidade de caracteres
#print(f'{frase.count("a")}') #Conta quantas vezes aparece na frase (frase.count('a',5,9))
#print(f'{frase.find("nipul")}') # -1 se não for encontrada
#print(f'{"Teste" in frase}')
#print(f'{frase.replace("Teste para","Nekopara")}')
#print(f"{frase.upper()} // {frase.lower()} // {frase.capitalize()} // {frase.title()} // {frase.strip()} // {'-='.join(frase)}")
#s = frase.split()
#print(f'{s}\n{s[2]}')
#print(s[2][2:6])
    #.rstrip(strip na direita)//.lstrip(strip na esquerda)
    #Dica: frase=frase.replace()
#-----------------------------CONDIÇÕES-I--Aula-10-----------------------------------------------------------
#if:
#elif:
#else:
#s = input('Sim ou Não').strip().lower()[0]
#print('Teste' if s=='s' else 'Sem teste')
#c = int(input('number:' ))
#x = c+4 if s=='s' else c-4
#print(x)
#n=str(input('Anata no namae wa: '))
#if n in 'Edward Sebastian Whatever':
#    print('DOUDEMOII')
#elif n in 'Christa Alice Maria':
#    print('DouDemoIi')
#else:
#    print(f'{n:.^20}')
#-----------------------------CORES--Aula-11-----------------------------------------------------------
#\033[STYLE;TEXT;BACKGROUNDm
#STYLE: 0(normal), 1(BOLD), 4(UNDERLINE), 7(NEGATIVE)
#TEXT: 30(WHITE), 31(RED), 32(GREEN), 33(YELLOW), 34(BLUE), 35(PINK...), 36(CYAN), 37(SHADE)
#BACK: 40(WHITE), 41(RED), 42(GREEN), 43(YELLOW), 44(BLUE), 45(PINK...), 46(CYAN), 47(SHADE)
#-------------------------------Aula-12-----------------------------------------------------------
#Converter número para binário --> bin(n)
#Octal --> oct(n)
#Hexadecimal --> hex(n)
#-----------------------------REPETIÇÕES--Aula-11-----------------------------------------------------------
#for c in range(Start, End, Steps):
#s+=n
#while something != another:
#q=w=e=0
#while something not in another:
#while True:
#    break
#-----------------------------TUPLAS--Aula-16-----------------------------------------------------------
#n=('Dango','Blue','Ludwig','Blood','...')# ou n=0,1,2,3,...                                               IMUTAVÉL
#for c, v in enumerate(n):
#    print(f'Na posição {c+1}, ha encontrado {v}...')
#print(n[2])        #[-1] == Último elemento
#print(n[:2])
#for cont in range(0,len(n)):           #for teste in n:
#    print(n[cont], end=' ')                      #   print(teste)
#print('\n')
#for pos, cont in enumerate(n):          #for teste in n:
#    print(cont, pos)                    #   print(n[teste], teste)
#print(sorted(n))
#z=(1,2,3,4,5)
#x=(0,1,7,8)
#y = x+z                     #  x+z != z+x   #index(coisa,a partir da posição)==posição
#print(f'{y}\n{y.count(1)}\n{y.index(3)}\n{max(y)}\n{min(y)}')
#del(y)
#-----------------------------LISTAS--Aula-17-----------------------------------------------------------
#z=['Curry','Black','Khyan','Cell','...']                                                                   #MUTAVÉL
#z[2]='Banana'
#print(z)
#z.append('Teste')
#z.insert(2,'AAAAAA')
#del(z[0]) == z.pop(0) == z.remove('Curry')
#print(z)
#x=list(range(4,11))
#x.append(5)
#x.sort(reverse=True)
#print(x)
#y=x                                             #When y receive x, it makes a BOND (What means, what happen for one will happen for other)
#print(f'LISTA X: {x}\nLISTA Y: {y}')
#y[1]=321
#print(f"{x}\n{y}")
#x.remove(321)
#y=x[:]                                          #y receive a copy of x
#y[1]=321
#print(f'LISTA X: {x}\nLISTA Y: {y}')
#-----------------------------LISTAS-2-Aula-18-----------------------------------------------------------
#L1=[['Whatever',0],['DoNotCare',1],['ItsDoesntMatter',3]]
#L1.append(L2[:])   #Lista recebe outra lista >>>>> L1[[x1],[y2],[z3]]
#print(f'{L1[0][0]}\n{L1[2]}')
#L1.clear()
#-----------------------------DICIONÁRIOS--Aula-19-----------------------------------------------------------
#n={'identificador':'VALOR'}#        n=dict()            n={fsfd:fsdfs,dsdsa:ffdsf,...
#n['mais']='adicionado'#                                    }
#print(n['mais'])
#del n['mais']
#print(f'{n.values()}\n{n.keys()}\n{n.items()}')
#for k(key),v(value) in n.items():
#    print(f'O {k} eh {v}')
#lista=[]
#lista.append(n.copy())
#-----------------------------FUNÇÃO--Aula-20-----------------------------------------------------------
#def lin():
#    print('-'*30)#  Normalmente eh dado 2 espaçamentos
#lin()
#def texto(txt):
#    lin()
#    print(f'{txt:^30}')
#    lin()
#texto('TESTE')
#texto("teste")
#def ad(x,y):
#    z=x+y
#    print(z)
#ad(1,2)
#ad(x=3,y=6)
#ad(y=5,x=6)
#def cont(*num):# O * serve para desempacotar os parâmetros
#    print(num)# Comportamento iqual a tupla
#    for v in num:
#        print(f'{v} ',end='')
#    print()
#    lin()
#    print(len(num))
#    lin()
#cont(1,2,3,5,0)
#cont(3,6,9)
#cont(0)
#def dobra(list):
#    posição=0
#    while posição<len(list):
#        list[posição]*=2
#        posição+=1
#val=[3,6,9,5,2,1]
#dobra(val)
#print(val)
#-----------------------------FUNÇÃO-2-Aula-21-----------------------------------------------------------
#def lin():
#    '''
#    Show this command (-=) thirty times
#    :return: no return
#    '''
#    print('-='*30)
#help(print)# o print(print.__doc__)
#lin()
#help(print())# o print(print().__doc__)
#lin()
#help(lin)
#lin()
#def test(x=0,y=0,z=0):
#    """
#    Turn all param equal to 0 for do not have a ERROR
#    return give the result for a variaty
#    :param x: Test_X
#    :param y: Test_Y
#    :param z: Test_Z
#    :return: No return
#
#    Made by Me
#    """
#    return(x+y+z)
#print(f'Pode ser expresso assim também, {test(4,8)}')
#T1=test(3,6,9)
#T2=test(3,6)
#T3=test(3)
#print(f'Os resultados foram {T1},{T2} e {T3}')
#def TESTE():# ----> TESTAR: def global():
#    global a#,n1
    #a=3
    #n1=2
#    print(f'N1 vale {n1} e A vale {a}')
#a=2
#n1=3
#TESTE()
#print(f'N1 vale {n1} e A vale {a}')
#-----------------------------MÓDULOS_E_PACOTES--Aula-22------------------------------------------------------------
#-----------------------------TRATAMENTO_DE_ERRO--Aula-23-----------------------------------------------------------
#try:
#    Operation
#except:
#    What if, the operation fails
#else:
#    What if, the operation succeed
#finally:
#    What if, the operation fail and/or succeed
#Exception# means the error when that's even correct
#try:
#    a=int(input('A: '))
#    b=int(input('B: '))
#    print(a/b)
#except Exception as erro:
#    print(f'O erro encontrado foi... {erro.__class__}')
#except TypeError:
#except ValueError:
#except OSError:
#
#else:
#    print(f'A == {a} and B == {b}, so A/B == {a/b}')
#finally:
#    print('END\nThank You')
    # ERROR List:
        #ValueError             #Erro de valor
        #TypeError              #Erro de tipo
        #ZeroDivisionError      #You can't make a divison of any number by 0
        #KeyboardInterrupt      #Não informou dado
        #NameError              #
        #IndexError
        #KeyError
        #EOFError
