from exceptions.excessoes import *
from audio.musicas import *
from factories.factory import *
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import time
import pygame

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
            raise ExcessaoTipoOpcaoInvalido()

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



# -> Como se fosse um gerenciador do jogo
def inicializaJogo():

    console = Console()

    personagem_criado = False

    verifica_saida = False

    while verifica_saida == False:

        #Inicializa a música principal
        inicializaMusicaPrincipal()

        while True:

            if(personagem_criado == False):

                console.print(Panel(Align.center(
                    "1 - Criar Personagem \n"
                    "2 - Sair do Jogo"
                )))
            else:

                console.print(Panel(Align.center(
                    "2 - Sair do Jogo \n"
                    "3 - Upar Skills de Jogador \n"
                    "4 - Upar Skills de Profissão \n"
                    "5 - Atacar Monstro \n"
                    "6 - Curar Personagem \n"
                    "7 - Verificar Status do Personagem"

                )))

            try:
                op = int(input("Digite sua opção: "))
            except ValueError:
                print("Digite apenas um valor inteiro!")

            if((personagem_criado == False) and op >= 1 and op <= 2):
                break
            elif((personagem_criado == True) and op >=2 and op <= 7):
                break
            else:
                print("Digite uma opção válida!")

        match op:

            case 1:
                personagem_criado = True

                opcao_jogador = menu_jogador()
                #Criando o objeto jogador em si
                obj_jogador = JogadorFactory.criar_jogador(opcao_jogador)

                opcao_profissao = menu_profissao()
                #Criando a profissao do jogador
                profissao_jogador = ProfissaoFactory.criar_profissao(opcao_profissao)
                obj_jogador.setProfissao(profissao_jogador)

            case 2: 
                verifica_saida = True

                #Pra fazer uma transição mais suave em vez de só encerrar a música
                pygame.mixer.music.fadeout(2000)
            case 3:
                pygame.mixer.music.stop()
                inicializaMusicaUparSkills()

                obj_jogador.aumenta_nivel_habilidade()
            case 4:
                pygame.mixer.music.stop()
                inicializaMusicaUparSkills()

                obj_jogador.getProfissao().aumenta_nivel_habilidade_profissao()
            case 5:
                if(obj_jogador.getHp() > 0):
                    #Inicializa a música da batalha
                    pygame.mixer.music.stop()
                    inicializaMusicaBatalha()

                #Fazendo uma pausa só pra dar tempo da música de batalha tocar
                time.sleep(20)

                monstro = MonstroFactory.criar_monstro_aleatorio()
                obj_jogador.atacar(monstro)
            case 6:
                obj_jogador.curar()
            case 7:

                barra = ""
                tamanho_barra = 20
                proporcao = obj_jogador.getHp() / obj_jogador.getHPMax()
                quantidade_caracteres = int(proporcao * tamanho_barra)

                for i in range(quantidade_caracteres):
                    barra += "█"

                for i in range(tamanho_barra - quantidade_caracteres):
                    barra += "░"

                console.print(Panel(Align.center(
                    f"Nome: {obj_jogador.getNome()} \n"
                    f"HP: {barra} {obj_jogador.getHp()}/{obj_jogador.getHPMax()} \n"
                    f"Raça: {obj_jogador.getNomeRaca()} \n"
                    f"Profissão: {obj_jogador.getProfissao().getNomeProfissao()} \n"

                    f"Nível Geral de Jogador: {obj_jogador.getNivelGeral()} \n"
                    f"Nível Geral da Profissão: {obj_jogador.getProfissao().getNivelGeral()} \n"
                    f"Pontos de Habilidade Disponíveis: {obj_jogador.getQtdPontos()}"
                ), title="✦ Status do Personagem ✦"))

    return

if __name__ == "__main__":
    
    try:

        console = Console()

        console.print(Panel(Align.center("\n The Witcher - RPG \n")))

        inicializaJogo()

    except Exception as e:
        print(e)