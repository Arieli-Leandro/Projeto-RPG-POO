from abc import ABC, abstractmethod
from exceptions.excessoes import *
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

"""
Nesse arquivo temos a classe Mãe Profissao que é uma classe Abstrata e as suas Classes Filhas:
Mago, Bardo, Artesão, Criminoso, Doutor, Cavaleiro, Comerciante, Sacerdote e Desempregado.

Na classe mãe temos as variáveis e métodos básicos que toda profissão obrigatoriamente possui, como:

-> Nível Geral da Profissão
-> Quantidade de Pontos de Profissão
-> Conversão de Experiência em Pontos de Habilidade
-> Verificação de Limite Máximo de Nível das Habilidades

Cada profissão possui habilidades específicas retiradas do livro de RPG de The Witcher (menos Desempregado), sendo elas:

-> Mago:
   Criar Ritual, Lançar Feitiço, Educação e Resistir Magia

-> Bardo:
   Etiqueta Social, Ludibriar e Sabedoria das Ruas

-> Artesão:
   Educação, Criação, Negociação e Físico

-> Criminoso:
   Arrombar Fechaduras, Falsificação, Atletismo e Sabedoria das Ruas

-> Doutor:
   Carisma, Educação, Coragem e Alquimia

-> Cavaleiro:
   Coragem, Intimidação, Sobrevivência e Esquivar

-> Comerciante:
   Carisma, Educação, Negócios e Persuasão

-> Sacerdote:
   Criar Ritual, Coragem, Ensinar e Lançar Feitiço

-> Desempregado:
   Sobrevivência e Consciência

Todas as profissões possuem getters e setters para suas respectivas habilidades, permitindo que os
atributos sejam manipulados sem acessar diretamente as variáveis privadas da classe.

A função transforma_pontos_experiencia() é responsável por converter a experiência acumulada em
pontos de profissão. Para cada 10 pontos de experiência acumulados, o personagem recebe 1 ponto
que poderá ser utilizado para aumentar uma habilidade da profissão escolhida.

A função aumenta_nivel_habilidade_profissao() é responsável por permitir que o usuário escolha qual
habilidade da sua profissão deseja evoluir. Antes de realizar a melhoria da habilidade, o sistema
verifica se o personagem possui pontos suficientes e se a habilidade ainda não atingiu o nível máximo.

Foi definido que todas as habilidades possuem nível máximo 13, evitando que um personagem fique
excessivamente forte em apenas uma característica e mantendo um maior equilíbrio durante o jogo.
"""

class Profissao(ABC):

    def __init__(self, nivel_geral_profissao=0):
        self._qtd_pontos_profissao = 0 
        self.setNivelGeral(nivel_geral_profissao)

    #método setter
    def setNivelGeral(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self._nivel_geral_profissao = valor
        else:
            self._nivel_geral_profissao = 0

        return
        
    #método getter
    def getNivelGeral(self):
        return self._nivel_geral_profissao

    def getNomeProfissao(self):
        return self.__class__.__name__

    def _valida_atributo_construtor(self, valor):
        retorno = False

        if valor > 0:
            retorno = True

        return retorno

    def transforma_pontos_experiencia(self):
        while self._nivel_geral_profissao >= 10:
            self._nivel_geral_profissao = self._nivel_geral_profissao - 10
            self._qtd_pontos_profissao = self._qtd_pontos_profissao + 1

        return

    def _verifica_aumenta_lvl_habilidade(self, valor):
        retorno = True

        valor = valor + 1
        if valor > 13:
            retorno = False

        return retorno

    @abstractmethod
    def inicializa_profissao(self):
        pass

    def __del__(self):
        print("")

class Mago(Profissao):

    def __init__(self, lvl_criar_ritual=0, lvl_lancar_feitico=0, lvl_educacao=0, lvl_resistir_magia=0, nivel_geral=0):
        super().__init__(nivel_geral)
        self.setLvlCriarRitual(lvl_criar_ritual)
        self.setLvlLancarFeitico(lvl_lancar_feitico)
        self.setLvlEducacao(lvl_educacao)
        self.setLvlResistirMagia(lvl_resistir_magia)

    #Métodos getters
    def getLvlCriarRitual(self):
        return self.__lvl_criar_ritual
    
    def getLvlLancarFeitico(self):
        return self.__lvl_lancar_feitico
    
    def getLvlEducacao(self):
        return self.__lvl_educacao
    
    def getLvlResistirMagia(self):
        return self.__lvl_resistir_magia

    #Métodos setters
    def setLvlCriarRitual(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_criar_ritual = valor
        else:
            self.__lvl_criar_ritual = 0
            
        return
    
    def setLvlLancarFeitico(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_lancar_feitico = valor
        else: 
            self.__lvl_lancar_feitico = 0

        return
    
    def setLvlEducacao(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_educacao = valor
        else:
            self.__lvl_educacao = 0

        return
    
    def setLvlResistirMagia(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_resistir_magia = valor
        else:
            self.__lvl_resistir_magia = 0

        return    

    #Métodos da classe
    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):

        self.transforma_pontos_experiencia()

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                console.print(
                    Panel(
                        Align.center(
                            "1 - Upar Habilidade de: Criar Ritual \n"
                            "2 - Upar Habilidade de: Educação \n"
                            "3 - Upar Habilidade de: Lancar Feitico \n"
                            "4 - Upar Habilidade de: Resistir Magia"
                        ),title="❇ Subir de LVL: Skill Profissão ❇"))
                
                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 1:  # Criar Ritual
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_criar_ritual) == True:
                    self.__lvl_criar_ritual = self.__lvl_criar_ritual + 1
                    print("Subiu de nível em Criar Ritual!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 2:  # Educacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_educacao) == True:
                    self.__lvl_educacao = self.__lvl_educacao + 1
                    print("Subiu de nível em Educação!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
                
            elif opcao == 3:  # Lancar Feitico
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_lancar_feitico) == True:
                    self.__lvl_lancar_feitico = self.__lvl_lancar_feitico + 1
                    print("Subiu de nível em Lancar Feitico!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 4:  # Resistir Magia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_resistir_magia) == True:
                    self.__lvl_resistir_magia = self.__lvl_resistir_magia + 1
                    print("Subiu de nível em Resistir a Magia!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

        else:
            print("Seu personagem não tem pontos suficientes para subir de nível!")

class Bardo(Profissao):

    def __init__(self, lvl_etiqueta_social=0, lvl_ludibriar=0, lvl_sabedoria_das_ruas=0, nivel_geral=0):
        super().__init__(nivel_geral)
        self.setLvlEtiquetaSocial(lvl_etiqueta_social)
        self.setLvlLudibriar(lvl_ludibriar)
        self.setLvlSabedoriaDasRuas(lvl_sabedoria_das_ruas)

    #Métodos getters
    def getLvlEtiquetaSocial(self):
        return self.__lvl_etiqueta_social
    
    def getLvlLudibriar(self):
        return self.__lvl_ludibriar
    
    def getLvlSabedoriaDasRuas(self):
        return self.__lvl_sabedoria_das_ruas

    #Métodos setters
    def setLvlEtiquetaSocial(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_etiqueta_social = valor
        else:
            self.__lvl_etiqueta_social = 0

        return 
    
    def setLvlLudibriar(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_ludibriar = valor
        else:
            self.__lvl_ludibriar = 0

        return
    
    def setLvlSabedoriaDasRuas(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_sabedoria_das_ruas = valor
        else:
            self.__lvl_sabedoria_das_ruas = 0

        return

    #Métodos da classe
    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):

        self.transforma_pontos_experiencia()

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Etiqueta Social \n"
                    "2 - Upar Habilidade de: Ludibriar \n"
                    "3 - Upar Habilidade de: Sabedoria das Ruas"
                ),title="❇ Subir de LVL: Skill Profissão ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 1 and opcao <= 3:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 1:  # Etiqueta Social
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_etiqueta_social) == True:
                    self.__lvl_etiqueta_social = self.__lvl_etiqueta_social + 1
                    print("Subiu de nível em Etiqueta Social!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 2:  # Ludibriar
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_ludibriar) == True:
                    self.__lvl_ludibriar = self.__lvl_ludibriar + 1
                    print("Subiu de nível em Ludibriar!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 3:  # Sabedoria das Ruas
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_sabedoria_das_ruas) == True:
                    self.__lvl_sabedoria_das_ruas = self.__lvl_sabedoria_das_ruas + 1
                    print("Subiu de nível em Sabedoria das Ruas!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

        else:
            print("Seu personagem não tem pontos suficientes para subir de nível!")

class Artesao(Profissao):

    def __init__(self, lvl_educacao=0, lvl_criacao=0, lvl_negociacao=0, lvl_fisico=0, nivel_geral=0):
        super().__init__(nivel_geral)
        self.setLvlEducacao(lvl_educacao)
        self.setLvlCriacao(lvl_criacao)
        self.setLvlNegociacao(lvl_negociacao)
        self.setLvlFisico(lvl_fisico)

    #Métodos getters
    def getLvlEducacao(self):
        return self.__lvl_educacao
    
    def getLvlCriacao(self):
        return self.__lvl_criacao
    
    def getLvlNegociacao(self):
        return self.__lvl_negociacao
    
    def getLvlFisico(self):
        return self.__lvl_fisico

    #Métodos setters
    def setLvlEducacao(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_educacao = valor
        else: 
            self.__lvl_educacao = 0

        return
    
    def setLvlCriacao(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_criacao = valor
        else:
            self.__lvl_criacao = 0

        return
    
    def setLvlNegociacao(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_negociacao = valor
        else:
            self.__lvl_negociacao = 0

        return
    
    def setLvlFisico(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_fisico = valor
        else: 
            self.__lvl_fisico = 0
        return

    #Métodos da classe
    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):

        self.transforma_pontos_experiencia()

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Educação \n"
                    "2 - Upar Habilidade de: Criação \n"
                    "3 - Upar Habilidade de: Negociação \n"
                    "4 - Upar Habilidade de: Físico"
                ),title="❇ Subir de LVL: Skill Profissão ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 1:  # Educacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_educacao) == True:
                    self.__lvl_educacao = self.__lvl_educacao + 1
                    print("Subiu de nível em Educação!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 2:  # Criacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_criacao) == True:
                    self.__lvl_criacao = self.__lvl_criacao + 1
                    print("Subiu de nível em Criação!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 3:  # Negociacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_negociacao) == True:
                    self.__lvl_negociacao = self.__lvl_negociacao + 1
                    print("Subiu de nível em Negociação!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 4:  # Fisico
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_fisico) == True:
                    self.__lvl_fisico = self.__lvl_fisico + 1
                    print("Subiu de nível em Físico!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

        else:
            print("Seu personagem não tem pontos suficientes para subir de nível!")

class Criminoso(Profissao):

    def __init__(self, lvl_arrombar_fechaduras=0, lvl_falsificacao=0, lvl_atletismo=0, lvl_sabedoria_das_ruas=0, nivel_geral=0):
        super().__init__(nivel_geral)
        self.setLvlArrombarFechaduras(lvl_arrombar_fechaduras)
        self.setLvlFalsificacao(lvl_falsificacao)
        self.setLvlAtletismo(lvl_atletismo)
        self.setLvlSabedoriaDasRuas(lvl_sabedoria_das_ruas)

    #Métodos getters
    def getLvlArrombarFechaduras(self):
        return self.__lvl_arrombar_fechaduras
    
    def getLvlFalsificacao(self):
        return self.__lvl_falsificacao
    
    def getLvlAtletismo(self):
        return self.__lvl_atletismo
    
    def getLvlSabedoriaDasRuas(self):
        return self.__lvl_sabedoria_das_ruas

    #Métodos setters
    def setLvlArrombarFechaduras(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_arrombar_fechaduras = valor
        else:
            self.__lvl_arrombar_fechaduras = 0

        return
    
    def setLvlFalsificacao(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_falsificacao = valor
        else:
            self.__lvl_falsificacao = 0

        return
    
    def setLvlAtletismo(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_atletismo = valor
        else:
            self.__lvl_atletismo = 0

        return
    
    def setLvlSabedoriaDasRuas(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_sabedoria_das_ruas = valor
        else:
            self.__lvl_sabedoria_das_ruas = 0

        return

    #Métodos da classe
    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):

        self.transforma_pontos_experiencia()

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:

                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Arrombar Fechadura \n"
                    "2 - Upar Habilidade de: Falsificacao \n"
                    "3 - Upar Habilidade de: Atletismo \n"
                    "4 - Upar Habilidade de: Sabedoria das Ruas"
                ),title="❇ Subir de LVL: Skill Profissão ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 1:  # Arrombar Fechadura
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_arrombar_fechaduras) == True:
                    self.__lvl_arrombar_fechaduras = self.__lvl_arrombar_fechaduras + 1
                    print("Subiu de nível em Arrombar Fechaduras!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 2:  # Falsificacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_falsificacao) == True:
                    self.__lvl_falsificacao = self.__lvl_falsificacao + 1
                    print("Subiu de nível em Falsificação!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 3:  # Atletismo
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_atletismo) == True:
                    self.__lvl_atletismo = self.__lvl_atletismo + 1
                    print("Subiu de nível em Atletismo!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 4:  # Sabedoria das Ruas
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_sabedoria_das_ruas) == True:
                    self.__lvl_sabedoria_das_ruas = self.__lvl_sabedoria_das_ruas + 1
                    print("Subiu de nível em Sabedoria das Ruas!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
        else:
            print("Seu personagem não tem pontos suficientes para subir de nível!")

class Doutor(Profissao):

    def __init__(self, lvl_carisma=0, lvl_educacao=0, lvl_coragem=0, lvl_alquimia=0, nivel_geral=0):
        super().__init__(nivel_geral)
        self.setLvlCarisma(lvl_carisma)
        self.setLvlCarisma(lvl_educacao)
        self.setLvlCoragem(lvl_coragem)
        self.setLvlAlquimia(lvl_alquimia)

    #Métodos getters
    def getLvlCarisma(self):
        return self.__lvl_carisma
    
    def getLvlEducacao(self):
        return self.__lvl_educacao
    
    def getLvlCoragem(self):
        return self.__lvl_coragem
    
    def getLvlAlquimia(self):
        return self.__lvl_alquimia

    #Métodos setters:
    def setLvlCarisma(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_carisma = valor
        else:
            self.__lvl_carisma = 0

        return

    def setLvlEducacao(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_educacao = valor
        else:
            self.__lvl_educacao = 0

        return

    def setLvlCoragem(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_coragem = valor
        else:
            self.__lvl_coragem = 0

        return

    def setLvlAlquimia(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_alquimia = valor
        else:
            self.__lvl_alquimia = 0

        return

    #Métodos da classe
    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):

        self.transforma_pontos_experiencia()

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True: 
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Educação \n"
                    "2 - Upar Habilidade de: Coragem \n"
                    "3 - Upar Habilidade de: Alquimia \n"
                    "4 - Upar Habilidade de: Carisma"
                ),title="❇ Subir de LVL: Skill Profissão ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 1:  # Educacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_educacao) == True:
                    self.__lvl_educacao = self.__lvl_educacao + 1
                    print("Subiu de nível em Educação!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 2:  # Coragem
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_coragem) == True:
                    self.__lvl_coragem = self.__lvl_coragem + 1
                    print("Subiu de nível em Coragem!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 3:  # Alquimia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_alquimia) == True:
                    self.__lvl_alquimia = self.__lvl_alquimia + 1
                    print("Subiu de nível em Alquimia!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
                
            elif opcao == 4:  # Carisma
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_carisma) == True:
                    self.__lvl_carisma = self.__lvl_carisma + 1
                    print("Subiu de nível em Carisma!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

        else:
            print("Seu personagem não tem pontos suficientes para subir de nível!")

class Cavaleiro(Profissao):

    def __init__(self, lvl_coragem=0, lvl_intimidacao=0, lvl_sobrevivencia=0, lvl_esquivar=0, nivel_geral=0):
        super().__init__(nivel_geral)
        self.setLvlCoragem(lvl_coragem)
        self.setLvlIntimidacao(lvl_intimidacao)
        self.setLvlSobrevivencia(lvl_sobrevivencia)
        self.setLvlEsquivar(lvl_esquivar)

    #Métodos getters
    def getLvlCoragem(self):
        return self.__lvl_coragem
    
    def getLvlIntimidacao(self):
        return self.__lvl_intimidacao
    
    def getLvlSobrevivencia(self):
        return self.__lvl_sobrevivencia
    
    def getLvlEsquivar(self):
        return self.__lvl_esquivar

    #Métodos setters
    def setLvlCoragem(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_coragem = valor
        else:
            self.__lvl_coragem = 0

        return
    
    def setLvlIntimidacao(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_intimidacao = valor
        else:
            self.__lvl_intimidacao = 0

        return
    
    def setLvlEsquivar(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_esquivar = valor
        else:
            self.__lvl_esquivar = 0

        return

    def setLvlSobrevivencia(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_sobrevivencia = valor
        else:
            self.__lvl_sobrevivencia = 0

        return

    #Métodos da classe
    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):

        self.transforma_pontos_experiencia()

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Coragem \n"
                    "2 - Upar Habilidade de: Intimidação \n"
                    "3 - Upar Habilidade de: Sobrevivência \n"
                    "4 - Upar Habilidade de: Esquivar"
                ),title="❇ Subir de LVL: Skill Profissão ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 1:  # Coragem
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_coragem) == True:
                    self.__lvl_coragem = self.__lvl_coragem + 1
                    print("Subiu de nível em Coragem!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 2:  # Intimidacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_intimidacao) == True:
                    self.__lvl_intimidacao = self.__lvl_intimidacao + 1
                    print("Subiu de nível em Intimidacao!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 3:  # Sobrevivencia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_sobrevivencia) == True:
                    self.__lvl_sobrevivencia = self.__lvl_sobrevivencia + 1
                    print("Subiu de nível em Sobrevivência!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 4:  # Esquivar
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_esquivar) == True:
                    self.__lvl_esquivar = self.__lvl_esquivar + 1
                    print("Subiu de nível em Esquivar!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
        else:
            print("Seu personagem não tem pontos suficientes para subir de nível!")

class Comerciante(Profissao):

    def __init__(self, lvl_carisma=0, lvl_educacao=0, lvl_negocios=0, lvl_persuasao=0, nivel_geral=0):
        super().__init__(nivel_geral)
        self.setLvlCarisma(lvl_carisma)
        self.setLvlEducacao(lvl_educacao)
        self.setLvlNegocios(lvl_negocios)
        self.setLvlPersuasao(lvl_persuasao)

    #Métodos getters
    def getLvlCarisma(self):
        return self.__lvl_carisma
    
    def getLvlEducacao(self):
        return self.__lvl_educacao

    def getLvlNegocios(self):
        return self.__lvl_negocios
    
    def getLvlPersuasao(self):
        return self.__lvl_persuasao

    #Métodos setters
    def setLvlCarisma(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_carisma = valor
        else:
            self.__lvl_carisma = 0

        return
    
    def setLvlEducacao(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_educacao = valor
        else:
            self.__lvl_educacao = 0

        return
    
    def setLvlNegocios(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_negocios = valor
        else:
            self.__lvl_negocios = 0

        return
    
    def setLvlPersuasao(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_persuasao = valor
        else:
            self.__lvl_persuasao = 0

        return

    #Métodos da classe
    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):

        self.transforma_pontos_experiencia()

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Carisma \n"
                    "2 - Upar Habilidade de: Educação \n"
                    "3 - Upar Habilidade de: Negócios \n"
                    "4 - Upar Habilidade de: Persuasão"
                ),title="❇ Subir de LVL: Skill Profissão ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 1:  # Carisma
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_carisma) == True:
                    self.__lvl_carisma = self.__lvl_carisma + 1
                    print("Subiu de nível em Carisma!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 2:  # Educacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_educacao) == True:
                    self.__lvl_educacao = self.__lvl_educacao + 1
                    print("Subiu de nível em Educação!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 3:  # Negocios
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_negocios) == True:
                    self.__lvl_negocios = self.__lvl_negocios + 1
                    print("Subiu de nível em Negócios!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 4:  # Persuasao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_persuasao) == True:
                    self.__lvl_persuasao = self.__lvl_persuasao + 1
                    print("Subiu de nível em Persuasão!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
        else:
            print("Seu personagem não tem pontos suficientes para subir de nível!")

class Sacerdote(Profissao):

    def __init__(self, lvl_criar_ritual=0, lvl_coragem=0, lvl_ensinar=0, lvl_lancar_feitico=0, nivel_geral=0):
        super().__init__(nivel_geral)
        self.setLvlCriarRitual(lvl_criar_ritual)
        self.setLvlCoragem(lvl_coragem)
        self.setLvlEnsinar(lvl_ensinar)
        self.setLvlLancarFeitico(lvl_lancar_feitico)

    #Métodos getters
    def getLvlCriarRitual(self):
        return self.__lvl_criar_ritual
    
    def getLvlCoragem(self):
        return self.__lvl_coragem
    
    def getLvlEnsinar(self):
        return self.__lvl_ensinar

    def getLvlLancarFeitico(self):
        return self.__lvl_lancar_feitico

    #Métodos setters
    def setLvlCriarRitual(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_criar_ritual = valor
        else:
            self.__lvl_criar_ritual = 0

        return
    
    def setLvlCoragem(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_coragem = valor
        else:
            self.__lvl_coragem = 0

        return
    
    def setLvlEnsinar(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_ensinar = valor
        else:
            self.__lvl_ensinar = 0

        return
    
    def setLvlLancarFeitico(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_lancar_feitico = valor
        else:
            self.__lvl_lancar_feitico = 0

        return

    #Métodos da classe
    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):

        self.transforma_pontos_experiencia()

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True: 
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Criar Ritual \n"
                    "2 - Upar Habilidade de: Coragem \n"
                    "3 - Upar Habilidade de: Ensinar \n"
                    "4 - Upar Habilidade de:  Lançar Feitiço"
                ),title="❇ Subir de LVL: Skill Profissão ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 1 and opcao <= 4:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 1:  # Criar Ritual
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_criar_ritual) == True:
                    self.__lvl_criar_ritual = self.__lvl_criar_ritual + 1
                    print("Subiu de nível em Criar Ritual!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 2:  # Coragem
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_coragem) == True:
                    self.__lvl_coragem = self.__lvl_coragem + 1
                    print("Subiu de nível em Coragem!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 3:  # Ensinar
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_ensinar) == True:
                    self.__lvl_ensinar = self.__lvl_ensinar + 1
                    print("Subiu de nível em Ensinar!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 4:  # Lancar Feitico
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_lancar_feitico) == True:
                    self.__lvl_lancar_feitico = self.__lvl_lancar_feitico + 1
                    print("Subiu de nível em Lançar Feitiço!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
        else:
            print("Seu personagem não tem pontos suficientes para subir de nível!")

class Desempregado(Profissao):

    def __init__(self, lvl_sobrevivencia=0, lvl_consciencia=0, nivel_geral=0):
        super().__init__(nivel_geral)
        self.setLvlSobrevivencia(lvl_sobrevivencia)
        self.setLvlConsciencia(lvl_consciencia)

    #Métodos getters
    def getLvlSobrevivencia(self):
        return self.__lvl_sobrevivencia
    
    def getLvlConsciencia(self):
        return self.__lvl_consciencia
    
    #Métodos setters
    def setLvlSobrevivencia(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_sobrevivencia = valor
        else:
            self.__lvl_sobrevivencia = 0

        return
    
    def setLvlConsciencia(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_consciencia = valor
        else:
            self.__lvl_consciencia = 0

        return

    #Métodos da classe
    def inicializa_profissao(self):
        return

    def aumenta_nivel_habilidade_profissao(self):

        self.transforma_pontos_experiencia()

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Sobrevivência \n"
                    "2 - Upar Habilidade de: Consciência \n"
                    "3 - Upar Habilidade de: Ensinar \n"
                    "4 - Upar Habilidade de:  Lancar Feitiço"
                ),title="❇ Subir de LVL: Skill Profissão ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 1 and opcao <= 2:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 1:  # Sobrevivencia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_sobrevivencia) == True:
                    self.__lvl_sobrevivencia = self.__lvl_sobrevivencia + 1
                    print("Subiu de nível em Sobrevivência!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 2:  # Consciencia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_consciencia) == True:
                    self.__lvl_consciencia = self.__lvl_consciencia + 1
                    print("Subiu de nível em Consciência!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
        else:
            print("Seu personagem não tem pontos suficientes para subir de nível!")