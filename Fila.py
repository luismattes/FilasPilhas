class Fila:
    fila = []
    frente = 0
    atras = 0
    def enfileirar(self, valor):
        self.fila.insert(self.atras, valor)
        self.atras += 1
        if self.atras > 100:
            self.atras = 0

    def desenfileirar(self):
        self.fila.remove(self.fila[self.frente])
        self.frente += 1
        if self.frente > 100:
            self.frente = 0

    def verInicio(self):
        print('Nome:',self.fila[self.frente].getNome(self.fila[self.frente]))
        print('Telefone:',self.fila[self.frente].getTelefone(self.fila[self.frente]))

    def imprimirValores(self):
        for i in self.fila:
            print(i.getNome(i))
            print(i.getTelefone(i))