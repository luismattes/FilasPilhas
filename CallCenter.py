import Fila
import Contato

fila = Fila.Fila
contato = Contato.Contato
mensage = 'Para adicionar um contato digite 1 para consultar um contato digite 2 e para sair do sistema digte 3'
put = 0
print(mensage)
while put != 3:
    put = int(input())
    if put == 1:
        pit = input('Digite o nome do contato: ')
        pat = input('Digite o telefone do contato: ')
        contato.__init__(contato, pit, pat)
        fila.enfileirar(fila, contato)
        print('Contato adicionado')
        print(mensage)
    if put == 2 and len(fila.fila) >= 1:
        fila.verInicio(fila)
        fila.desenfileirar(fila)
    else:
        print('Fila vazia')