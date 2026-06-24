class ExcessaoTipoOpcaoInvalido(Exception):
    def __str__(self):
        return f"Digite um número inteiro!"
    
class ExcessaoOpcaoInvalida(Exception):
    def __str__(self):
        return f"Digite uma opção válida!"
    
class ExcessaoNomeJogadorInvalido(Exception):
    def __str__(self):
        return f"Digite um nome válido!"