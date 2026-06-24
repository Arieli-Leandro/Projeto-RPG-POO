from abc import ABC, abstractmethod

"""
Interface responsável por definir o comportamento de combate.

Toda classe que implementar ICombate deve obrigatoriamente
fornecer uma implementação para o método atacar(monstro),
que representa uma ação ofensiva contra um inimigo.
"""

class ICombate(ABC):

    @abstractmethod
    def atacar(self, monstro):
        pass


"""
Interface responsável por definir o comportamento de cura.

Toda classe que implementar ICuravel deve obrigatoriamente
fornecer uma implementação para o método curar(),
responsável por recuperar pontos de vida do personagem.
"""
class ICuravel(ABC):

    @abstractmethod
    def curar(self):
        pass