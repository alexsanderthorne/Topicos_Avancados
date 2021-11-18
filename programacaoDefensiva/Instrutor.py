from typing import List, Optional


class Instrutor:
    def __init__(self, nome: str, precos_cursos: Optional[List[float]] = None):
        self.nome = nome
        self.precos_cursos = precos_cursos or []

    def addPreco(self, novo_preco: float):
        self.precos_cursos.append(novo_preco)


joaquim = Instrutor("Tey", [111])

print(joaquim.precos_cursos)

print(id(joaquim.precos_cursos))
