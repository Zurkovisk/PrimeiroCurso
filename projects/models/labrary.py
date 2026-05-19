class Biblioteca:
    bibliotecas = []
    
    def __init__(self, nome):
        self.name = nome
        self._ativo = False
        Biblioteca.bibliotecas.append(self)
    
    def __str__(self):
        return self.name
    
    def listar_bibliotecas(self):
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.name} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada" 

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

# Call the method on an instance, not the class
biblioteca_cidade.listar_bibliotecas()

print(biblioteca_cidade)
biblioteca_cidade.alterna_estado()
print(biblioteca_cidade.ativo)
print(biblioteca_shopping)
biblioteca_shopping.alterna_estado()
print(biblioteca_shopping.ativo)