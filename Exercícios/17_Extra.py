#-------------------------------Exerc-86-----------------------------------------------------------
#l=[[0,0,0],[0,0,0],[0,0,0]]
#for c in range (0,3):
#    for v in range(0,3):
#        l[c][v]=int(input(f'Valor para a posição [{c+1},{v+1}]'))
#for c in l:
#    for v in c:
#        print(f'[{v:^5}]',end=' ')
#    print()
#-------------------------------Exerc-87/86-----------------------------------------------------------
#l=[[0,0,0],[0,0,0],[0,0,0]]
#par=col=tin=0
#for c in range(0,3):
#    for v in range(0,3):
#        l[c][v]=int(input(f'Número para ocupar a posição [{c+1},{v+1}]: '))
#for c in range(0,3):
#    for v in range(0,3):
#        print(f'[{l[c][v]:^5}] ',end='')
#        if l[c][v]%2==0:
#            par+=l[c][v]
#    col+=l[c][2]
#    if tin<l[1][c]:
#        tin=l[1][c]
#    print()
############################################
#for c in l:
#    for v in c:
#        if v in c[2]:
#            col+=v
#        if c[1]:
#            if tin<v:
#                tin=v
############################################
#print(f'A) {par}\nB) {col}\nC) {tin}')
