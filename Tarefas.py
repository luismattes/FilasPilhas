import Pilha
pilha = Pilha.Pilha
print('Precione a tecla 1 para inserir uma tarefa na pilha, precione a tecla 2 para obter a próxima tarefa da pilha'
      ' ou precione a tecla 3 para sair do sistema')
put = 0
while put != 3:
    put = int(input())
    if put == 1:
        pit = input('Descreva a tarefa a ser feita: ')
        pilha.empilhar(pilha,pit)
        print(pilha.verTopo(pilha),'adicionada a pilha de tarefas')
    if put == 2:
        if len(pilha.pilha) >= 1:
            print(pilha.verTopo(pilha), 'retirada da pilha de tarefas')
            pilha.desempilhar(pilha)
            print('Ainda restam estas tarefas na pilha')
            pilha.imprimirValores(pilha)
        else:
            print('Pilha vazia, adicione uma tarefa')