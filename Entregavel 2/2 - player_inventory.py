"""Descrição: refatore a classe Jogador com todos os atributos 
privados e validados 
Implemente propriedades para hp (não pode exceder 
hp máximo) 
□Criar método receber_dano( ) com validação 
□Criar método curar( ) com validação 
□Garantir que nível nunca seja negativo
"""

class Jogador:
    def __init__(self, nome, nivel, hp, lvl_combate, lvl_magia, lvl_alquimia, lvl_habilidade_geral):
        self.__nome = nome

        if(self.__valida_atributo_construtor(nivel) == True):
            self.__nivel = nivel
        else:
            self.__nivel = 0

        if(self.__valida_atributo_construtor(hp) == True):
            self.__hp = hp
        else:
            self.__hp = 10

        if(self.__valida_atributo_construtor(lvl_combate) == True):
            self.__lvl_combate = lvl_combate
        else:
            self.__lvl_combate = 0

        if(self.__valida_atributo_construtor(lvl_magia) == True):
            self.__lvl_magia = lvl_magia
        else:
            self.__lvl_magia = 0

        if(self.__valida_atributo_construtor(lvl_alquimia) == True):
            self.__lvl_alquimia = lvl_alquimia
        else:
            self.__lvl_alquimia = 0

        if(self.__valida_atributo_construtor(lvl_habilidade_geral) == True):
            self.__lvl_habilidade_geral = lvl_habilidade_geral
        else:
            self.__lvl_habilidade_geral = 0

        self.__hp_maximo = 999

    def __valida_atributo_construtor(self, valor):
        retorno = False

        if(valor > 0):
            retorno = True

        return retorno

    def __valida_dano(self, valor_dano):
        retorno = False

        vida_total = self.__hp - valor_dano

        if(vida_total >= 0):
            retorno = True

        return retorno

    def __valida_cura(self, valor_cura):
        retorno = False

        vida_total = self.__hp + valor_cura

        if(vida_total <= self.__hp_maximo):
            retorno = True

        return retorno

    def recebe_dano(self, valor):
        if(self.__valida_dano(valor) == True):
            self.__hp = self.__hp - valor

    def recebe_cura(self, valor):
        if(self.__valida_cura(valor) == True):
            self.__hp = self.__hp + valor


    def __str__(self):
        return f"|{self.__nome}|HP:{self.__hp}|LVL:{self.__nivel}|Alquimia:{self.__lvl_alquimia}|Combate:{self.__lvl_combate}|Geral:{self.__lvl_habilidade_geral}|Magia:{self.__lvl_magia}|"
    

if __name__ == "__main__":

    jogador1 = Jogador("Geralt", 100, 500, 80, 60, 40, 70)

    print(jogador1)
    jogador1.recebe_dano(100)
    print(jogador1)
    jogador1.recebe_cura(50)

    print("-" * 68)

    jogador2 = Jogador("Yennefer", 90, 400, 30, 95, 50, 60)
    print(jogador2)
    jogador2.recebe_dano(450)  
    print(jogador2)

    print("-" * 68)

    jogador3 = Jogador("Ciri", 120, 450, 90, 40, 30, 80)
    print(jogador3)
    jogador3.recebe_cura(1000) 
    print(jogador3)

    print("-" * 68)