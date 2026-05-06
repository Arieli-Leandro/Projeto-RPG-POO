"""Classe: Jogador/Player/Character 
Atributos: nome, nível, HP, HP máximo 
Métodos: exibirStatus(), estaVivo(), receberDano(), curar() 
Linguagens: Python e C++
"""

class Jogador:
    def __init__(self, nome, nivel, hp):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.hp_maximo = 300

    def exibirStatus(self):
        return f'| {self.nome} | {self.nivel} | {self.hp} |'

    def estaVivo(self):
        if self.hp > 0:
            return f'{self.nome} ainda está vivo!'

    def receberDano(self):
        if self.hp > 0:
            self.hp-= 10
            return f'{self.nome} recebeu 10 de dano!'
        else:
            return f'{self.nome} está morto!'

    def curar(self):
        if self.hp < self.hp_maximo:
            self.hp+= 20
        return f'{self.nome} bebeu uma poção de cura +20Hp!'
    

if __name__ == "__main__":

    player1 = Jogador("Yennefer", 50, 200)
    player2 = Jogador("Geralt de Rivia", 35, 350)

    print(player1.receberDano())
    print(player2.curar())

    print(player1.exibirStatus())
    print(player2.exibirStatus())
    print(player1.estaVivo())