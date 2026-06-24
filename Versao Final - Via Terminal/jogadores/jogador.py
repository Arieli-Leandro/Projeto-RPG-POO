from exceptions.excessoes import *
from interfaces.interface import *
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

class Jogador(ICombate, ICuravel):

    def __init__(self, nome="Guest", hp=0, imunidade=0, nivel_geral=0, lvl_brigar=0, lvl_apostar=0, lvl_forca=0, lvl_inteligencia=0):
        self._profissao_jogador = None 
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
    
    def getNomeRaca(self):
        return self.__class__.__name__
    
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
        if(valor.strip() == ""):
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

        if(valor > 0 and valor <= self._hp_maximo):
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
                    "5 - Não Upar Habilidade Básica\\Ir para Habilidades Específicas"
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
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 2:  # Brigar
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_brigar) == True:
                    self._lvl_brigar = self._lvl_brigar + 1
                    print(self._nome + " Subiu de nível em Brigar!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
            
            elif opcao == 3:  # Forca
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_forca) == True:
                    self._lvl_forca = self._lvl_forca + 1
                    print(self._nome + " Subiu de nível em Força!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 4:  # Inteligencia
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self._lvl_inteligencia) == True:
                    self._lvl_inteligencia = self._lvl_inteligencia + 1
                    print(self._nome + " Subiu de nível em Inteligência!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
            elif opcao == 5:  # Não upar habilidade basica
                pass
        else:
            print("Seu personagem não tem pontos suficientes para subir de nível!")
        
        return

    #Implementação da interface ICombate
    def atacar(self, monstro):

        if(self.getHp() > 0):

            console = Console()

            dano = self._lvl_forca + self._lvl_brigar
            dano_recebido = 0.5 * monstro.getXpRecompensa()

            if dano <= 0:
                dano = 1

            monstro.recebeDano(dano)

            #fazendo o personagem receber o dano
            valor_vida = self.getHp() - dano_recebido
            self.setHP(valor_vida)

            console.print(Panel(Align.center(
                f"{self._nome} atacou {monstro.getNome()} e causou {dano} de dano!\n"
                f"{monstro.getNome()} atacou {self._nome} e causou {dano_recebido} de dano!\n"
                f"{monstro.getNome()} possui {monstro.getHp()} de HP restante."
            ), title="⚔ Combate ⚔"))

            if monstro.estaMorto():

                xp_ganho = monstro.getXpRecompensa()

                #Atribuição do xp que foi ganhado no nivel_geral de Jogador
                self.setNivelGeral(self._nivel_geral + xp_ganho)

                #Atribuição do xp que foi ganhado no nivel_geral de Profissao
                if self._profissao_jogador is not None:
                    self._profissao_jogador.setNivelGeral(self._profissao_jogador.getNivelGeral() + xp_ganho)

                console.print(Panel(Align.center(
                    f"{monstro.getNome()} foi derrotado!\n"
                    f"{self._nome} ganhou {xp_ganho} pontos de experiência!"
                ), title="✦ Vitória ✦"))
        else:
            pass #Antes era um raise, mas ele impedia do jogo continuar em loop

        return

    #Implementação da interface ICuravel
    def curar(self):

        console = Console()

        self.setHP(self._hp_maximo)

        console.print(Panel(Align.center(
            f"{self._nome} foi totalmente curado!\n"
            f"HP: {self._hp}/{self._hp_maximo}"
        ), title="✚ Cura ✚"))

        return

    @abstractmethod
    def inicializa_jogador(self):
        pass

    def __del__(self):
        print("")

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
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_persuasao) == True:
                    self.__lvl_persuasao = self.__lvl_persuasao + 1
                    print(self._nome + " Subiu de nível em Persuasão!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 8:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_teimosia) == True:
                    self.__lvl_teimosia = self.__lvl_teimosia + 1
                    print(self._nome + " Subiu de nível em Teimosia!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
            elif opcao == 9:
                pass
        
        return

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
                    print("Seu personagem já está com essa skill no nível Máximo!")
            elif opcao == 7:
                pass

        return

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
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_deducao) == True:
                    self.__lvl_deducao = self.__lvl_deducao + 1
                    print(self._nome + " Subiu de nível em Dedução!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
            elif opcao == 8:
                pass

        return

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
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 7:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_arcos) == True:
                    self.__lvl_arcos = self.__lvl_arcos + 1
                    print(self._nome + " Subiu de nível em Artilharia de Arcos!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")

            elif opcao == 8:
                self._qtd_pontos = self._qtd_pontos - 1
                if self.verifica_aumenta_lvl_habilidade(self.__lvl_sintonia_natureza) == True:
                    self.__lvl_sintonia_natureza = self.__lvl_sintonia_natureza + 1
                    print(self._nome + " Subiu de nível em Sintonia da Natureza!")
                else:
                    print("Seu personagem já está com essa skill no nível Máximo!")
                    
            elif opcao == 9:
                pass

        return

