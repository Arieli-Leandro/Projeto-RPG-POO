from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import random
from jogadores.jogador import *
from profissoes.profissoes import *
from monstros.monstro import *

class MonstroFactory:

    @staticmethod
    def criar_monstro_aleatorio():

        lista_monstros = [
            ("Afogador", 15, 20),
            ("Necrófago", 18, 25),
            ("Carniçal", 20, 30),
            ("Endriaga", 25, 35),
            ("Alghoul", 30, 40),
            ("Grifo", 45, 60),
            ("Lobisomem", 40, 55),
            ("Ekimmara", 50, 70),
            ("Foglet", 35, 50),
            ("Leshen", 80, 120),
            ("Basilisco", 70, 100),
            ("Wyvern", 60, 85),
            ("Aracnomorfo", 40, 60),
            ("Doppler Corrompido", 55, 80),
            ("Fiend", 90, 130)
        ]

        nome, hp, xp = random.choice(lista_monstros)

        return Monstro(nome, hp, xp)

#Dependendo do tipo de personagem, ele entra na função e pede os parâmetros necessários para a criação naquele jogador
def recebeParametrosJogador(tipo):

    console = Console()

    lista_strings = [
        ("Digite o nome do personagem: ", str, None, None),
        ("Digite o hp do personagem: 0-300", int, 0, 300),
        ("Digite o nível geral do personagem: 0-200", int, 0, 200),
        ("Digite o nível de briga do personagem: 0-13", int, 0, 13),
        ("Digite o nível de apostar do personagem: 0-13", int, 0, 13),
        ("Digite o nível de força do personagem: 0-13", int, 0, 13),
        ("Digite o nível de inteligência do personagem: 0-13", int, 0, 13)
    ]

    lista_strings_humano = [
        ("Digite o nível de Sedução do personagem: 0-13", int, 0, 13),
        ("Digite o nível de Persuasão do personagem: 0-13", int, 0, 13),
        ("Digite o nível de Teimosia do personagem: 0-13", int, 0, 13)
    ]

    lista_strings_bruxo = [
        ("Digite o nível de Reflexos Relâmpagos do personagem: 0-13", int, 0, 13)
    ]

    lista_strings_anao = [
        ("Digite o nível de Armadura do persoagem: 0-13", int, 0, 13),
        ("Digite o nível de Dedução do personagem: 0-13", int, 0, 13)
    ]

    lista_strings_elfo = [
        ("Digite o nível de Artesanato do personagem: 0-13", int, 0, 13),
        ("Digite o nível em Arcos do personagem: 0-13", int, 0, 13),
        ("Digite o nível em Sintonia da Natureza do personagem: 0-13", int, 0, 13)
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
    
def recebeParametrosProfissao():

    console = Console()

    console.print(Panel(Align.center("Digite o valor de nível geral de profissão: 0-200")))
    
    while True:
        try:
            nivel_geral = int(input(""))  
        except ValueError:
            print("Digite apenas números inteiros!")

        if(nivel_geral >= 0 and nivel_geral <= 200):
            break
        else:
            console.print(Panel(Align.center("Digite o valor de nível geral de profissão: 0-200")))

    return nivel_geral
    
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