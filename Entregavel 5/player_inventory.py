#O método Fabric vai permitir q a gnt tenha um menu de criação de jogador e profissão
# Não esquecer dps de fazer um gerenciador com interface pra fazer as tasks e tbm vai precisar de um Singleton :/ (-A)

#Fazer uma função para tocar música com o Pyfiglet

#Entregável em Python Feito por Arieli (-A)

#Nas profissões mandar o atributo verificador de atributo antes de fazer a igualação(esqueci o nome)

from abc import ABC, abstractmethod
from pyfiglet import Figlet
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

# =------ Excessões ------=

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
        return f"Digite uma opcao válida!"

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
                        )),title="❇ Subir de LVL: Skill Profissão ❇")
                
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
#fazer os getters e setters daqui tbbm

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

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Etiqueta Social \n"
                    "2 - Upar Habilidade de: Ludibriar \n"
                    "3 - Upar Habilidade de: Sabedoria das Ruas"
                )),title="❇ Subir de LVL: Skill Profissão ❇")

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

#fazer os getters e setters daqui tbbm
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

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Educação \n"
                    "2 - Upar Habilidade de: Criação \n"
                    "3 - Upar Habilidade de: Negociação \n"
                    "4 - Upar Habilidade de: Físico"
                )),title="❇ Subir de LVL: Skill Profissão ❇")

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

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:

                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Arrombar Fechadura \n"
                    "2 - Upar Habilidade de: Falsificacao \n"
                    "3 - Upar Habilidade de: Atletismo \n"
                    "4 - Upar Habilidade de: Sabedoria das Ruas"
                )),title="❇ Subir de LVL: Skill Profissão ❇")

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

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True: 
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Educação \n"
                    "2 - Upar Habilidade de: Coragem \n"
                    "3 - Upar Habilidade de: Alquimia \n"
                    "4 - Upar Habilidade de: Carisma"
                )),title="❇ Subir de LVL: Skill Profissão ❇")

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

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Coragem \n"
                    "2 - Upar Habilidade de: Intimidação \n"
                    "3 - Upar Habilidade de: Sobrevivência \n"
                    "4 - Upar Habilidade de: Esquivar"
                )),title="❇ Subir de LVL: Skill Profissão ❇")

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

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Carisma \n"
                    "2 - Upar Habilidade de: Educação \n"
                    "3 - Upar Habilidade de: Negócios \n"
                    "4 - Upar Habilidade de: Persuasão"
                )),title="❇ Subir de LVL: Skill Profissão ❇")

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

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True: 
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Criar Ritual \n"
                    "2 - Upar Habilidade de: Coragem \n"
                    "3 - Upar Habilidade de: Ensinar \n"
                    "4 - Upar Habilidade de:  Lançar Feitiço"
                )),title="❇ Subir de LVL: Skill Profissão ❇")

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

        console = Console()

        opcao = 0

        if self._qtd_pontos_profissao > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Sobrevivência \n"
                    "2 - Upar Habilidade de: Consciência \n"
                    "3 - Upar Habilidade de: Ensinar \n"
                    "4 - Upar Habilidade de:  Lancar Feitiço"
                )),title="❇ Subir de LVL: Skill Profissão ❇")

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

        self._transforma_pontos_experiencia()

        console = Console()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:
                console.print(Panel(Align.center(
                    "1 - Upar Habilidade de: Aposta \n"
                    "2 - Upar Habilidade de: Brigar \n"
                    "3 - Upar Habilidade de: Coragem \n"
                    "4 - Upar Habilidade de: Forca \n"
                    "5 - Upar Habilidade de: Inteligencia \n"
                    "6 - Não Upar Habilidade Básica"
                ),title="❇ Subir de LVL: Habilidades Básicas ❇"))
                
                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()
            
                if opcao >= 1 and opcao <= 6:
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

            elif opcao == 3:  # Coragem
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_coragem) == True:
                    self._lvl_coragem = self._lvl_coragem + 1
                    print(self._nome + " Subiu de nível em Coragem!")
                else:
                    raise ExcessaoNivelMaximo()
            
            elif opcao == 4:  # Forca
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_forca) == True:
                    self._lvl_forca = self._lvl_forca + 1
                    print(self._nome + " Subiu de nível em Força!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 5:  # Inteligencia
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_inteligencia) == True:
                    self._lvl_inteligencia = self._lvl_inteligencia + 1
                    print(self._nome + " Subiu de nível em Inteligência!")
                else:
                    raise ExcessaoNivelMaximo()
            elif opcao == 6:  # Não upar habilidade basica
                pass
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()
        
        return

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

        console = Console()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:

                console.print(Panel(Align.center(
                    "7 - Upar Habilidade de: Sedução \n"
                    "8 - Upar Habilidade de: Persuasão \n"
                    "9 - Upar Habilidade de: Teimosia \n"
                    "10 - Não Upar Habilidade Específica"
                ),title="❇ Subir de LVL: Habilidades Específicas ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 7 and opcao <= 10:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_seducao) == True:
                    self.__lvl_seducao = self.__lvl_seducao + 1
                    print(self._nome + " Subiu de nível em Sedução!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 8:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_persuasao) == True:
                    self.__lvl_persuasao = self.__lvl_persuasao + 1
                    print(self._nome + " Subiu de nível em Persuasão!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 9:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_teimosia) == True:
                    self.__lvl_teimosia = self.__lvl_teimosia + 1
                    print(self._nome + " Subiu de nível em Teimosia!")
                else:
                    raise ExcessaoNivelMaximo()
            elif opcao == 10:
                pass
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()
        
        return

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

        console = Console()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:

                console.print(Panel(Align.center(
                    "7 - Upar Habilidade de: Reflexos Relâmpagos \n"
                    "8 - Não Upar Habilidade Específica"
                ),title="❇ Subir de LVL: Habilidades Específicas ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 7 and opcao <= 8:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_reflexos_relampagos) == True:
                    self.__lvl_reflexos_relampagos = self.__lvl_reflexos_relampagos + 1
                    print(self._nome + " Subiu de nível em Reflexos Relâmpagos!")
                else:
                    raise ExcessaoNivelMaximo()
            elif opcao == 8:
                pass
                
        else:
            ExcessaoPontosInsuficientesSubirNivel()

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

        console = Console()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:
                console.print(Panel(Align.center(
                    "7 - Upar Habilidade de: Armaduras \n"
                    "8 - Upar Habilidade de: Dedução \n"
                    "9 - Não Upar Habilidade Específica"
                ),title="❇ Subir de LVL: Habilidades Específicas ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()

                if opcao >= 7 and opcao <= 9:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_armadura) == True:
                    self.__lvl_armadura = self.__lvl_armadura + 1
                    print(self._nome + " Subiu de nível em Armadura!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 8:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_deducao) == True:
                    self.__lvl_deducao = self.__lvl_deducao + 1
                    print(self._nome + " Subiu de nível em Dedução!")
                else:
                    raise ExcessaoNivelMaximo()
            elif opcao == 9:
                pass
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()
        return

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

        console = Console()

        opcao = 0

        if self._qtd_pontos > 0:

            while True:
                console.print(Panel(Align.center(
                    "7 - Upar Habilidade de: Artesanato \n"
                    "8 - Upar Habilidade de: Artilharia de Arcos \n"
                    "9 - Upar Habilidade de: Sintonia da Natureza \n"
                    "10 - Não Upar Habilidade Específica"
                ),title="❇ Subir de LVL: Habilidades Específicas ❇"))

                try:
                    opcao = int(input("Digite uma opção: "))
                except ValueError:
                    raise ExcessaoTipoOpcaoInvalido()
                

                if opcao >= 7 and opcao <= 10:
                    break
                else:
                    raise ExcessaoOpcaoInvalida()

            if opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_artesanato) == True:
                    self.__lvl_artesanato = self.__lvl_artesanato + 1
                    print(self._nome + " Subiu de nível em Artesanato!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 8:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_arcos) == True:
                    self.__lvl_arcos = self.__lvl_arcos + 1
                    print(self._nome + " Subiu de nível em Artilharia de Arcos!")
                else:
                    raise ExcessaoNivelMaximo()

            elif opcao == 9:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_sintonia_natureza) == True:
                    self.__lvl_sintonia_natureza = self.__lvl_sintonia_natureza + 1
                    print(self._nome + " Subiu de nível em Sintonia da Natureza!")
                else:
                    raise ExcessaoNivelMaximo()
            elif opcao == 10:
                pass
        else:
            raise ExcessaoPontosInsuficientesSubirNivel()
        return

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

    jogador = JogadorFactory.criar_jogador(opcao_jogador,nome,100,200,0,0,0,0,0)
    opcao_profissao = menu_profissao()

    profissao = ProfissaoFactory.criar_profissao(opcao_profissao)

    jogador._profissao_jogador = profissao

    jogador.aumenta_nivel_habilidade()

    print("\nPersonagem criado com sucesso!")
    print("Nome:", jogador._nome)
    print("Raça:", type(jogador).__name__) #trocar isso dps por um getter plmds -A
    print("Profissão:", type(jogador._profissao_jogador).__name__) #trocar isso dps por um getter plmds -A
