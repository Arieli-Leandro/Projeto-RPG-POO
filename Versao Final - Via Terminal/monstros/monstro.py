"""
Nesse arquivo tem o construtor do Monstro
Como o jogo é focado na criação de personagens o construtor do monstro tem o básico para
operar em segundo plano, então aqui temos poucas variáveis que vão ser interessantes para ser usadas
em conjunto com a classe de Interface ICombate, para operar no combate do jogador com o Monstro
"""

class Monstro:

    def __init__(self, nome, hp, xp_recompensa):
        self._nome = nome
        self._hp = hp
        self._xp_recompensa = xp_recompensa

    #Métodos getters
    def getNome(self):
        return self._nome

    def getHp(self):
        return self._hp

    def getXpRecompensa(self):
        return self._xp_recompensa

    #Métodos da classe
    def recebeDano(self, dano):
        self._hp = self._hp - dano

        if self._hp < 0:
            self._hp = 0

        return

    def estaMorto(self):
        return self._hp <= 0