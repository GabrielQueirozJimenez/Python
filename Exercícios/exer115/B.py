def folder(name):
    try:
        a=open(name,'rt')#rt=ReadText
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def CreateFolder(name):
    try:
        a=open(name, 'wt+')#wt+ WriteText (+==if it's not exist, create one)
        a.close()
    except:
        print('ERROR')
    else:
        print(f'File {name} create with success')

def ReadFolder(name):
    from exer115.A import title
    try:
        a=open(name, 'rt')
    except:
        print('EOOR')
    else:
        title('CADASTROS')
        print('-'*30)
        for line in a:
            data=line.split(';')
            data[1]=data[1].replace('\n','')
            print(f'{data[0]:<30}{data[1]:>3} años')
    finally:
        a.close()

def cadastrar(arq, nome='Unknown', idade=0):
    try:
        a=open(arq,'at')#at, a==append t==text
    except:
        print('Error')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro com os dados')
        else:
            a.close()
