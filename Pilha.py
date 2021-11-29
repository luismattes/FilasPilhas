class Pilha:
    pilha = []
    def empilhar(self, valor):
        self.pilha.insert(0, valor)

    def desempilhar(self):
        self.pilha.remove(self.pilha[0])

    def verTopo(self):
        return(self.pilha[0])

    def imprimirValores(self):
        for i in self.pilha:
            print(i)