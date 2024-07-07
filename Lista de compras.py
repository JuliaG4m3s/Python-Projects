soun=None
lista=[]
def adicion():
    arr1=input('O que deseja adicionar na sua lista?')
    lista.append(arr1)
    print('Adicionou',*lista,'a sua lista')
def remov():
    remover=int(input('Que elemento deseja remover?(número)'))
    lista.remove(lista[remover])
def index():
    elec=int(input('Que elemento deseja procurar?'))
    lista.index(elec)
def sub():
    subs=input('Que elemento deseja substituir?')
    ind=int(input('Número do elemento que deseja substituir(começa em 0)'))
    lista[ind]=subs
def simounao():
    global soun
    while soun!='n':
        soun=input('Deseja continuar? (s/n)')
        if soun=='s':
            arr1=input('O que deseja fazer a sua lista?')
arr1=input('O que deseja adicionar na sua lista?')
lista.append(arr1)
soun=input('Deseja continuar? (y/n)')
if soun=='n':
    print('Programa encerrado')
while soun=='y':
    arr2=input('O que deseja fazer na sua lista?(A-Adicionar um elemento, R-remover um elemento, I-procurar, S-Substituir)')
    match arr2:
        case 'a':
            adicion()
            simounao()
        case 'r':
            remov()
            simounao()
            print('Removeu',*lista,'a sua lista')
        case 'i':
            index()
            simounao()
        case 's':
            sub()
            simounao()
        case _:
             print('Opção inválida')