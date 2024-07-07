a=0
e=0
cores=['azul', 'amarelo', 'verde', 'vermelho', 'preto', 'branco']
while e==0:
    v=input('Deseja eliminar algum elemento da lista?(y/n): ')
    if v=='y' or v=='Y':
        print(cores)
        i=int(input('Qual posição deseja eliminar? '))
        cores.remove[i]
        print(cores)
    elif v=='n' or v=='N':
        print('Lista: ',cores)
        e=e+1
    else:
        print('opção inválida')
        e=e+1
while a==0:
    c=input('Deseja adicionar algum elemento da lista?(y/n): ')
    if c=='y' or c=='Y':
        n1=input('Introduza o elemento que deseja adicionar: ')
        cores.append[n1]
        print(cores)
    elif c=='n' or c=='N':
        print('Lista: ',cores)
        a=a+1
    else:
        print('Opção inválida')
        a=a+1