# =========================================================
#  RPG Manager - The Witcher
#  Interface Grafica (PyQt5)
#  Liga as telas nas classes que ja existem no arquivo logica.py
# =========================================================

import sys
import io
import contextlib

from PyQt5.QtWidgets import (
    QApplication, QWidget, QStackedWidget, QLabel, QLineEdit, QPushButton,
    QComboBox, QSpinBox, QVBoxLayout, QHBoxLayout, QFormLayout, QTextEdit,
    QMessageBox, QDialog, QGridLayout, QSlider
)
from PyQt5.QtCore import Qt

# importa TODAS as classes do projeto (Humano, Bruxo, Mago, Factory, etc.)
from player_inventory import *


# Tema visual da interface (cores estilo The Witcher: preto e dourado)
ESTILO = """
QWidget {
    background-color: #1b1b1b;
    color: #e8e1d0;
    font-size: 14px;
    font-family: 'Segoe UI';
}
QLabel {
    color: #e8e1d0;
}
QLineEdit, QSpinBox, QComboBox {
    background-color: #2a2a2a;
    border: 1px solid #4a4a4a;
    border-radius: 4px;
    padding: 5px;
    color: #f5efe0;
}
QLineEdit:focus, QSpinBox:focus, QComboBox:focus {
    border: 1px solid #c8a44d;
}
QComboBox QAbstractItemView {
    background-color: #2a2a2a;
    selection-background-color: #c8a44d;
    selection-color: #1b1b1b;
}
QPushButton {
    background-color: #2e2a20;
    border: 1px solid #c8a44d;
    border-radius: 6px;
    padding: 9px 14px;
    color: #e7c977;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #c8a44d;
    color: #1b1b1b;
}
QPushButton:pressed {
    background-color: #a8863a;
}
QTextEdit {
    background-color: #141414;
    border: 1px solid #3a3a3a;
    border-radius: 6px;
    color: #d8d0bc;
    font-family: 'Consolas';
    font-size: 13px;
}
QSlider::groove:horizontal {
    height: 6px;
    background: #3a3a3a;
    border-radius: 3px;
}
QSlider::sub-page:horizontal {
    background: #c8a44d;
    border-radius: 3px;
}
QSlider::handle:horizontal {
    background: #e7c977;
    border: 1px solid #a8863a;
    width: 16px;
    height: 16px;
    margin: -6px 0;
    border-radius: 8px;
}
QSlider::handle:horizontal:hover {
    background: #ffe9a8;
}
"""


# Funcao que chama o atacar() da logica SEM deixar os paineis do Rich
# aparecerem no terminal (a gente mostra o resultado na propria janela)
def ataca_em_silencio(jogador, monstro):
    saida_falsa = io.StringIO()
    with contextlib.redirect_stdout(saida_falsa):
        jogador.atacar(monstro)
    return


# =========================================================
#  Janela para subir de nivel uma skill
#  Recebe uma lista de skills no formato (nome, getter, setter)
# =========================================================
class JanelaUparSkill(QDialog):

    def __init__(self, dono, lista_skills, get_pontos, nome_atributo_pontos, titulo):
        super().__init__()

        self._dono = dono
        self._lista_skills = lista_skills
        self._get_pontos = get_pontos
        self._nome_atributo_pontos = nome_atributo_pontos

        self.setWindowTitle(titulo)
        self.resize(420, 360)

        layout = QVBoxLayout()

        self._label_pontos = QLabel()
        self._label_pontos.setAlignment(Qt.AlignCenter)
        layout.addWidget(self._label_pontos)

        # cria um botao para cada skill
        self._botoes = []
        grid = QGridLayout()
        linha = 0
        for nome, getter, setter in self._lista_skills:
            botao = QPushButton()
            # guarda qual skill esse botao mexe
            botao.clicked.connect(self._fazer_clique(getter, setter, nome))
            grid.addWidget(botao, linha, 0)
            self._botoes.append((botao, getter))
            linha = linha + 1

        layout.addLayout(grid)

        botao_fechar = QPushButton("Fechar")
        botao_fechar.clicked.connect(self.accept)
        layout.addWidget(botao_fechar)

        self.setLayout(layout)
        self._atualiza_textos()

    # devolve a funcao que vai ser chamada quando clicar no botao da skill
    def _fazer_clique(self, getter, setter, nome):
        def clique():
            self._sobe_skill(getter, setter, nome)
        return clique

    def _pontos_atuais(self):
        return self._get_pontos()

    def _sobe_skill(self, getter, setter, nome):

        pontos = self._pontos_atuais()

        if pontos <= 0:
            QMessageBox.warning(self, "Sem pontos", "Voce nao tem pontos suficientes para subir de nivel!")
            return

        valor_atual = getattr(self._dono, getter)()

        if valor_atual >= 13:
            QMessageBox.warning(self, "Nivel maximo", "Essa skill ja esta no nivel maximo (13)!")
            return

        # sobe a skill em 1
        getattr(self._dono, setter)(valor_atual + 1)

        # gasta 1 ponto (mexe direto no atributo de pontos)
        valor_pontos = getattr(self._dono, self._nome_atributo_pontos)
        valor_pontos = valor_pontos - 1
        setattr(self._dono, self._nome_atributo_pontos, valor_pontos)

        self._atualiza_textos()

    def _atualiza_textos(self):
        self._label_pontos.setText("Pontos disponiveis: " + str(self._pontos_atuais()))
        for botao, getter in self._botoes:
            nome = None
            for n, g, s in self._lista_skills:
                if g == getter:
                    nome = n
            valor = getattr(self._dono, getter)()
            botao.setText(nome + "   (nivel " + str(valor) + ")")


# =========================================================
#  Janela principal do jogo
# =========================================================
class JanelaPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("RPG Manager - The Witcher")
        self.resize(700, 660)

        # aplica o tema visual (preto e dourado)
        self.setStyleSheet(ESTILO)

        # aqui fica guardado o personagem atual
        self._jogador = None

        # o StackedWidget troca entre a tela de criacao e a tela do jogo
        self._telas = QStackedWidget()

        self._tela_criacao = self._monta_tela_criacao()
        self._tela_jogo = self._monta_tela_jogo()

        self._telas.addWidget(self._tela_criacao)
        self._telas.addWidget(self._tela_jogo)

        layout = QVBoxLayout()
        titulo = QLabel("⚔  The Witcher — RPG Manager  ⚔")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 22px; font-weight: bold; padding: 12px; color: #e7c977;")
        layout.addWidget(titulo)
        layout.addWidget(self._telas)
        self.setLayout(layout)

        # comeca na tela de criacao
        self._telas.setCurrentWidget(self._tela_criacao)

    # cria uma barra deslizante (slider) com o numero aparecendo do lado
    # devolve o container (pra colocar na tela) e o slider (pra ler o valor depois)
    def _nova_barra(self, minimo, maximo, valor):

        container = QWidget()
        linha = QHBoxLayout()
        linha.setContentsMargins(0, 0, 0, 0)

        slider = QSlider(Qt.Horizontal)
        slider.setRange(minimo, maximo)
        slider.setValue(valor)

        rotulo = QLabel(str(valor))
        rotulo.setMinimumWidth(36)
        rotulo.setAlignment(Qt.AlignCenter)
        rotulo.setStyleSheet("color: #e7c977; font-weight: bold;")

        # quando arrastar a barra, o numero do lado muda junto
        slider.valueChanged.connect(self._atualizador(rotulo))

        linha.addWidget(slider)
        linha.addWidget(rotulo)
        container.setLayout(linha)

        return container, slider

    # devolve a funcao que atualiza o numero do lado da barra
    def _atualizador(self, rotulo):
        def mudou(valor):
            rotulo.setText(str(valor))
        return mudou

    # ---------------- TELA DE CRIACAO ----------------
    def _monta_tela_criacao(self):
        tela = QWidget()
        layout = QFormLayout()

        self._campo_nome = QLineEdit()
        self._campo_nome.setText("Geralt")

        # cada atributo agora e uma barra deslizante (slider) com o numero do lado
        self._cont_hp, self._campo_hp = self._nova_barra(1, 300, 100)
        self._cont_nivel, self._campo_nivel = self._nova_barra(0, 200, 0)
        self._cont_brigar, self._campo_brigar = self._nova_barra(0, 13, 0)
        self._cont_apostar, self._campo_apostar = self._nova_barra(0, 13, 0)
        self._cont_forca, self._campo_forca = self._nova_barra(0, 13, 0)
        self._cont_inteligencia, self._campo_inteligencia = self._nova_barra(0, 13, 0)

        self._campo_raca = QComboBox()
        self._campo_raca.addItem("Humano")
        self._campo_raca.addItem("Bruxo")
        self._campo_raca.addItem("Anao")
        self._campo_raca.addItem("Elfo")

        self._campo_profissao = QComboBox()
        self._campo_profissao.addItem("Mago")
        self._campo_profissao.addItem("Bardo")
        self._campo_profissao.addItem("Artesao")
        self._campo_profissao.addItem("Criminoso")
        self._campo_profissao.addItem("Doutor")
        self._campo_profissao.addItem("Cavaleiro")
        self._campo_profissao.addItem("Comerciante")
        self._campo_profissao.addItem("Sacerdote")
        self._campo_profissao.addItem("Desempregado")

        self._cont_nivel_profissao, self._campo_nivel_profissao = self._nova_barra(0, 200, 0)

        layout.addRow("Nome:", self._campo_nome)
        layout.addRow("HP (1-300):", self._cont_hp)
        layout.addRow("Nivel geral (0-200):", self._cont_nivel)
        layout.addRow("Raca:", self._campo_raca)
        layout.addRow("Brigar (0-13):", self._cont_brigar)
        layout.addRow("Apostar (0-13):", self._cont_apostar)
        layout.addRow("Forca (0-13):", self._cont_forca)
        layout.addRow("Inteligencia (0-13):", self._cont_inteligencia)
        layout.addRow("Profissao:", self._campo_profissao)
        layout.addRow("Nivel da profissao (0-200):", self._cont_nivel_profissao)

        botao_criar = QPushButton("Criar Personagem")
        botao_criar.clicked.connect(self._criar_personagem)
        layout.addRow(botao_criar)

        tela.setLayout(layout)
        return tela

    # ---------------- TELA DO JOGO ----------------
    def _monta_tela_jogo(self):

        tela = QWidget()
        layout = QVBoxLayout()

        self._label_status = QLabel()
        self._label_status.setStyleSheet("font-size: 14px; padding: 12px; background: #242018; color: #e7c977; border: 1px solid #c8a44d; border-radius: 6px;")
        self._label_status.setAlignment(Qt.AlignLeft)
        layout.addWidget(self._label_status)

        # area de texto que mostra o que acontece (combate, cura, etc.)
        self._log = QTextEdit()
        self._log.setReadOnly(True)
        layout.addWidget(self._log)

        # botoes de acao
        linha_botoes = QHBoxLayout()

        botao_upar_jogador = QPushButton("Upar Skill Jogador")
        botao_upar_jogador.clicked.connect(self._upar_skill_jogador)
        linha_botoes.addWidget(botao_upar_jogador)

        botao_upar_profissao = QPushButton("Upar Skill Profissao")
        botao_upar_profissao.clicked.connect(self._upar_skill_profissao)
        linha_botoes.addWidget(botao_upar_profissao)

        layout.addLayout(linha_botoes)

        linha_botoes2 = QHBoxLayout()

        botao_atacar = QPushButton("Atacar Monstro")
        botao_atacar.clicked.connect(self._atacar_monstro)
        linha_botoes2.addWidget(botao_atacar)

        botao_curar = QPushButton("Curar Personagem")
        botao_curar.clicked.connect(self._curar)
        linha_botoes2.addWidget(botao_curar)

        layout.addLayout(linha_botoes2)

        botao_novo = QPushButton("Criar Novo Personagem")
        botao_novo.clicked.connect(self._voltar_para_criacao)
        layout.addWidget(botao_novo)

        tela.setLayout(layout)
        return tela

    # ---------------- ACOES ----------------

    def _criar_personagem(self):

        # le o nome e valida
        nome = self._campo_nome.text()
        if nome.strip() == "":
            QMessageBox.warning(self, "Nome invalido", "Digite um nome para o personagem!")
            return

        hp = self._campo_hp.value()
        nivel = self._campo_nivel.value()
        brigar = self._campo_brigar.value()
        apostar = self._campo_apostar.value()
        forca = self._campo_forca.value()
        inteligencia = self._campo_inteligencia.value()

        indice_raca = self._campo_raca.currentIndex()

        # cria o jogador da raca escolhida (as skills especificas comecam em 0)
        if indice_raca == 0:  # Humano
            jogador = Humano(nome, hp, nivel, 5, brigar, apostar, forca, inteligencia)
        elif indice_raca == 1:  # Bruxo
            jogador = Bruxo(nome, hp, nivel, 13, brigar, apostar, forca, inteligencia)
        elif indice_raca == 2:  # Anao
            jogador = Anao(nome, hp, nivel, 7, brigar, apostar, forca, inteligencia)
        elif indice_raca == 3:  # Elfo
            jogador = Elfo(nome, hp, nivel, brigar, apostar, forca, inteligencia)

        # cria a profissao escolhida
        indice_profissao = self._campo_profissao.currentIndex()
        nivel_prof = self._campo_nivel_profissao.value()

        if indice_profissao == 0:
            profissao = Mago(nivel_geral=nivel_prof)
        elif indice_profissao == 1:
            profissao = Bardo(nivel_geral=nivel_prof)
        elif indice_profissao == 2:
            profissao = Artesao(nivel_geral=nivel_prof)
        elif indice_profissao == 3:
            profissao = Criminoso(nivel_geral=nivel_prof)
        elif indice_profissao == 4:
            profissao = Doutor(nivel_geral=nivel_prof)
        elif indice_profissao == 5:
            profissao = Cavaleiro(nivel_geral=nivel_prof)
        elif indice_profissao == 6:
            profissao = Comerciante(nivel_geral=nivel_prof)
        elif indice_profissao == 7:
            profissao = Sacerdote(nivel_geral=nivel_prof)
        elif indice_profissao == 8:
            profissao = Desempregado(nivel_geral=nivel_prof)

        jogador.setProfissao(profissao)

        self._jogador = jogador

        self._log.clear()
        self._escreve_log("Personagem " + nome + " criado com sucesso!")
        self._atualiza_status()

        # troca para a tela do jogo
        self._telas.setCurrentWidget(self._tela_jogo)

    def _atualiza_status(self):

        if self._jogador is None:
            return

        jogador = self._jogador

        nome_raca = type(jogador).__name__
        nome_profissao = type(jogador.getProfissao()).__name__

        texto = ""
        texto = texto + "Nome: " + jogador.getNome() + "\n"
        texto = texto + "Raca: " + nome_raca + "     Profissao: " + nome_profissao + "\n"
        texto = texto + "HP: " + str(jogador.getHp()) + " / " + str(jogador.getHPMax()) + "\n"
        texto = texto + "Nivel geral: " + str(jogador.getNivelGeral()) + "\n"
        texto = texto + "Brigar: " + str(jogador.getLvlBrigar())
        texto = texto + "   Apostar: " + str(jogador.getLvlApostar())
        texto = texto + "   Forca: " + str(jogador.getLvlForca())
        texto = texto + "   Inteligencia: " + str(jogador.getLvlInteligencia())

        self._label_status.setText(texto)

    def _escreve_log(self, mensagem):
        self._log.append(mensagem)

    # monta a lista de skills do jogador conforme a raca
    def _skills_do_jogador(self):

        jogador = self._jogador

        # skills basicas (todo jogador tem)
        lista = [
            ("Brigar", "getLvlBrigar", "setLvlBrigar"),
            ("Apostar", "getLvlApostar", "setLvlApostar"),
            ("Forca", "getLvlForca", "setLvlForca"),
            ("Inteligencia", "getLvlInteligencia", "setLvlInteligencia"),
        ]

        # skills especificas de cada raca
        if isinstance(jogador, Humano):
            lista.append(("Seducao", "getLvlSeducao", "setLvlSeducao"))
            lista.append(("Persuasao", "getLvlPersuasao", "setLvlPersuasao"))
            lista.append(("Teimosia", "getLvlTeimosia", "setLvlTeimosia"))
        elif isinstance(jogador, Bruxo):
            lista.append(("Reflexos Relampagos", "getLvlReflexos", "setLvlReflexosRelampagos"))
        elif isinstance(jogador, Anao):
            lista.append(("Armadura", "getLvlArmadura", "setLvlArmadura"))
            lista.append(("Deducao", "getLvlDeducao", "setLvlDeducao"))
        elif isinstance(jogador, Elfo):
            lista.append(("Artesanato", "getLvlArtesanato", "setLvlArtesanato"))
            lista.append(("Arcos", "getLvlArcos", "setLvlArcos"))
            lista.append(("Sintonia da Natureza", "getLvlSintoniaNatureza", "setLvlSintoniaNatureza"))

        return lista

    # monta a lista de skills da profissao
    def _skills_da_profissao(self):

        profissao = self._jogador.getProfissao()
        lista = []

        if isinstance(profissao, Mago):
            lista.append(("Criar Ritual", "getLvlCriarRitual", "setLvlCriarRitual"))
            lista.append(("Lancar Feitico", "getLvlLancarFeitico", "setLvlLancarFeitico"))
            lista.append(("Educacao", "getLvlEducacao", "setLvlEducacao"))
            lista.append(("Resistir Magia", "getLvlResistirMagia", "setLvlResistirMagia"))
        elif isinstance(profissao, Bardo):
            lista.append(("Etiqueta Social", "getLvlEtiquetaSocial", "setLvlEtiquetaSocial"))
            lista.append(("Ludibriar", "getLvlLudibriar", "setLvlLudibriar"))
            lista.append(("Sabedoria das Ruas", "getLvlSabedoriaDasRuas", "setLvlSabedoriaDasRuas"))
        elif isinstance(profissao, Artesao):
            lista.append(("Educacao", "getLvlEducacao", "setLvlEducacao"))
            lista.append(("Criacao", "getLvlCriacao", "setLvlCriacao"))
            lista.append(("Negociacao", "getLvlNegociacao", "setLvlNegociacao"))
            lista.append(("Fisico", "getLvlFisico", "setLvlFisico"))
        elif isinstance(profissao, Criminoso):
            lista.append(("Arrombar Fechaduras", "getLvlArrombarFechaduras", "setLvlArrombarFechaduras"))
            lista.append(("Falsificacao", "getLvlFalsificacao", "setLvlFalsificacao"))
            lista.append(("Atletismo", "getLvlAtletismo", "setLvlAtletismo"))
            lista.append(("Sabedoria das Ruas", "getLvlSabedoriaDasRuas", "setLvlSabedoriaDasRuas"))
        elif isinstance(profissao, Doutor):
            lista.append(("Carisma", "getLvlCarisma", "setLvlCarisma"))
            lista.append(("Educacao", "getLvlEducacao", "setLvlEducacao"))
            lista.append(("Coragem", "getLvlCoragem", "setLvlCoragem"))
            lista.append(("Alquimia", "getLvlAlquimia", "setLvlAlquimia"))
        elif isinstance(profissao, Cavaleiro):
            lista.append(("Coragem", "getLvlCoragem", "setLvlCoragem"))
            lista.append(("Intimidacao", "getLvlIntimidacao", "setLvlIntimidacao"))
            lista.append(("Sobrevivencia", "getLvlSobrevivencia", "setLvlSobrevivencia"))
            lista.append(("Esquivar", "getLvlEsquivar", "setLvlEsquivar"))
        elif isinstance(profissao, Comerciante):
            lista.append(("Carisma", "getLvlCarisma", "setLvlCarisma"))
            lista.append(("Educacao", "getLvlEducacao", "setLvlEducacao"))
            lista.append(("Negocios", "getLvlNegocios", "setLvlNegocios"))
            lista.append(("Persuasao", "getLvlPersuasao", "setLvlPersuasao"))
        elif isinstance(profissao, Sacerdote):
            lista.append(("Criar Ritual", "getLvlCriarRitual", "setLvlCriarRitual"))
            lista.append(("Coragem", "getLvlCoragem", "setLvlCoragem"))
            lista.append(("Ensinar", "getLvlEnsinar", "setLvlEnsinar"))
            lista.append(("Lancar Feitico", "getLvlLancarFeitico", "setLvlLancarFeitico"))
        elif isinstance(profissao, Desempregado):
            lista.append(("Sobrevivencia", "getLvlSobrevivencia", "setLvlSobrevivencia"))
            lista.append(("Consciencia", "getLvlConsciencia", "setLvlConsciencia"))

        return lista

    def _upar_skill_jogador(self):

        if self._jogador is None:
            return

        # converte o nivel geral em pontos (igual a logica original faz)
        self._jogador._transforma_pontos_experiencia()

        if self._jogador.getQtdPontos() <= 0:
            QMessageBox.information(self, "Sem pontos", "Voce precisa de pelo menos 10 de nivel geral para ganhar 1 ponto.")
            self._atualiza_status()
            return

        lista = self._skills_do_jogador()

        # abre a janela de upar, mexendo no atributo _qtd_pontos do jogador
        janela = JanelaUparSkill(
            self._jogador, lista,
            self._jogador.getQtdPontos, "_qtd_pontos",
            "Subir Skill do Jogador"
        )
        janela.exec_()

        self._escreve_log("Skills do jogador atualizadas.")
        self._atualiza_status()

    def _upar_skill_profissao(self):

        if self._jogador is None:
            return

        profissao = self._jogador.getProfissao()

        # converte o nivel geral da profissao em pontos
        profissao.transforma_pontos_experiencia()

        if profissao._qtd_pontos_profissao <= 0:
            QMessageBox.information(self, "Sem pontos", "A profissao precisa de pelo menos 10 de nivel para ganhar 1 ponto.")
            return

        lista = self._skills_da_profissao()

        def get_pontos_prof():
            return profissao._qtd_pontos_profissao

        janela = JanelaUparSkill(
            profissao, lista,
            get_pontos_prof, "_qtd_pontos_profissao",
            "Subir Skill da Profissao"
        )
        janela.exec_()

        self._escreve_log("Skills da profissao atualizadas.")
        self._atualiza_status()

    def _atacar_monstro(self):

        if self._jogador is None:
            return

        if self._jogador.getHp() <= 0:
            QMessageBox.warning(self, "Sem vida", "Seu personagem esta sem vida! Use Curar antes de atacar.")
            return

        # cria um monstro aleatorio
        monstro = MonstroFactory.criar_monstro_aleatorio()

        self._escreve_log("")
        self._escreve_log("--- Um " + monstro.getNome() + " apareceu! (HP " + str(monstro.getHp()) + ") ---")

        # luta por turnos: ataca ate o monstro morrer ou o jogador cair
        seguranca = 0
        while monstro.estaMorto() == False and self._jogador.getHp() > 0:

            hp_monstro_antes = monstro.getHp()
            hp_jogador_antes = self._jogador.getHp()

            ataca_em_silencio(self._jogador, monstro)

            dano_no_monstro = hp_monstro_antes - monstro.getHp()
            dano_no_jogador = hp_jogador_antes - self._jogador.getHp()

            self._escreve_log(
                self._jogador.getNome() + " causou " + str(dano_no_monstro) + " de dano   |   "
                "recebeu " + str(dano_no_jogador) + " de dano   |   "
                "HP monstro: " + str(monstro.getHp()) + "   HP voce: " + str(self._jogador.getHp())
            )

            seguranca = seguranca + 1
            if seguranca > 100:
                break

        if monstro.estaMorto() == True:
            self._escreve_log(">> " + monstro.getNome() + " foi derrotado! Voce ganhou XP.")
        else:
            self._escreve_log(">> Voce caiu em combate! Use Curar para se recuperar.")

        self._atualiza_status()

    def _curar(self):

        if self._jogador is None:
            return

        # chama o curar() da logica em silencio (ele tambem usa Rich)
        saida_falsa = io.StringIO()
        with contextlib.redirect_stdout(saida_falsa):
            self._jogador.curar()

        self._escreve_log(self._jogador.getNome() + " foi totalmente curado! HP: " + str(self._jogador.getHp()) + "/" + str(self._jogador.getHPMax()))
        self._atualiza_status()

    def _voltar_para_criacao(self):
        self._telas.setCurrentWidget(self._tela_criacao)


# =========================================================
#  Inicio do programa
# =========================================================
if __name__ == "__main__":

    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec_())