"""Objetivo: Sistema de progressão baseado em experiência, e 
jogador com múltiplos construtores 
□
□Criar construtores para inicializar jogadores 
adequadamente 
Implementar sistema de experiência (xp) e subir_nivel( ) 
□Gerenciamento de memória: destrutores para liberar 
recursos
"""


from colorama import Fore, Back, Style, init
init(autoreset=True)



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

        self.__qtd_pontos_lvl = 0

    #Destrutor
    def __dell__(self):
        return Fore.RED + f"Removendo os dados do jogador{self.__nome}"

    #Métodos Privados
    def __valida_experiencia(self):
        #usar um while pra rancar -100 de cada nivel
        #cada vez que ele puder rancar 100 de lvl, dou um append no vetor_pontos

        while(self.__nivel >= 100):
            self.__nivel -= 100
            self.__qtd_pontos_lvl += 1

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
    
    #Métodos públicos

    def recebe_dano(self, valor):
        if(self.__valida_dano(valor) == True):
            self.__hp = self.__hp - valor
            print(f"{self.__nome} recebeu um dano de:" + Fore.RED + f"{valor}")

    def recebe_cura(self, valor):
        if(self.__valida_cura(valor) == True):
            self.__hp = self.__hp + valor
            print(f"{self.__nome} recebeu uma cura de:" + Fore.GREEN + f"{valor}")

    def subir_nivel(self):
        
        #chama a função que valida xp
        self.__valida_experiencia()

        #se o jogador tiver pontos p/ gastar faz um mini menu p escolher com oq ele quer gastar esse ponto
        print("\n")
        if(self.__qtd_pontos_lvl > 0):

            #menu 
            while True:
                print(f"--------- {self.__nome} ---------")
                print("1 - Upar" + Fore.RED + " Combate")
                print("2 - Upar" + Fore.MAGENTA + " Magia")
                print("3 - Upar" + Fore.GREEN + " Alquimia")
                print("4 - Upar" + Fore.YELLOW + " Habilidades Gerais")
                try:
                    opcao = int(input("Digite uma opção: \n"))
                except ValueError:
                    print("Digite um valor inteiro!")
                
                if(opcao >= 1 and opcao <=4):
                    break
                else:
                    print("Digite uma opção válida!")
            match opcao:
                case 1: #Combate
                    self.__qtd_pontos_lvl -= 1
                    self.__lvl_combate +=1
                    print(f"{self.__nome} subiu de nível em" + Fore.RED + " Combate" + "!")

                case 2: #Magia
                    self.__qtd_pontos_lvl -= 1
                    self.__lvl_magia += 1
                    print(f"{self.__nome} subiu de nível em" + Fore.MAGENTA + " Magia" + "!")

                case 3: #Alquimia
                    self.__qtd_pontos_lvl -= 1
                    self.__lvl_alquimia += 1
                    print(f"{self.__nome} subiu de nível em" + Fore.GREEN + " Alquimia" + "!")

                case 4: #Habilidades Gerais
                    self.__qtd_pontos_lvl -= 1
                    self.__lvl_habilidade_geral += 1
                    print(f"{self.__nome} subiu de nível em" + Fore.YELLOW + " Habilidades Gerais" + "!")
        else:
            print(f"{self.__nome} não tem pontos para subir de nível!")


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

    #subindo de nível pelo sistema de xp
    jogador1.subir_nivel()
    jogador2.subir_nivel()
    jogador3.subir_nivel()

    #exibindo os personagens cm novos lvls
    print(jogador1)
    print(jogador2)
    print(jogador3)

    #Removendo 1 jogador
    del jogador1

    print("-" * 68)