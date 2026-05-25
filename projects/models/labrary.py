class Biblioteca:
    bibliotecas = []
    
    def __init__(self, nome):
        self.nome = nome  # Consistência com o parâmetro
        self._ativo = False
        Biblioteca.bibliotecas.append(self)
    
    def __str__(self):
        return self.nome
    
    @classmethod
    def listar_bibliotecas(cls):
        for biblioteca in cls.bibliotecas:
            print(f"{biblioteca.nome} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada" 

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

# Agora funciona tanto pela instância quanto pela classe
biblioteca_cidade.listar_bibliotecas()  # ou Biblioteca.listar_bibliotecas()

print(biblioteca_cidade)
biblioteca_cidade.alterna_estado()
print(biblioteca_cidade.ativo)

print(biblioteca_shopping)
biblioteca_shopping.alterna_estado()
print(biblioteca_shopping.ativo)
