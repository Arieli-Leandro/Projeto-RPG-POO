"""
Esse arquivo contém as excessões que interrompem o jogo caso elas aconteçam

-> ExcessaoTipoOpcaoInvalido: Ao decorrer do jogo tem muitos menus de seleção para que o usuário escolha o que fazer,
porém como dependendo do tipo de escolha se necessita de um tipo específico, caso o usuário digitar uma string em vez de um número inteiro ou
um número inteiro em vez de um string, pode acarretar na quebra do código, então essa excessão interrompe o jogo caso aconteça.

-> ExcessaoOpcaoInvalida: Quase o mesmo funcionamento da ExcessaoTipoOpcaoInvalido, mas como para o bom funiconamento das funções precisamos de um intervalo
fixo de opções, caso o usuário digitar uma opção fora desse intervalo pode causar uma quebra no programa. Então Essa excessão interrompe o Jogo antes que isso ocorar.

-> ExcessaoNomeJogadorInvalido: Essa excessão trata o caso do usuário digitar um nome vazio na hora de criar o personagem.
Por mais que não vai ocorrer nenhuma quebra de código se acontecer, obrigatoriamente o jogador precisa dar um nome ao Personagem.

"""


class ExcessaoTipoOpcaoInvalido(Exception):
    def __str__(self):
        return f"Digite um número inteiro!"
    
class ExcessaoOpcaoInvalida(Exception):
    def __str__(self):
        return f"Digite uma opção válida!"
    
class ExcessaoNomeJogadorInvalido(Exception):
    def __str__(self):
        return f"Digite um nome válido!"