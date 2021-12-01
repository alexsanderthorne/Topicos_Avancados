from typing import List, Optional
class Instrutor:
    def __init__(self, nome: str, precos_cursos: Optional[List[float]] = None):
        self.nome = nome
        self.precos_cursos = precos_cursos or []

    def addPreco(self, novo_preco: float):
        self.precos_cursos.append(novo_preco)

jhony = Instrutor('Well Jhony')
jhony.addPreco(3333.55)
jhony.addPreco(999)
print(jhony.precos_cursos)
print(id(jhony.precos_cursos))

caradeporco = Instrutor('Joe cara de porco')
caradeporco.addPreco(921)
caradeporco.addPreco(3666)
print(caradeporco.precos_cursos)

print(id(caradeporco.precos_cursos))


joaquim = Instrutor('Tey', [111])

print(joaquim.precos_cursos)
print(id(joaquim.precos_cursos))
