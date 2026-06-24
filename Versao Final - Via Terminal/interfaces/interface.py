from abc import ABC, abstractmethod

class ICombate(ABC):

    @abstractmethod
    def atacar(self, monstro):
        pass

class ICuravel(ABC):

    @abstractmethod
    def curar(self):
        pass