""" Quadro de atualizações q eu tenho q fzr (-A)
-> Música via terminal pelo Pyfliglet 
-> Colocar cor no Terminal
-> Métodos de interface para funções de atacar e curar (Atacar vai dar o xp pra upar as skills)
-> Interface Gráfica
-> Separar em outros arquivos
-> Jogador e Profissão estão funcionando perfeitamente
"""

from abc import ABC, abstractmethod
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

# =------ Excessões ------= #Tudo OK
class ExcessaoNivelGeralInvalido(Exception):
    def __str__(self):
        return f"Valor de nível geral inválido!"
    
class ExcessaoNivelMaximo(Exception):
    def __str__(self):
        return f"Seu personagem já está com essa skill no nível Máximo!"
    
class ExcessaoPontosInsuficientesSubirNivel(Exception):
    def __str__(self):
        return f"Seu personagem não tem pontos suficientes para subir de nível!"
    
class ExcessaoTipoOpcaoInvalido(Exception):
    def __str__(self):
        return f"Digite um número inteiro!"
    
class ExcessaoOpcaoInvalida(Exception):
    def __str__(self):
        return f"Digite uma opção válida!"
    
class ExcessaoNomeJogadorInvalido(Exception):
    def __str__(self):
        return f"Digite um nome válido!"

#Tudo OK
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
        print("Profissao deletada")

#Tudo OK
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
                    raise ExcessaoNivelMaximo()

            elif opcao == 2:  # Educacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_educacao) == True:
                    self.__lvl_educacao = self.__lvl_educacao + 1
                    print("Subiu de nível em Educação!")
                else:
                    raise ExcessaoNivelMaximo()
                
            elif opcao == 3:  # Lancar Feitico
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_lancar_feitico) == True:
                    self.__lvl_lancar_feitico = self.__lvl_lancar_feitico + 1
                    print("Subiu de nível em Lancar Feitico!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 4:  # Resistir Magia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_resistir_magia) == True:
                    self.__lvl_resistir_magia = self.__lvl_resistir_magia + 1
                    print("Subiu de nível em Resistir a Magia!")
                else:
                    raise ExcessaoNivelMaximo()

        else:
            raise ExcessaoPontosInsuficientesSubirNivel()

#Tudo OK
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
                    raise ExcessaoNivelMaximo()

            elif opcao == 2:  # Ludibriar
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_ludibriar) == True:
                    self.__lvl_ludibriar = self.__lvl_ludibriar + 1
                    print("Subiu de nível em Ludibriar!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 3:  # Sabedoria das Ruas
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_sabedoria_das_ruas) == True:
                    self.__lvl_sabedoria_das_ruas = self.__lvl_sabedoria_das_ruas + 1
                    print("Subiu de nível em Sabedoria das Ruas!")
                else:
                    raise ExcessaoNivelMaximo()

        else:
            raise ExcessaoPontosInsuficientesSubirNivel()

#Tudo OK
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
                    raise ExcessaoNivelMaximo()

            elif opcao == 2:  # Criacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_criacao) == True:
                    self.__lvl_criacao = self.__lvl_criacao + 1
                    print("Subiu de nível em Criação!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 3:  # Negociacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_negociacao) == True:
                    self.__lvl_negociacao = self.__lvl_negociacao + 1
                    print("Subiu de nível em Negociação!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 4:  # Fisico
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_fisico) == True:
                    self.__lvl_fisico = self.__lvl_fisico + 1
                    print("Subiu de nível em Físico!")
                else:
                    raise ExcessaoNivelMaximo()

        else:
            raise ExcessaoPontosInsuficientesSubirNivel()

#Tudo OK
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
                    raise ExcessaoNivelMaximo()

            elif opcao == 2:  # Falsificacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_falsificacao) == True:
                    self.__lvl_falsificacao = self.__lvl_falsificacao + 1
                    print("Subiu de nível em Falsificação!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 3:  # Atletismo
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_atletismo) == True:
                    self.__lvl_atletismo = self.__lvl_atletismo + 1
                    print("Subiu de nível em Atletismo!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 4:  # Sabedoria das Ruas
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_sabedoria_das_ruas) == True:
                    self.__lvl_sabedoria_das_ruas = self.__lvl_sabedoria_das_ruas + 1
                    print("Subiu de nível em Sabedoria das Ruas!")
                else:
                    raise ExcessaoNivelMaximo()
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()

#Tudo OK
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
                    raise ExcessaoNivelMaximo()

            elif opcao == 2:  # Coragem
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_coragem) == True:
                    self.__lvl_coragem = self.__lvl_coragem + 1
                    print("Subiu de nível em Coragem!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 3:  # Alquimia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_alquimia) == True:
                    self.__lvl_alquimia = self.__lvl_alquimia + 1
                    print("Subiu de nível em Alquimia!")
                else:
                    raise ExcessaoNivelMaximo()
                
            elif opcao == 4:  # Carisma
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_carisma) == True:
                    self.__lvl_carisma = self.__lvl_carisma + 1
                    print("Subiu de nível em Carisma!")
                else:
                    raise ExcessaoNivelMaximo()

        else:
            raise ExcessaoPontosInsuficientesSubirNivel()

#Tudo OK
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
                    raise ExcessaoNivelMaximo()

            elif opcao == 2:  # Intimidacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_intimidacao) == True:
                    self.__lvl_intimidacao = self.__lvl_intimidacao + 1
                    print("Subiu de nível em Intimidacao!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 3:  # Sobrevivencia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_sobrevivencia) == True:
                    self.__lvl_sobrevivencia = self.__lvl_sobrevivencia + 1
                    print("Subiu de nível em Sobrevivência!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 4:  # Esquivar
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_esquivar) == True:
                    self.__lvl_esquivar = self.__lvl_esquivar + 1
                    print("Subiu de nível em Esquivar!")
                else:
                    raise ExcessaoNivelMaximo()
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()

#Tudo OK
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
                    raise ExcessaoNivelMaximo()

            elif opcao == 2:  # Educacao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_educacao) == True:
                    self.__lvl_educacao = self.__lvl_educacao + 1
                    print("Subiu de nível em Educação!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 3:  # Negocios
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_negocios) == True:
                    self.__lvl_negocios = self.__lvl_negocios + 1
                    print("Subiu de nível em Negócios!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 4:  # Persuasao
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_persuasao) == True:
                    self.__lvl_persuasao = self.__lvl_persuasao + 1
                    print("Subiu de nível em Persuasão!")
                else:
                    raise ExcessaoNivelMaximo()
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()

#Tudo OK
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
                    raise ExcessaoNivelMaximo()

            elif opcao == 2:  # Coragem
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_coragem) == True:
                    self.__lvl_coragem = self.__lvl_coragem + 1
                    print("Subiu de nível em Coragem!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 3:  # Ensinar
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_ensinar) == True:
                    self.__lvl_ensinar = self.__lvl_ensinar + 1
                    print("Subiu de nível em Ensinar!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 4:  # Lancar Feitico
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_lancar_feitico) == True:
                    self.__lvl_lancar_feitico = self.__lvl_lancar_feitico + 1
                    print("Subiu de nível em Lançar Feitiço!")
                else:
                    raise ExcessaoNivelMaximo()
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()

#Tudo OK
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
                    raise ExcessaoNivelMaximo()

            elif opcao == 2:  # Consciencia
                self._qtd_pontos_profissao = self._qtd_pontos_profissao - 1
                if self._verifica_aumenta_lvl_habilidade(self.__lvl_consciencia) == True:
                    self.__lvl_consciencia = self.__lvl_consciencia + 1
                    print("Subiu de nível em Consciência!")
                else:
                    raise ExcessaoNivelMaximo()
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()

#Tudo OK
class Jogador(ABC):

    def __init__(self, nome="Guest", hp=0, imunidade=0, nivel_geral=0, lvl_brigar=0, lvl_apostar=0, lvl_forca=0, lvl_inteligencia=0):
        self._profissao_jogador = None #Se comporta como se fosse um ponteiro para a classe Profissao
        self._hp_maximo = 300
        self._qtd_pontos = 0  
        self.setNome(nome)
        self.setHP(hp)
        self.setNivelGeral(nivel_geral)
        self.setLvlApostar(lvl_apostar)
        self.setLvlBrigar(lvl_brigar)
        self.setLvlForca(lvl_forca)
        self.setLvlInteligencia(lvl_inteligencia)
        self.setImunidade(imunidade)

    #Métodos getters
    def getNivelGeral(self):
        return self._nivel_geral
    
    def getHp(self):
        return self._hp
    
    def getHPMax(self):
        return self._hp_maximo
    
    def getNome(self):
        return self._nome
    
    def getLvlBrigar(self):
        return self._lvl_brigar
    
    def getLvlApostar(self):
        return self._lvl_apostar
    
    def getLvlForca(self):
        return self._lvl_forca
    
    def getLvlInteligencia(self):
        return self._lvl_inteligencia
    
    def getProfissao(self):
        return self._profissao_jogador
    
    def setProfissao(self, valor):
        self._profissao_jogador = valor
        return
    
    #Só pra dps fazer uma função que mostre qts pontos o jogador tem
    def getQtdPontos(self):
        return self._qtd_pontos
    
    def getImunidade(self):
        return self._imunidade

    #Métodos setters
    def setNome(self, valor):
        if(valor.split() == ""):
            raise ExcessaoNomeJogadorInvalido()
        else:
            self._nome = valor
        return
    
    def setNivelGeral(self, valor):
        if(self._verifica_nivel_geral(valor) == True):
            self._nivel_geral = valor
        else:
            self._nivel_geral = 0

        return
    
    def setHP(self, valor):
        if(self._verifica_valor_hp(valor) == True):
            self._hp = valor
        else:
            self._hp = 0

        return
    
    def setLvlBrigar(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self._lvl_brigar = valor
        else:
            self._lvl_brigar = 0

        return
    
    def setLvlApostar(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self._lvl_apostar = valor
        else:
            self._lvl_apostar = 0

        return
    
    def setLvlForca(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self._lvl_forca = valor
        else:
            self._lvl_forca = 0

        return
    
    def setLvlInteligencia(self, valor):
        if(self._valida_atributo_construtor(valor) == True):
            self._lvl_inteligencia = valor
        else:
            self._lvl_inteligencia = 0

        return
    
    def setImunidade(self, valor):

        if(self._valida_atributo_construtor(valor) == True):
            self._imunidade = valor
        else:
            self._imunidade = 0

        return
            
    #Métodos da classe
    def _verifica_valor_hp(self, valor):

        retorno = False

        if(valor > 0 and valor < self._hp_maximo):
            retorno = True
        
        return retorno

    def _valida_atributo_construtor(self, valor):
        retorno = False

        if valor > 0:
            retorno = True

        return retorno
    
    def _verifica_nivel_geral(self, valor):

        retorno = False

        if(valor > 0):
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

        self._transforma_pontos_experiencia()

        console = Console()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Aposta \n"
                    "2 - Upar Habilidade de: Brigar \n"
                    "3 - Upar Habilidade de: Forca \n"
                    "4 - Upar Habilidade de: Inteligencia \n"
                    "5 - Não Upar Habilidade Básica"
                ),title="❇ Subir de LVL: Habilidades Básicas ❇"))
                
                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()
            
                if opcao >= 1 and opcao <= 5:
                    break
                else:
                    raise ExcessaoTipoOpcaoInvalido()

            if opcao == 1:  # Aposta
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_apostar) == True:
                    self._lvl_apostar = self._lvl_apostar + 1
                    print(self._nome + " Subiu de nível em Aposta!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 2:  # Brigar
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_brigar) == True:
                    self._lvl_brigar = self._lvl_brigar + 1
                    print(self._nome + " Subiu de nível em Brigar!")
                else:
                    raise ExcessaoNivelMaximo()
            
            elif opcao == 3:  # Forca
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_forca) == True:
                    self._lvl_forca = self._lvl_forca + 1
                    print(self._nome + " Subiu de nível em Força!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 4:  # Inteligencia
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_inteligencia) == True:
                    self._lvl_inteligencia = self._lvl_inteligencia + 1
                    print(self._nome + " Subiu de nível em Inteligência!")
                else:
                    raise ExcessaoNivelMaximo()
            elif opcao == 5:  # Não upar habilidade basica
                pass
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()
        
        return

    @abstractmethod
    def inicializa_jogador(self):
        pass

    def __del__(self):
        print("Removendo os dados do jogador: " + self._nome)

#Tudo OK
class Humano(Jogador):

    def __init__(self, nome="Guest", hp=100, nivel_geral=0, imunidade=5, lvl_brigar=0, lvl_apostar=0, lvl_forca=0, lvl_inteligencia=0, lvl_seducao=0, lvl_persuasao=0, lvl_teimosia=0):
        super().__init__(nome, hp, imunidade, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_inteligencia)
        self.setLvlSeducao(lvl_seducao)
        self.setLvlPersuasao(lvl_persuasao)
        self.setLvlTeimosia(lvl_teimosia)

    #Métodos getters
    def getLvlSeducao(self):
        return self.__lvl_seducao
    
    def getLvlPersuasao(self):
        return self.__lvl_persuasao
    
    def getLvlTeimosia(self):
        return self.__lvl_teimosia

    #Métodos setters
    def setLvlSeducao(self, valor):
        
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_seducao = valor
        else:
            self.__lvl_seducao = 0

        return

    def setLvlPersuasao(self, valor):
        
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_persuasao = valor
        else:
            self.__lvl_persuasao = 0

        return

    def setLvlTeimosia(self, valor):
        
        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_teimosia = valor
        else:
            self.__lvl_teimosia = 0

        return

    #Métodos da classe
    def inicializa_jogador(self):
        return

    def aumenta_nivel_habilidade(self):
        
        super().aumenta_nivel_habilidade()

        console = Console()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:

                console.print(Panel(Align.center(
                    "6 - Upar Habilidade de: Sedução \n"
                    "7 - Upar Habilidade de: Persuasão \n"
                    "8 - Upar Habilidade de: Teimosia \n"
                    "9 - Não Upar Habilidade Específica"
                ),title="❇ Subir de LVL: Habilidades Específicas ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 6 and opcao <= 9:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 6:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_seducao) == True:
                    self.__lvl_seducao = self.__lvl_seducao + 1
                    print(self._nome + " Subiu de nível em Sedução!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_persuasao) == True:
                    self.__lvl_persuasao = self.__lvl_persuasao + 1
                    print(self._nome + " Subiu de nível em Persuasão!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 8:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_teimosia) == True:
                    self.__lvl_teimosia = self.__lvl_teimosia + 1
                    print(self._nome + " Subiu de nível em Teimosia!")
                else:
                    raise ExcessaoNivelMaximo()
            elif opcao == 9:
                pass
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()
        
        return

#Tudo OK
class Bruxo(Jogador):

    def __init__(self, nome="Guest", hp=100, nivel_geral=0, imunidade = 13, lvl_brigar=0, lvl_apostar=0, lvl_forca=0, lvl_inteligencia=0, lvl_reflexos_relampagos=0):
        super().__init__(nome, hp, imunidade, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_inteligencia)
        self.__lvl_carisma = 0  # private - de acordo com o livro, bruxos tem carisma 0 nn tem como aumentar/diminuir
        self.setLvlReflexosRelampagos(lvl_reflexos_relampagos)

    #Métodos getters 
    def getCarisma(self):
        return self.__lvl_carisma
    
    def getLvlReflexos(self):
        return self.__lvl_reflexos_relampagos

    #Métodos setters
    def setLvlReflexosRelampagos(self, valor):

        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_reflexos_relampagos = valor
        else:
            self.__lvl_reflexos_relampagos = 0

        return

    #Métodos da classe
    def inicializa_jogador(self):
        return

    def aumenta_nivel_habilidade(self):
        
        super().aumenta_nivel_habilidade()

        console = Console()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:

                console.print(Panel(Align.center(
                    "6 - Upar Habilidade de: Reflexos Relâmpagos \n"
                    "7 - Não Upar Habilidade Específica"
                ),title="❇ Subir de LVL: Habilidades Específicas ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao == 6 or opcao == 7:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 6:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_reflexos_relampagos) == True:
                    self.__lvl_reflexos_relampagos = self.__lvl_reflexos_relampagos + 1
                    print(self._nome + " Subiu de nível em Reflexos Relâmpagos!")
                else:
                    raise ExcessaoNivelMaximo()
            elif opcao == 7:
                pass
                
        else:
            ExcessaoPontosInsuficientesSubirNivel()

#Tudo OK
class Anao(Jogador):

    def __init__(self, nome="Guest", hp=100, nivel_geral=0, imunidade=7, lvl_brigar=0, lvl_apostar=0, lvl_forca=0, lvl_inteligencia=0, lvl_armadura=0, lvl_deducao=0):
        super().__init__(nome, hp, imunidade, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_inteligencia)
        self.setLvlArmadura(lvl_armadura)
        self.setLvlDeducao(lvl_deducao)

    #Métodos getters    
    def getLvlArmadura(self):
        return self.__lvl_armadura
    
    def getLvlDeducao(self):
        return self.__lvl_deducao

    #Métodos setters  
    def setLvlArmadura(self, valor):

        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_armadura = valor
        else:
            self.__lvl_armadura = 0
        
        return
    
    def setLvlDeducao(self, valor):

        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_deducao = valor
        else:
            self.__lvl_deducao = 0

        return

    #Métodos da classe
    def inicializa_jogador(self):
        return

    def aumenta_nivel_habilidade(self):
        
        super().aumenta_nivel_habilidade()

        console = Console()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:
                console.print(Panel(Align.center(
                    "6 - Upar Habilidade de: Armaduras \n"
                    "7 - Upar Habilidade de: Dedução \n"
                    "8 - Não Upar Habilidade Específica"
                ),title="❇ Subir de LVL: Habilidades Específicas ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 6 and opcao <= 8:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 6:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_armadura) == True:
                    self.__lvl_armadura = self.__lvl_armadura + 1
                    print(self._nome + " Subiu de nível em Armadura!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_deducao) == True:
                    self.__lvl_deducao = self.__lvl_deducao + 1
                    print(self._nome + " Subiu de nível em Dedução!")
                else:
                    raise ExcessaoNivelMaximo()
            elif opcao == 8:
                pass
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()
        return

#Tudo OK
class Elfo(Jogador):

    def __init__(self, nome="Guest", hp=100, nivel_geral=0, lvl_brigar=0, lvl_apostar=0, lvl_forca=0, lvl_inteligencia=0, imunidade=8, lvl_artesanato=0, lvl_arcos=0, lvl_sintonia_natureza=0):
        super().__init__(nome, hp, imunidade, nivel_geral, lvl_brigar, lvl_apostar, lvl_forca, lvl_inteligencia)
        self.setLvlSintoniaNatureza(lvl_sintonia_natureza)
        self.setLvlArcos(lvl_arcos)
        self.setLvlArtesanato(lvl_artesanato)

    #Métodos getters   
    def getLvlArtesanato(self):
        return self.__lvl_artesanato
    
    def getLvlArcos(self):
        return self.__lvl_arcos
    
    def getLvlSintoniaNatureza(self):
        return self.__lvl_sintonia_natureza

    #Métodos setters   
    def setLvlArcos(self, valor):

        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_arcos = valor
        else:
            self.__lvl_arcos = 0

        return
    
    def setLvlSintoniaNatureza(self, valor):

        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_sintonia_natureza = valor
        else:
            self.__lvl_sintonia_natureza = 0

        return
    
    def setLvlArtesanato(self, valor):

        if(self._valida_atributo_construtor(valor) == True):
            self.__lvl_artesanato = valor
        else:
            self.__lvl_artesanato = 0

        return        

    #Métodos da Classe
    def inicializa_jogador(self):
        return

    def aumenta_nivel_habilidade(self):
        super().aumenta_nivel_habilidade()

        console = Console()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:
                console.print(Panel(Align.center(
                    "6 - Upar Habilidade de: Artesanato \n"
                    "7 - Upar Habilidade de: Artilharia de Arcos \n"
                    "8 - Upar Habilidade de: Sintonia da Natureza \n"
                    "9 - Não Upar Habilidade Específica"
                ),title="❇ Subir de LVL: Habilidades Específicas ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()
                

                if opcao >= 6 and opcao <= 9:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 6:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_artesanato) == True:
                    self.__lvl_artesanato = self.__lvl_artesanato + 1
                    print(self._nome + " Subiu de nível em Artesanato!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_arcos) == True:
                    self.__lvl_arcos = self.__lvl_arcos + 1
                    print(self._nome + " Subiu de nível em Artilharia de Arcos!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 8:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_sintonia_natureza) == True:
                    self.__lvl_sintonia_natureza = self.__lvl_sintonia_natureza + 1
                    print(self._nome + " Subiu de nível em Sintonia da Natureza!")
                else:
                    raise ExcessaoNivelMaximo()
            elif opcao == 9:
                pass
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()
        return

class ExcessaoNivelInvalido(Exception):

    def __str__(self):
        return f"Valor de nível Inválido, Mínimo 0 e Máximo 13!"

#Dependendo do tipo de personagem, ele entra na função e pede os parâmetros necessários para a criação naquele jogador
#Tudo OK
def recebeParametrosJogador(tipo):

    console = Console()

    lista_strings = [
        ("Digite o nome do personagem: ", str, None, None),
        ("Digite o hp do personagem: ", int, 0, 300),
        ("Digite o nível geral do personagem: ", int, 0, 200),
        ("Digite o nível de briga do personagem: ", int, 0, 13),
        ("Digite o nível de apostar do personagem: ", int, 0, 13),
        ("Digite o nível de força do personagem: ", int, 0, 13),
        ("Digite o nível de inteligência do personagem: ", int, 0, 13)
    ]

    lista_strings_humano = [
        ("Digite o nível de Sedução do personagem: ", int, 0, 13),
        ("Digite o nível de Persuasão do personagem: ", int, 0, 13),
        ("Digite o nível de Teimosia do personagem: ", int, 0, 13)
    ]

    lista_strings_bruxo = [
        ("Digite o nível de Reflexos Relâmpagos do personagem: ", int, 0, 13)
    ]

    lista_strings_anao = [
        ("Digite o nível de Armadura do persoagem: ", int, 0, 13),
        ("Digite o nível de Dedução do personagem: ", int, 0, 13)
    ]

    lista_strings_elfo = [
        ("Digite o nível de Artesanato do personagem: ", int, 0, 13),
        ("Digite o nível em Arcos do personagem: ", int, 0, 13),
        ("Digite o nível em Sintonia da Natureza do personagem: ", int, 0, 13)
    ]

    #Aqui vai ficar guardado todas as variáveis e elas vão ser retornadas para a classe Factory para poder criar um personagem naquele tipo
    lista_parametros_tipo = []
    
    for mensagem, tipo_var, minimo, maximo in lista_strings:

        console.print(Panel(Align.center(mensagem)))

        if tipo_var == str:
            valor = input("")
        else:
            while True:
                try:
                    valor = int(input(""))

                    if minimo <= valor <= maximo:
                        break
                    else:
                        print(f"Digite um valor entre {minimo} e {maximo}")
                        console.print(Panel(Align.center(mensagem)))
                except ValueError:
                    print("Digite apenas números!")

        lista_parametros_tipo.append(valor)
    
    #Parâmetros específicos
    match tipo:
        case 1: #Humano
            for mensagem, tipo_var, minimo, maximo in lista_strings_humano:

                console.print(Panel(Align.center(mensagem)))
            
                if tipo_var == str:
                    valor = input("")
                else:
                    while True:
                        try:
                            valor = int(input(""))

                            if minimo <= valor <= maximo:
                                break
                            else:
                                print(f"Digite um valor entre {minimo} e {maximo}")
                                console.print(Panel(Align.center(mensagem)))
                        except ValueError:
                            print("Digite apenas números!")

                lista_parametros_tipo.append(valor)
        case 2: #Bruxo
            for mensagem, tipo_var, minimo, maximo in lista_strings_bruxo:

                console.print(Panel(Align.center(mensagem)))

                if tipo_var == str:
                    valor = input("")
                else:
                    while True:
                        try:
                            valor = int(input(""))

                            if minimo <= valor <= maximo:
                                break
                            else:
                                print(f"Digite um valor entre {minimo} e {maximo}")
                                console.print(Panel(Align.center(mensagem)))
                        except ValueError:
                            print("Digite apenas números!")

                lista_parametros_tipo.append(valor)
        case 3: #Anão
            for mensagem, tipo_var, minimo, maximo in lista_strings_anao:

                console.print(Panel(Align.center(mensagem)))

                if tipo_var == str:
                    valor = input("")
                else:
                    while True:
                        try:
                            valor = int(input(""))

                            if minimo <= valor <= maximo:
                                break
                            else:
                                print(f"Digite um valor entre {minimo} e {maximo}")
                                console.print(Panel(Align.center(mensagem)))
                        except ValueError:
                            print("Digite apenas números!")

                lista_parametros_tipo.append(valor)
        case 4: #Elfo
            for mensagem, tipo_var, minimo, maximo in lista_strings_elfo:

                console.print(Panel(Align.center(mensagem)))

                if tipo_var == str:
                    valor = input("")
                else:
                    while True:
                        try:
                            valor = int(input(""))

                            if minimo <= valor <= maximo:
                                break
                            else:
                                print(f"Digite um valor entre {minimo} e {maximo}")
                                console.print(Panel(Align.center(mensagem)))
                        except ValueError:
                            print("Digite apenas números!")

                lista_parametros_tipo.append(valor)


    return lista_parametros_tipo

#O jogador pode começar com níveis, menos em profissão, profissão ele começa apenas com o lvl geral de profissao
#Tudo OK
class JogadorFactory:

    @staticmethod
    def criar_jogador(tipo):

        jogador = None

        lista_params = recebeParametrosJogador(tipo)
        
        match tipo:
            case 1: #Humano
                imunidade = 5
                jogador = Humano(lista_params[0], lista_params[1], lista_params[2], imunidade, lista_params[3], lista_params[4], lista_params[5], lista_params[6], lista_params[7], lista_params[8], lista_params[9])
            case 2: #Bruxo
                imunidade = 13
                jogador = Bruxo(lista_params[0], lista_params[1], lista_params[2], imunidade,lista_params[3], lista_params[4], lista_params[5], lista_params[6], lista_params[7])
            case 3: #Anão
                imunidade = 7
                jogador = Anao(lista_params[0], lista_params[1], lista_params[2], imunidade, lista_params[3], lista_params[4], lista_params[5], lista_params[6], lista_params[7], lista_params[8])
            case 4: #Elfo
                imunidade = 8
                jogador = Elfo(lista_params[0], lista_params[1], lista_params[2], imunidade, lista_params[3], lista_params[4], lista_params[5], lista_params[6], lista_params[7], lista_params[8], lista_params[9])

        return jogador
    
#Tudo OK
def recebeParametrosProfissao():

    console.print(
        Panel(
            Align.center(
                "Digite o valor de nível geral de profissão: "
            ),title= "Experiência Profissional"))   #Decorar isso aqui dps
    try:
        nivel_geral = int(input(""))  
    except ValueError:
        print("Digite apenas números inteiros!")

    return nivel_geral
    
#Tudo OK
class ProfissaoFactory:

    @staticmethod
    def criar_profissao(tipo):

        profissao = None

        nivel_geral = recebeParametrosProfissao()

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

#Tudo OK
def menu_jogador():

    console = Console()

    while True:

        console.print(
            Panel(
                Align.center(
                    "◉ 1 - Humano \n"
                    "✡ 2 - Bruxo \n"
                    "⛏ 3 - Anão \n"
                    "❀ 4 - Elfo"
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

#Tudo OK
def menu_profissao():

    console = Console()

    while True:

        console.print(
            Panel(
                Align.center(
                    "✧ 1 - Mago \n"
                    "🛡 2 - Bardo \n"
                    "❀ 3 - Artesão \n"
                    "☠ 4 - Criminoso \n"
                    "☤ 5 - Doutor \n"
                    "⚔ 6 - Cavaleiro \n"
                    "❈ 7 - Comerciante \n"
                    "⌘ 8 - Sacerdote \n"
                    "◈ 9 - Desempregado"
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

#O Personagem tem a capacidade de combater monstros
class ICombate():
    pass

#O Personagem tem a capacidade de se curar
class ICuravel():
    pass

#O personagem tem a capacidade de ficar doente
#Acho que não vai dar tempo de implementar isso
class IDoente():
    pass

#Decorar isso aqui dps (melhorar visualmente via terminal)
def inicializaJogo():
    # -> Como se fosse um gerenciador do jogo

    personagem_criado = False

    verifica_saida = False

    #Distrinchar isso em menu e em partes que vão chamar outras para funcionar
    while verifica_saida == False:

        while True:
            #Decorar isso aqui dps
            if(personagem_criado == False):
                print("0 - Sair do Jogo") #Mudar o valor dessa opção aqui
                print("1 - Criar Personagem")
            else:
                print("0 - Sair do Jogo") #Mudar o valor dessa opção aqui
                #No momento criar personagem só reescreve o existente
                #print("1 - Criar Personagem") #Ver se seria melhor criar apenas 1 ou mais personagens
                print("2 - Upar Skills de Jogador")
                print("3 - Upar Skills de Profissao")

            try:
                op = int(input("Digite sua opção: "))
            except ValueError:
                print("Digite apenas um valor inteiro!")

            if((personagem_criado == False) and op >=0 and op <= 1):
                break
            elif((personagem_criado == True) and op >=0 and op <= 3):
                break
            else:
                print("Digite uma opção válida!")

        match op:

            case 0:
                verifica_saida = True
            case 1:

                personagem_criado = True

                opcao_jogador = menu_jogador()
                #Criando o objeto jogador em si
                obj_jogador = JogadorFactory.criar_jogador(opcao_jogador)

                opcao_profissao = menu_profissao()
                #Criando a profissao do jogador
                profissao_jogador = ProfissaoFactory.criar_profissao(opcao_profissao)
                obj_jogador.setProfissao(profissao_jogador)

                print("\nPersonagem criado com sucesso!")
                print("Nome:", obj_jogador.getNome())
                print("Raça:", type(obj_jogador).__name__) 
                print("Profissão:", obj_jogador.getProfissao()) 
            case 2: 
                obj_jogador.aumenta_nivel_habilidade()
            case 3:
                obj_jogador.getProfissao().aumenta_nivel_habilidade_profissao()
                
            case 4:
                pass

    return

if __name__ == "__main__":
    
    try:
        
        console = Console()

        fonte = Figlet(font="starwars")

        print(fonte.renderText("RPG"))
        print(fonte.renderText("The Witcher"))

        inicializaJogo()

    except Exception as e:
        print(e)

    
