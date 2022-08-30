def leiaInt(num):
    while True:
        try:
            n=int(input(f'\033[m{num}\033[m'))
        except (ValueError, TypeError):
            print('\033[1;31mERROR, this is not a int number, try again ')
            continue
        except (KeyboardInterrupt):
            print('Programa interrompido')
            return 0
        else:
            return n

def title(txt):
    print(f'{txt:^30}')
    print('-'*30)

def body():
    print('-'*30)
    l=['Ver cadastro', 'Fazer novo cadastro', 'Sair do Sistema']
    for c,v in enumerate(l):
        print(f'{c+1} - {v}')
    print('-'*30)
    a=leiaInt('Option: ')
    return a

def op_1(thing):
    from exer115.B import ReadFolder
    print('-'*30)
    print(f'OPTION 1'.center(30))
    ReadFolder(thing)

def op_2():
    arc = 'CADASTRO.txt'
    from exer115.B import cadastrar
    print('-'*30)
    print(f'OPTION 2'.center(30))
    print('-'*30)
    name=str(input('Nombre: ')).strip().title()
    age=leiaInt('Edad: ')
    cadastrar(arc, name, age)
