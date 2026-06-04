#O método Fabric vai permitir q a gnt tenha um menu de criação de jogador e profissão
# Não esquecer dps de fazer um gerenciador com interface pra fazer as tasks e tbm vai precisar de um Singleton :/ (-A)

from abc import ABC, abstractmethod
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

class ExcessaoNivelGeralInvalido(Exception):

    def __str__(self):
        return f"Valor de nível geral inválido!"

class Profissao(ABC):

    def __init__(self, nivel_geral_profissao=0):
        self._qtd_pontos_profissao = 0 

        if self._valida_atributo_construtor(nivel_geral_profissao) == True:
            self._nivel_geral_profissao = nivel_geral_profissao
        else:
            self._nivel_geral_profissao = 0

    #método setter
    def setNivelGeral(self, valor):
        if(valor < 0):
            raise ExcessaoNivelGeralInvalido()
        
    #método getter
    def getNivelGeral(self):
        return self._nivel_geral_profissao

    #método privado
    def __valida_atributo_construtor(self, valor):
        retorno = False

        if valor > 0:
            retorno = True

        return retorno

    def transforma_pontos_experiencia(self):
        while self._nivel_geral_profissao >= 10:
            self._nivel_geral_profissao = self._nivel_geral_profissao - 10
            self._qtd_pontos_profissao = self._qtd_pontos_profissao + 1

        return

    #método privado tbbm
    def __verifica_aumenta_lvl_habilidade(self, valor):
        retorno = True

        valor = valor + 1
        if valor > 13:
            retorno = False

        return retorno

    @abstractmethod
    def inicializa_profissao(self):
        pass

    def __del__(self):
        print("Profissao deletada")

#fazer os getters e setters daqui tbbm
class Mago(Profissao):

    def __init__(self, lvl_criar_ritual=0, lvl_lancar_feitico=0, lvl_educacao=0, lvl_resistir_magia=0, nivel_geral=0):
        super().__init__(nivel_geral)

        if self.__valida_atributo_construtor(lvl_criar_ritual) == True:
            self.__lvl_criar_ritual = lvl_criar_ritual
        else:
            self.__lvl_criar_ritual = 0

        if self.__valida_atributo_construtor(lvl_lancar_feitico) == True:
            self.__lvl_lancar_feitico = lvl_lancar_feitico
        else:
            self.__lvl_lancar_feitico = 0

        if self.__valida_atributo_construtor(lvl_educacao) == True:
            self.__lvl_educacao = lvl_educacao
        else:
            self.__lvl_educacao = 0

        if self.__valida_atributo_construtor(lvl_resistir_magia) == True:
            self.__lvl_resistir_magia = lvl_resistir_magia
        else:
            self.__lvl_resistir_magia = 0

    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):
        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("1 - Upar Habilidade de: Criar Ritual")
                print("2 - Upar Habilidade de: Educacao")
                print("3 - Upar Habilidade de: Lancar Feitico")
                print("4 - Upar Habilidade de: Resistir Magia")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 1:  # Criar Ritual
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_criar_ritual) == True:
                    self.__lvl_criar_ritual = self.__lvl_criar_ritual + 1
                    print("subiu de nivel em Criar Ritual!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 2:  # Educacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_educacao) == True:
                    self.__lvl_educacao = self.__lvl_educacao + 1
                    print("subiu de nivel em Educacao!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 3:  # Lancar Feitico
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_lancar_feitico) == True:
                    self.__lvl_lancar_feitico = self.__lvl_lancar_feitico + 1
                    print("subiu de nivel em Lancar Feitico!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 4:  # Resistir Magia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_resistir_magia) == True:
                    self.__lvl_resistir_magia = self.__lvl_resistir_magia + 1
                    print("subiu de nivel em Resistir a Magia!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print("Voce nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm

class Bardo(Profissao):

    def __init__(self, lvl_etiqueta_social=0, lvl_ludibriar=0, lvl_sabedoria_das_ruas=0, nivel_geral=0):
        super().__init__(nivel_geral)

        # private
        if self.__valida_atributo_construtor(lvl_etiqueta_social) == True:
            self.__lvl_etiqueta_social = lvl_etiqueta_social
        else:
            self.__lvl_etiqueta_social = 0

        if self.__valida_atributo_construtor(lvl_ludibriar) == True:
            self.__lvl_ludibriar = lvl_ludibriar
        else:
            self.__lvl_ludibriar = 0

        if self.__valida_atributo_construtor(lvl_sabedoria_das_ruas) == True:
            self.__lvl_sabedoria_das_ruas = lvl_sabedoria_das_ruas
        else:
            self.__lvl_sabedoria_das_ruas = 0

    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):
        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("1 - Upar Habilidade de: Etiqueta Social")
                print("2 - Upar Habilidade de: Ludibriar")
                print("3 - Upar Habilidade de: Sabedoria das Ruas")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 1 and opcao <= 3:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 1:  # Etiqueta Social
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_etiqueta_social) == True:
                    self.__lvl_etiqueta_social = self.__lvl_etiqueta_social + 1
                    print("subiu de nivel em Etiqueta Social!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 2:  # Ludibriar
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_ludibriar) == True:
                    self.__lvl_ludibriar = self.__lvl_ludibriar + 1
                    print("subiu de nivel em Ludibriar!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 3:  # Sabedoria das Ruas
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_sabedoria_das_ruas) == True:
                    self.__lvl_sabedoria_das_ruas = self.__lvl_sabedoria_das_ruas + 1
                    print("subiu de nivel em Sabedoria das Ruas!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print("Voce nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm
class Artesao(Profissao):

    def __init__(self, lvl_educacao=0, lvl_criacao=0, lvl_negociacao=0, lvl_fisico=0, nivel_geral=0):
        super().__init__(nivel_geral)

        # private
        if self.__valida_atributo_construtor(lvl_educacao) == True:
            self.__lvl_educacao = lvl_educacao
        else:
            self.__lvl_educacao = 0

        if self.__valida_atributo_construtor(lvl_criacao) == True:
            self.__lvl_criacao = lvl_criacao
        else:
            self.__lvl_criacao = 0

        if self.__valida_atributo_construtor(lvl_negociacao) == True:
            self.__lvl_negociacao = lvl_negociacao
        else:
            self.__lvl_negociacao = 0

        if self.__valida_atributo_construtor(lvl_fisico) == True:
            self.__lvl_fisico = lvl_fisico
        else:
            self.__lvl_fisico = 0

    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):
        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("1 - Upar Habilidade de: Educacao")
                print("2 - Upar Habilidade de: Criacao")
                print("3 - Upar Habilidade de: Negociacao")
                print("4 - Upar Habilidade de: Fisico")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 1:  # Educacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_educacao) == True:
                    self.__lvl_educacao = self.__lvl_educacao + 1
                    print("subiu de nivel em Educacao!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 2:  # Criacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_criacao) == True:
                    self.__lvl_criacao = self.__lvl_criacao + 1
                    print("subiu de nivel em Criacao!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 3:  # Negociacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_negociacao) == True:
                    self.__lvl_negociacao = self.__lvl_negociacao + 1
                    print("subiu de nivel em Negociacao!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 4:  # Fisico
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_fisico) == True:
                    self.__lvl_fisico = self.__lvl_fisico + 1
                    print("subiu de nivel em Fisico!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print("Voce nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm
class Criminoso(Profissao):

    def __init__(self, lvl_arrombar_fechaduras=0, lvl_falsificacao=0, lvl_atletismo=0, lvl_sabedoria_das_ruas=0, nivel_geral=0):
        super().__init__(nivel_geral)

        if self.__valida_atributo_construtor(lvl_arrombar_fechaduras) == True:
            self.__lvl_arrombar_fechaduras = lvl_arrombar_fechaduras
        else:
            self.__lvl_arrombar_fechaduras = 0

        if self.__valida_atributo_construtor(lvl_falsificacao) == True:
            self.__lvl_falsificacao = lvl_falsificacao
        else:
            self.__lvl_falsificacao = 0

        if self.__valida_atributo_construtor(lvl_atletismo) == True:
            self.__lvl_atletismo = lvl_atletismo
        else:
            self.__lvl_atletismo = 0

        if self.__valida_atributo_construtor(lvl_sabedoria_das_ruas) == True:
            self.__lvl_sabedoria_das_ruas = lvl_sabedoria_das_ruas
        else:
            self.__lvl_sabedoria_das_ruas = 0

    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):
        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("1 - Upar Habilidade de: Arrombar Fechadura")
                print("2 - Upar Habilidade de: Falsificacao")
                print("3 - Upar Habilidade de: Atletismo")
                print("4 - Upar Habilidade de: Sabedoria das Ruas")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 1:  # Arrombar Fechadura
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_arrombar_fechaduras) == True:
                    self.__lvl_arrombar_fechaduras = self.__lvl_arrombar_fechaduras + 1
                    print("subiu de nivel em Arrombar Fechaduras!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 2:  # Falsificacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_falsificacao) == True:
                    self.__lvl_falsificacao = self.__lvl_falsificacao + 1
                    print("subiu de nivel em Falsificacao!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 3:  # Atletismo
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_atletismo) == True:
                    self.__lvl_atletismo = self.__lvl_atletismo + 1
                    print("subiu de nivel em Atletismo!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 4:  # Sabedoria das Ruas
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_sabedoria_das_ruas) == True:
                    self.__lvl_sabedoria_das_ruas = self.__lvl_sabedoria_das_ruas + 1
                    print("subiu de nivel em Sabedoria das Ruas!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print("Voce nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm
class Doutor(Profissao):

    def __init__(self, lvl_carisma=0, lvl_educacao=0, lvl_coragem=0, lvl_alquimia=0, nivel_geral=0):
        super().__init__(nivel_geral)

        if self.__valida_atributo_construtor(lvl_carisma) == True:
            self.__lvl_carisma = lvl_carisma
        else:
            self.__lvl_carisma = 0

        if self.__valida_atributo_construtor(lvl_educacao) == True:
            self.__lvl_educacao = lvl_educacao
        else:
            self.__lvl_educacao = 0

        if self.__valida_atributo_construtor(lvl_coragem) == True:
            self.__lvl_coragem = lvl_coragem
        else:
            self.__lvl_coragem = 0

        if self.__valida_atributo_construtor(lvl_alquimia) == True:
            self.__lvl_alquimia = lvl_alquimia
        else:
            self.__lvl_alquimia = 0

    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):
        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True: 
                #Colocar o treco do console aqui tbm
                print("1 - Upar Habilidade de: Educacao")
                print("2 - Upar Habilidade de: Coragem")
                print("3 - Upar Habilidade de: Alquimia")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 1 and opcao <= 3:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 1:  # Educacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_educacao) == True:
                    self.__lvl_educacao = self.__lvl_educacao + 1
                    print("subiu de nivel em Educacao!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 2:  # Coragem
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_coragem) == True:
                    self.__lvl_coragem = self.__lvl_coragem + 1
                    print("subiu de nivel em Coragem!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 3:  # Alquimia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_alquimia) == True:
                    self.__lvl_alquimia = self.__lvl_alquimia + 1
                    print("subiu de nivel em Alquimia!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print("Voce nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm
class Cavaleiro(Profissao):

    def __init__(self, lvl_coragem=0, lvl_intimidacao=0, lvl_sobrevivencia=0, lvl_esquivar=0, nivel_geral=0):
        super().__init__(nivel_geral)

        # private
        if self.__valida_atributo_construtor(lvl_coragem) == True:
            self.__lvl_coragem = lvl_coragem
        else:
            self.__lvl_coragem = 0

        if self.__valida_atributo_construtor(lvl_intimidacao) == True:
            self.__lvl_intimidacao = lvl_intimidacao
        else:
            self.__lvl_intimidacao = 0

        if self.__valida_atributo_construtor(lvl_sobrevivencia) == True:
            self.__lvl_sobrevivencia = lvl_sobrevivencia
        else:
            self.__lvl_sobrevivencia = 0

        if self.__valida_atributo_construtor(lvl_esquivar) == True:
            self.__lvl_esquivar = lvl_esquivar
        else:
            self.__lvl_esquivar = 0

    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):
        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("1 - Upar Habilidade de: Coragem")
                print("2 - Upar Habilidade de: Intimidacao")
                print("3 - Upar Habilidade de: Sobrevivencia")
                print("4 - Upar Habilidade de: Esquivar")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 1:  # Coragem
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_coragem) == True:
                    self.__lvl_coragem = self.__lvl_coragem + 1
                    print("subiu de nivel em Coragem!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 2:  # Intimidacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_intimidacao) == True:
                    self.__lvl_intimidacao = self.__lvl_intimidacao + 1
                    print("subiu de nivel em Intimidacao!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 3:  # Sobrevivencia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_sobrevivencia) == True:
                    self.__lvl_sobrevivencia = self.__lvl_sobrevivencia + 1
                    print("subiu de nivel em Sobrevivencia!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 4:  # Esquivar
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_esquivar) == True:
                    self.__lvl_esquivar = self.__lvl_esquivar + 1
                    print("subiu de nivel em Esquivar!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print("Voce nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm
class Comerciante(Profissao):

    def __init__(self, lvl_carisma=0, lvl_educacao=0, lvl_negocios=0, lvl_persuasao=0, nivel_geral=0):
        super().__init__(nivel_geral)

        # private
        if self.__valida_atributo_construtor(lvl_carisma) == True:
            self.__lvl_carisma = lvl_carisma
        else:
            self.__lvl_carisma = 0

        if self.__valida_atributo_construtor(lvl_educacao) == True:
            self.__lvl_educacao = lvl_educacao
        else:
            self.__lvl_educacao = 0

        if self.__valida_atributo_construtor(lvl_negocios) == True:
            self.__lvl_negocios = lvl_negocios
        else:
            self.__lvl_negocios = 0

        if self.__valida_atributo_construtor(lvl_persuasao) == True:
            self.__lvl_persuasao = lvl_persuasao
        else:
            self.__lvl_persuasao = 0

    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):
        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("1 - Upar Habilidade de: Carisma")
                print("2 - Upar Habilidade de: Educacao")
                print("3 - Upar Habilidade de: Negocios")
                print("4 - Upar Habilidade de: Persuasao")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 1:  # Carisma
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_carisma) == True:
                    self.__lvl_carisma = self.__lvl_carisma + 1
                    print("subiu de nivel em Carisma!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 2:  # Educacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_educacao) == True:
                    self.__lvl_educacao = self.__lvl_educacao + 1
                    print("subiu de nivel em Educacao!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 3:  # Negocios
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_negocios) == True:
                    self.__lvl_negocios = self.__lvl_negocios + 1
                    print("subiu de nivel em Negocios!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 4:  # Persuasao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_persuasao) == True:
                    self.__lvl_persuasao = self.__lvl_persuasao + 1
                    print("subiu de nivel em Persuasao!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print("Voce nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm
class Sacerdote(Profissao):

    def __init__(self, lvl_criar_ritual=0, lvl_coragem=0, lvl_ensinar=0, lvl_lancar_feitico=0, nivel_geral=0):
        super().__init__(nivel_geral)

        # private
        if self.__valida_atributo_construtor(lvl_criar_ritual) == True:
            self.__lvl_criar_ritual = lvl_criar_ritual
        else:
            self.__lvl_criar_ritual = 0

        if self.__valida_atributo_construtor(lvl_coragem) == True:
            self.__lvl_coragem = lvl_coragem
        else:
            self.__lvl_coragem = 0

        if self.__valida_atributo_construtor(lvl_ensinar) == True:
            self.__lvl_ensinar = lvl_ensinar
        else:
            self.__lvl_ensinar = 0

        if self.__valida_atributo_construtor(lvl_lancar_feitico) == True:
            self.__lvl_lancar_feitico = lvl_lancar_feitico
        else:
            self.__lvl_lancar_feitico = 0

    
    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):
        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True: 
                #Colocar o treco do console aqui tbm
                print("1 - Upar Habilidade de: Criar Ritual")
                print("2 - Upar Habilidade de: Coragem")
                print("3 - Upar Habilidade de: Ensinar")
                print("4 - Upar Habilidade de: Lancar Feitico")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 1:  # Criar Ritual
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_criar_ritual) == True:
                    self.__lvl_criar_ritual = self.__lvl_criar_ritual + 1
                    print("subiu de nivel em Criar Ritual!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 2:  # Coragem
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_coragem) == True:
                    self.__lvl_coragem = self.__lvl_coragem + 1
                    print("subiu de nivel em Coragem!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 3:  # Ensinar
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_ensinar) == True:
                    self.__lvl_ensinar = self.__lvl_ensinar + 1
                    print("subiu de nivel em Ensinar!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 4:  # Lancar Feitico
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_lancar_feitico) == True:
                    self.__lvl_lancar_feitico = self.__lvl_lancar_feitico + 1
                    print("subiu de nivel em Lancar Feitico!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print("Voce nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm
class Desempregado(Profissao):

    def __init__(self, lvl_sobrevivencia=0, lvl_consciencia=0, nivel_geral=0):
        super().__init__(nivel_geral)

        # private
        if self.__valida_atributo_construtor(lvl_sobrevivencia) == True:
            self.__lvl_sobrevivencia = lvl_sobrevivencia
        else:
            self.__lvl_sobrevivencia = 0

        if self.__valida_atributo_construtor(lvl_consciencia) == True:
            self.__lvl_consciencia = lvl_consciencia
        else:
            self.__lvl_consciencia = 0


    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):
        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("1 - Upar Habilidade de: Sobrevivencia")
                print("2 - Upar Habilidade de: Consciencia")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 1 and opcao <= 2:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 1:  # Sobrevivencia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_sobrevivencia) == True:
                    self.__lvl_sobrevivencia = self.__lvl_sobrevivencia + 1
                    print("subiu de nivel em Sobrevivencia!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 2:  # Consciencia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self.__verifica_aumenta_lvl_habilidade(self.__lvl_consciencia) == True:
                    self.__lvl_consciencia = self.__lvl_consciencia + 1
                    print("subiu de nivel em Consciencia!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print("Voce nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm
class Jogador(ABC):

    def __init__(self, nome="Guest", hp=100, nivel_geral=0, lvl_brigar=0, lvl_apostar=0, lvl_forca=0, lvl_coragem=0, lvl_inteligencia=0):

        self._profissao_jogador = None
        self._nome = nome
        self._hp_maximo = 100
        self._qtd_pontos = 0  

        if self._valida_atributo_construtor(hp) == True:
            self._hp = hp
        else:
            self._hp = 0

        if self._valida_atributo_construtor(nivel_geral) == True:
            self._nivel_geral = nivel_geral
        else:
            self._nivel_geral = 0

        if self._valida_atributo_construtor(lvl_brigar) == True:
            self._lvl_brigar = lvl_brigar
        else:
            self._lvl_brigar = 0

        if self._valida_atributo_construtor(lvl_apostar) == True:
            self._lvl_apostar = lvl_apostar
        else:
            self._lvl_apostar = 0

        if self._valida_atributo_construtor(lvl_forca) == True:
            self._lvl_forca = lvl_forca
        else:
            self._lvl_forca = 0

        if self._valida_atributo_construtor(lvl_coragem) == True:
            self._lvl_coragem = lvl_coragem
        else:
            self._lvl_coragem = 0

        if self._valida_atributo_construtor(lvl_inteligencia) == True:
            self._lvl_inteligencia = lvl_inteligencia
        else:
            self._lvl_inteligencia = 0

    def _valida_atributo_construtor(self, valor):
        retorno = False

        if valor > 0:
            retorno = True

        return retorno

    def _transforma_pontos_experiencia(self):
        while self._nivel_geral >= 10:
            self._nivel_geral = self._nivel_geral - 10
            self._qtd_pontos = self._qtd_pontos + 1

        return

    def verifica_aumenta_lvl_habilidade(self, valor):
        retorno = True

        valor = valor + 1
        if valor > 13:
            retorno = False

        return retorno

    def aumenta_nivel_habilidade(self):

        opcao = 0

        if self._qtd_pontos > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("1 - Upar Habilidade de: Aposta")
                print("2 - Upar Habilidade de: Brigar")
                print("3 - Upar Habilidade de: Coragem")
                print("4 - Upar Habilidade de: Forca")
                print("5 - Upar Habilidade de: Inteligencia")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 1 and opcao <= 5:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 1:  # Aposta
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_apostar) == True:
                    self._lvl_apostar = self._lvl_apostar + 1
                    print(self._nome + " subiu de nivel em Aposta!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 2:  # Brigar
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_brigar) == True:
                    self._lvl_brigar = self._lvl_brigar + 1
                    print(self._nome + " subiu de nivel em Brigar!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 3:  # Coragem
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_coragem) == True:
                    self._lvl_coragem = self._lvl_coragem + 1
                    print(self._nome + " subiu de nivel em Coragem!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 4:  # Forca
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_forca) == True:
                    self._lvl_forca = self._lvl_forca + 1
                    print(self._nome + " subiu de nivel em Forca!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 5:  # Inteligencia
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_inteligencia) == True:
                    self._lvl_inteligencia = self._lvl_inteligencia + 1
                    print(self._nome + " subiu de nivel em Inteligencia!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print(self._nome + " nao tem pontos suficientes para subir de nivel")

    @abstractmethod
    def inicializa_jogador(self):
        pass

    def __del__(self):
        print("Removendo os dados do jogador: " + self._nome)

#fazer os getters e setters daqui tbbm
class Humano(Jogador):

    def __init__(self, nome="Guest", hp=100, nivel_geral=0, lvl_brigar=0, lvl_apostar=0, lvl_forca=0, lvl_coragem=0, lvl_inteligencia=0, imunidade=0, lvl_seducao=0, lvl_persuasao=0, lvl_teimosia=0):
        super().__init__(nome, hp, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_coragem, lvl_inteligencia)

        if self._valida_atributo_construtor(imunidade) == True:
            self.__imunidade = imunidade
        else:
            self.__imunidade = 0

        if self._valida_atributo_construtor(lvl_seducao) == True:
            self.__lvl_seducao = lvl_seducao
        else:
            self.__lvl_seducao = 0

        if self._valida_atributo_construtor(lvl_persuasao) == True:
            self.__lvl_persuasao = lvl_persuasao
        else:
            self.__lvl_persuasao = 0

        if self._valida_atributo_construtor(lvl_teimosia) == True:
            self.__lvl_teimosia = lvl_teimosia
        else:
            self.__lvl_teimosia = 0

    def inicializa_jogador(self):
        return

    def aumenta_nivel_habilidade(self):
        
        super().aumenta_nivel_habilidade()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("6 - Upar Habilidade de: Seducao")
                print("7 - Upar Habilidade de: Persuasao")
                print("8 - Upar Habilidade de: Teimosia")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 6 and opcao <= 8:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 6:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_seducao) == True:
                    self.__lvl_seducao = self.__lvl_seducao + 1
                    print(self._nome + " subiu de nivel em Seducao!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_persuasao) == True:
                    self.__lvl_persuasao = self.__lvl_persuasao + 1
                    print(self._nome + " subiu de nivel em Persuasao!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 8:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_teimosia) == True:
                    self.__lvl_teimosia = self.__lvl_teimosia + 1
                    print(self._nome + " subiu de nivel em Teimosia!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print(self._nome + " nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm
class Bruxo(Jogador):

    def __init__(self, nome="Guest", hp=100, nivel_geral=0, lvl_brigar=0, lvl_apostar=0, lvl_forca=0, lvl_coragem=0, lvl_inteligencia=0, lvl_reflexos_relampagos=0):
        super().__init__(nome, hp, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_coragem, lvl_inteligencia)

        self.__imunidade = 13   # private - bruxo tem o nivel maximo de imunidade
        self.__lvl_carisma = 0  # private - de acordo com o livro, bruxos tem carisma 0

        if self._valida_atributo_construtor(lvl_reflexos_relampagos) == True:
            self.__lvl_reflexos_relampagos = lvl_reflexos_relampagos
        else:
            self.__lvl_reflexos_relampagos = 0

    def inicializa_jogador(self):
        return

    def aumenta_nivel_habilidade(self):
        
        super().aumenta_nivel_habilidade()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("6 - Upar Habilidade de: Reflexos Relampagos")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao == 6:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 6:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_reflexos_relampagos) == True:
                    self.__lvl_reflexos_relampagos = self.__lvl_reflexos_relampagos + 1
                    print(self._nome + " subiu de nivel em Reflexos Relampagos!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print(self._nome + " nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm
class Anao(Jogador):

    def __init__(self, nome="Guest", hp=100, nivel_geral=0, lvl_brigar=0, lvl_apostar=0, lvl_forca=0, lvl_coragem=0, lvl_inteligencia=0, imunidade=0, lvl_armadura=0, lvl_deducao=0):
        super().__init__(nome, hp, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_coragem, lvl_inteligencia)

        if self._valida_atributo_construtor(imunidade) == True:
            self.__imunidade = imunidade
        else:
            self.__imunidade = 0

        if self._valida_atributo_construtor(lvl_armadura) == True:
            self.__lvl_armadura = lvl_armadura
        else:
            self.__lvl_armadura = 0

        if self._valida_atributo_construtor(lvl_deducao) == True:
            self.__lvl_deducao = lvl_deducao
        else:
            self.__lvl_deducao = 0


    def inicializa_jogador(self):
        return

    def aumenta_nivel_habilidade(self):
        
        super().aumenta_nivel_habilidade()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("6 - Upar Habilidade de: Armaduras")
                print("7 - Upar Habilidade de: Deducao")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 6 and opcao <= 7:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 6:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_armadura) == True:
                    self.__lvl_armadura = self.__lvl_armadura + 1
                    print(self._nome + " subiu de nivel em Armadura!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_deducao) == True:
                    self.__lvl_deducao = self.__lvl_deducao + 1
                    print(self._nome + " subiu de nivel em Deducao!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print(self._nome + " nao tem pontos suficientes para subir de nivel")

#fazer os getters e setters daqui tbbm
class Elfo(Jogador):

    def __init__(self, nome="Guest", hp=100, nivel_geral=0, lvl_brigar=0, lvl_apostar=0, lvl_forca=0, lvl_coragem=0, lvl_inteligencia=0, imunidade=0, lvl_artesanato=0, lvl_arcos=0, lvl_sintonia_natureza=0):
        super().__init__(nome, hp, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_coragem, lvl_inteligencia)

        if self._valida_atributo_construtor(imunidade) == True:
            self.__imunidade = imunidade
        else:
            self.__imunidade = 0

        if self._valida_atributo_construtor(lvl_artesanato) == True:
            self.__lvl_artesanato = lvl_artesanato
        else:
            self.__lvl_artesanato = 0

        if self._valida_atributo_construtor(lvl_arcos) == True:
            self.__lvl_arcos = lvl_arcos
        else:
            self.__lvl_arcos = 0

        if self._valida_atributo_construtor(lvl_sintonia_natureza) == True:
            self.__lvl_sintonia_natureza = lvl_sintonia_natureza
        else:
            self.__lvl_sintonia_natureza = 0

    def inicializa_jogador(self):
        return

    def aumenta_nivel_habilidade(self):

        super().aumenta_nivel_habilidade()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:
                #Colocar o treco do console aqui tbm
                print("6 - Upar Habilidade de: Artesanato")
                print("7 - Upar Habilidade de: Artilharia de Arcos")
                print("8 - Upar Habilidade de: Sintonia da Natureza")
                print("Digite uma opcao: ")
                opcao = int(input())

                if opcao >= 6 and opcao <= 8:
                    break
                else:
                    print("Digite uma opcao valida!")

            if opcao == 6:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_artesanato) == True:
                    self.__lvl_artesanato = self.__lvl_artesanato + 1
                    print(self._nome + " subiu de nivel em Artesanato!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_arcos) == True:
                    self.__lvl_arcos = self.__lvl_arcos + 1
                    print(self._nome + " subiu de nivel em Artilharia de Arcos!")
                else:
                    print("Voce ja esta no nivel maximo!")

            elif opcao == 8:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_sintonia_natureza) == True:
                    self.__lvl_sintonia_natureza = self.__lvl_sintonia_natureza + 1
                    print(self._nome + " subiu de nivel em Sintonia da Natureza!")
                else:
                    print("Voce ja esta no nivel maximo!")

        else:
            print(self._nome + " nao tem pontos suficientes para subir de nivel")


class JogadorFactory:

    @staticmethod
    def criar_jogador(tipo, nome, hp, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_coragem, lvl_inteligencia, imunidade=0, lvl_seducao=0, lvl_persuasao=0, lvl_teimosia=0, lvl_reflexos_relampagos=0, lvl_armadura=0, lvl_deducao=0, lvl_artesanato=0, lvl_arcos=0, lvl_sintonia_natureza=0):

        #tenho q fazer o menu na main, e jogar pra verificar antes de entrar no método fabric
        jogador = None
        
        match tipo:
            case 1: #Humano
                jogador = Humano(nome, hp, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_coragem, lvl_inteligencia, imunidade, lvl_seducao, lvl_persuasao, lvl_teimosia)
            case 2: #Bruxo
                jogador = Bruxo(nome, hp, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_coragem, lvl_inteligencia, lvl_reflexos_relampagos)
            case 3: #Anão
                jogador = Anao(nome, hp, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_coragem, lvl_inteligencia, imunidade, lvl_armadura, lvl_deducao)
            case 4: #Elfo
                jogador = Elfo(nome, hp, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_coragem, lvl_inteligencia, imunidade, lvl_artesanato, lvl_arcos, lvl_sintonia_natureza)

        return jogador
    
class ProfissaoFactory:

    @staticmethod
    def criar_profissao(tipo, nivel_geral=0):

        #A ideia é q em profissão o jogador fazendo as tasks ele aumente de nível para upar
        #tenho q fazer o menu na main, e jogar pra verificar antes de entrar no método fabric (mesmo q na de cima)

        profissao = None

        match tipo:

            case 1: #Mago
                profissao = Mago(nivel_geral=nivel_geral)
            case 2: #Bardo
                profissao = Bardo(nivel_geral=nivel_geral)
            case 3: #Artesao
                profissao = Artesao(nivel_geral=nivel_geral)
            case 4: #Criminoso
                profissao = Criminoso(nivel_geral=nivel_geral)
            case 5: #Doutor
                profissao = Doutor(nivel_geral=nivel_geral)
            case 6: #Cavaleiro
                profissao = Cavaleiro(nivel_geral=nivel_geral)
            case 7: #Comerciante
                profissao = Comerciante(nivel_geral=nivel_geral)
            case 8: #Sacerdote
                profissao = Sacerdote(nivel_geral=nivel_geral)
            case 9: #Desempregado
                profissao = Desempregado(nivel_geral=nivel_geral)

        return profissao


# -> Classe com interface para realizar as tasks
# -> ? Gerenciador ? -> A pensar

class ExcessaoTipoOpcaoInvalido(Exception):

    def __str__(self):
        return f"Digite um número inteiro!"
    
class ExcessaoOpcaoInvalida(Exception):

    def __str__(self):
        return f"Digite uma opcao válida!"

def menu_jogador():

    console = Console()

    while True:

        console.print(
            Panel(
                Align.center(
                    "1 - Humano \n"
                    "2 - Bruxo \n"
                    "3 - Anão \n"
                    "4 - Elfo"
                ),                
                title= "Escolha a raça do seu personagem"
                
            )
        )

        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            raise ExcessaoTipoOpcaoInvalido

        if(opcao >= 1 and opcao <= 4):
            break
        else:
            raise ExcessaoOpcaoInvalida()

    return opcao

def menu_profissao():

    console = Console()

    while True:

        console.print(
            Panel(
                Align.center(
                   "1 - Ser um Mago \n"
                    "2 - Ser um Bardo \n"
                    "3 - Ser um Artesão \n"
                    "4 - Ser um Criminoso \n"
                    "5 - Ser um Doutor \n"
                    "6 - Ser um Cavaleiro \n"
                    "7 - Ser um Comerciante \n"
                    "8 - Ser um Sacerdote \n"
                    "9 - Ser um Desempregado"
                ),                
                title= "Escolha o que o seu personagem vai ser"
                
            )
        )        

        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            raise ExcessaoTipoOpcaoInvalido()

        if(opcao >= 1 and opcao <= 9):
            break
        else:
            raise ExcessaoOpcaoInvalida()
        
    return opcao

if __name__ == "__main__":

    console = Console()

    fonte = Figlet(font="starwars")

    print(fonte.renderText("RPG"))
    print(fonte.renderText("The Witcher"))

    console.print(
        Panel(
            Align.center("Digite o nome do personagem:")
        )
    )
    nome = input("")

    opcao_jogador = menu_jogador()

    jogador = JogadorFactory.criar_jogador(opcao_jogador,nome,100,0,0,0,0,0,0)

    opcao_profissao = menu_profissao()

    profissao = ProfissaoFactory.criar_profissao(opcao_profissao)

    jogador._profissao_jogador = profissao

    print("\nPersonagem criado com sucesso!")
    print("Nome:", jogador._nome)
    print("Raça:", type(jogador).__name__) #trocar isso dps por um getter plmds -A
    print("Profissão:", type(jogador._profissao_jogador).__name__) #trocar isso dps por um getter plmds -A
