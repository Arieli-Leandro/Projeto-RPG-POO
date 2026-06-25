# =========================================================
#  Testes automatizados do RPG Manager
#  Usa o modulo unittest (ja vem com o Python, nao precisa instalar)
#
#  Como rodar no terminal:
#     python -m unittest test_logica.py -v
#
#  Ele testa a LOGICA (classes), nao a interface.
#  A interface (terminal ou grafica) usa input(), entao nao da pra
#  automatizar por ela - por isso a gente testa as classes direto.
# =========================================================

import unittest
import io
import contextlib

# importa as classes do projeto.
# usa o arquivo player_inventory.py (o teu); se nao achar, tenta logica.py
try:
    from player_inventory import *
except ImportError:
    from logica import *


# chama uma funcao que imprime paineis do Rich sem sujar a tela do teste
def silencioso(funcao, *args):
    saida_falsa = io.StringIO()
    with contextlib.redirect_stdout(saida_falsa):
        funcao(*args)
    return


# =========================================================
#  Testes de criacao de personagem
# =========================================================
class TesteCriacaoPersonagem(unittest.TestCase):

    def teste_cria_humano(self):
        h = Humano("Geralt", 100, 0, 5, 3, 2, 4, 1)
        self.assertEqual(h.getNome(), "Geralt")
        self.assertEqual(h.getHp(), 100)
        self.assertEqual(h.getLvlBrigar(), 3)
        self.assertEqual(h.getLvlForca(), 4)

    def teste_cria_bruxo(self):
        b = Bruxo("Lambert", 100, 0, 13, 1, 1, 1, 1)
        self.assertEqual(b.getNome(), "Lambert")
        # de acordo com o livro, bruxo tem carisma 0 sempre
        self.assertEqual(b.getCarisma(), 0)

    def teste_cria_anao(self):
        a = Anao("Zoltan", 100, 0, 7, 1, 1, 1, 1)
        self.assertEqual(a.getNome(), "Zoltan")
        self.assertEqual(a.getImunidade(), 7)

    def teste_cria_elfo(self):
        e = Elfo("Iorveth", 100, 0, 1, 1, 1, 1, 8)
        self.assertEqual(e.getNome(), "Iorveth")
        self.assertEqual(e.getImunidade(), 8)

    def teste_imunidade_humano(self):
        h = Humano("Teste", 100, 0, 5)
        self.assertEqual(h.getImunidade(), 5)


# =========================================================
#  Testes de validacao (regras de negocio)
# =========================================================
class TesteValidacoes(unittest.TestCase):

    def teste_nome_vazio_da_excecao(self):
        # nome vazio tem que levantar a excecao certa
        with self.assertRaises(ExcessaoNomeJogadorInvalido):
            Humano("", 100, 0, 5)

    def teste_hp_invalido_vira_zero(self):
        # hp negativo nao passa na validacao, entao vira 0
        h = Humano("Teste", 100, 0, 5)
        h.setHP(-50)
        self.assertEqual(h.getHp(), 0)

    def teste_hp_acima_do_maximo_vira_zero(self):
        # hp acima de 300 nao passa, vira 0
        h = Humano("Teste", 100, 0, 5)
        h.setHP(9999)
        self.assertEqual(h.getHp(), 0)

    def teste_atributo_negativo_vira_zero(self):
        # atributo negativo no construtor vira 0
        h = Humano("Teste", 100, 0, 5, -3, 0, 0, 0)
        self.assertEqual(h.getLvlBrigar(), 0)


# =========================================================
#  Testes do sistema de pontos / subir de nivel
# =========================================================
class TestePontos(unittest.TestCase):

    def teste_transforma_pontos_jogador(self):
        # nivel geral 45 -> deve virar 4 pontos e sobrar 5 de nivel
        h = Humano("Teste", 100, 45, 5)
        h._transforma_pontos_experiencia()
        self.assertEqual(h.getQtdPontos(), 4)
        self.assertEqual(h.getNivelGeral(), 5)

    def teste_sem_pontos_quando_nivel_baixo(self):
        # nivel 5 (menor que 10) -> 0 pontos
        h = Humano("Teste", 100, 5, 5)
        h._transforma_pontos_experiencia()
        self.assertEqual(h.getQtdPontos(), 0)

    def teste_transforma_pontos_profissao(self):
        # profissao com nivel 35 -> 3 pontos, sobra 5
        m = Mago(nivel_geral=35)
        m.transforma_pontos_experiencia()
        self.assertEqual(m._qtd_pontos_profissao, 3)
        self.assertEqual(m.getNivelGeral(), 5)


# =========================================================
#  Testes das profissoes
# =========================================================
class TesteProfissoes(unittest.TestCase):

    def teste_cria_todas_profissoes(self):
        # todas as profissoes devem ser criadas sem erro
        profissoes = [
            Mago(nivel_geral=10), Bardo(nivel_geral=10), Artesao(nivel_geral=10),
            Criminoso(nivel_geral=10), Doutor(nivel_geral=10), Cavaleiro(nivel_geral=10),
            Comerciante(nivel_geral=10), Sacerdote(nivel_geral=10), Desempregado(nivel_geral=10)
        ]
        for p in profissoes:
            self.assertEqual(p.getNivelGeral(), 10)

    def teste_jogador_recebe_profissao(self):
        h = Humano("Geralt", 100, 0, 5)
        prof = Mago(nivel_geral=20)
        h.setProfissao(prof)
        self.assertIsNotNone(h.getProfissao())
        self.assertEqual(h.getProfissao().getNivelGeral(), 20)

    def teste_setter_skill_profissao(self):
        m = Mago(nivel_geral=10)
        m.setLvlCriarRitual(5)
        self.assertEqual(m.getLvlCriarRitual(), 5)


# =========================================================
#  Testes do monstro
# =========================================================
class TesteMonstro(unittest.TestCase):

    def teste_monstro_recebe_dano(self):
        m = Monstro("Afogador", 15, 20)
        m.recebeDano(10)
        self.assertEqual(m.getHp(), 5)

    def teste_monstro_hp_nao_fica_negativo(self):
        # mesmo levando mais dano que a vida, o hp para em 0
        m = Monstro("Afogador", 15, 20)
        m.recebeDano(100)
        self.assertEqual(m.getHp(), 0)

    def teste_monstro_esta_morto(self):
        m = Monstro("Afogador", 15, 20)
        m.recebeDano(15)
        self.assertTrue(m.estaMorto())

    def teste_factory_cria_monstro(self):
        # a fabrica tem que devolver um objeto Monstro de verdade
        m = MonstroFactory.criar_monstro_aleatorio()
        self.assertIsInstance(m, Monstro)
        self.assertTrue(m.getHp() > 0)


# =========================================================
#  Testes de combate e cura
# =========================================================
class TesteCombate(unittest.TestCase):

    def teste_ataque_causa_dano(self):
        # forca 10 + brigar 5 = 15 de dano; monstro tem 15 de hp -> morre
        h = Humano("Geralt", 100, 0, 5, 5, 0, 10, 0)
        monstro = Monstro("Afogador", 15, 20)
        silencioso(h.atacar, monstro)
        self.assertTrue(monstro.estaMorto())

    def teste_ataque_da_xp_ao_matar(self):
        # ao matar o monstro, o nivel geral do jogador aumenta com o xp
        h = Humano("Geralt", 100, 0, 5, 5, 0, 10, 0)
        nivel_antes = h.getNivelGeral()
        monstro = Monstro("Afogador", 15, 20)
        silencioso(h.atacar, monstro)
        self.assertTrue(h.getNivelGeral() > nivel_antes)

    def teste_ataque_sem_vida_da_excecao(self):
        # jogador com 0 de hp nao pode atacar
        h = Humano("Geralt", 100, 0, 5)
        h.setHP(-1)  # cai pra 0 pela validacao
        monstro = Monstro("Afogador", 15, 20)
        with self.assertRaises(ExcessaoJogadorSemVida):
            silencioso(h.atacar, monstro)

    def teste_cura_restaura_hp(self):
        # depois de curar, o hp volta pro maximo
        h = Humano("Geralt", 100, 0, 5)
        h.setHP(50)
        silencioso(h.curar)
        self.assertEqual(h.getHp(), h.getHPMax())


# =========================================================
#  Testes das skills basicas (setters e getters)
# =========================================================
class TesteSkillsBasicas(unittest.TestCase):

    def teste_set_apostar(self):
        h = Humano("Teste", 100, 0, 5)
        h.setLvlApostar(7)
        self.assertEqual(h.getLvlApostar(), 7)

    def teste_set_inteligencia(self):
        h = Humano("Teste", 100, 0, 5)
        h.setLvlInteligencia(9)
        self.assertEqual(h.getLvlInteligencia(), 9)

    def teste_set_nivel_geral(self):
        h = Humano("Teste", 100, 0, 5)
        h.setNivelGeral(50)
        self.assertEqual(h.getNivelGeral(), 50)

    def teste_set_imunidade(self):
        h = Humano("Teste", 100, 0, 5)
        h.setImunidade(10)
        self.assertEqual(h.getImunidade(), 10)

    def teste_limite_skill_13(self):
        # no nivel 12 ainda pode subir (vira 13), no 13 nao pode mais
        h = Humano("Teste", 100, 0, 5)
        self.assertTrue(h.verifica_aumenta_lvl_habilidade(12))
        self.assertFalse(h.verifica_aumenta_lvl_habilidade(13))


# =========================================================
#  Testes das skills especificas de cada raca
# =========================================================
class TesteSkillsRaca(unittest.TestCase):

    def teste_humano_seducao(self):
        h = Humano("Teste", 100, 0, 5)
        h.setLvlSeducao(6)
        self.assertEqual(h.getLvlSeducao(), 6)

    def teste_humano_persuasao(self):
        h = Humano("Teste", 100, 0, 5)
        h.setLvlPersuasao(4)
        self.assertEqual(h.getLvlPersuasao(), 4)

    def teste_humano_teimosia(self):
        h = Humano("Teste", 100, 0, 5)
        h.setLvlTeimosia(3)
        self.assertEqual(h.getLvlTeimosia(), 3)

    def teste_bruxo_reflexos(self):
        b = Bruxo("Teste", 100, 0, 13)
        b.setLvlReflexosRelampagos(8)
        self.assertEqual(b.getLvlReflexos(), 8)

    def teste_anao_armadura(self):
        a = Anao("Teste", 100, 0, 7)
        a.setLvlArmadura(5)
        self.assertEqual(a.getLvlArmadura(), 5)

    def teste_anao_deducao(self):
        a = Anao("Teste", 100, 0, 7)
        a.setLvlDeducao(2)
        self.assertEqual(a.getLvlDeducao(), 2)

    def teste_elfo_artesanato(self):
        e = Elfo("Teste", 100, 0, 1, 1, 1, 1, 8)
        e.setLvlArtesanato(7)
        self.assertEqual(e.getLvlArtesanato(), 7)

    def teste_elfo_arcos(self):
        e = Elfo("Teste", 100, 0, 1, 1, 1, 1, 8)
        e.setLvlArcos(9)
        self.assertEqual(e.getLvlArcos(), 9)

    def teste_elfo_sintonia(self):
        e = Elfo("Teste", 100, 0, 1, 1, 1, 1, 8)
        e.setLvlSintoniaNatureza(6)
        self.assertEqual(e.getLvlSintoniaNatureza(), 6)


# =========================================================
#  Testes dos setters de TODAS as profissoes
# =========================================================
class TesteSkillsProfissao(unittest.TestCase):

    def teste_mago_skills(self):
        m = Mago(nivel_geral=10)
        m.setLvlLancarFeitico(5)
        m.setLvlEducacao(4)
        m.setLvlResistirMagia(3)
        self.assertEqual(m.getLvlLancarFeitico(), 5)
        self.assertEqual(m.getLvlEducacao(), 4)
        self.assertEqual(m.getLvlResistirMagia(), 3)

    def teste_bardo_skills(self):
        b = Bardo(nivel_geral=10)
        b.setLvlEtiquetaSocial(6)
        b.setLvlLudibriar(5)
        b.setLvlSabedoriaDasRuas(4)
        self.assertEqual(b.getLvlEtiquetaSocial(), 6)
        self.assertEqual(b.getLvlLudibriar(), 5)
        self.assertEqual(b.getLvlSabedoriaDasRuas(), 4)

    def teste_artesao_skills(self):
        a = Artesao(nivel_geral=10)
        a.setLvlCriacao(7)
        a.setLvlNegociacao(3)
        a.setLvlFisico(8)
        self.assertEqual(a.getLvlCriacao(), 7)
        self.assertEqual(a.getLvlNegociacao(), 3)
        self.assertEqual(a.getLvlFisico(), 8)

    def teste_criminoso_skills(self):
        c = Criminoso(nivel_geral=10)
        c.setLvlArrombarFechaduras(9)
        c.setLvlFalsificacao(5)
        c.setLvlAtletismo(6)
        self.assertEqual(c.getLvlArrombarFechaduras(), 9)
        self.assertEqual(c.getLvlFalsificacao(), 5)
        self.assertEqual(c.getLvlAtletismo(), 6)

    def teste_doutor_skills(self):
        d = Doutor(nivel_geral=10)
        d.setLvlCarisma(7)
        d.setLvlCoragem(5)
        d.setLvlAlquimia(8)
        self.assertEqual(d.getLvlCarisma(), 7)
        self.assertEqual(d.getLvlCoragem(), 5)
        self.assertEqual(d.getLvlAlquimia(), 8)

    def teste_cavaleiro_skills(self):
        c = Cavaleiro(nivel_geral=10)
        c.setLvlCoragem(6)
        c.setLvlIntimidacao(7)
        c.setLvlSobrevivencia(4)
        c.setLvlEsquivar(5)
        self.assertEqual(c.getLvlCoragem(), 6)
        self.assertEqual(c.getLvlIntimidacao(), 7)
        self.assertEqual(c.getLvlSobrevivencia(), 4)
        self.assertEqual(c.getLvlEsquivar(), 5)

    def teste_comerciante_skills(self):
        c = Comerciante(nivel_geral=10)
        c.setLvlCarisma(8)
        c.setLvlNegocios(6)
        c.setLvlPersuasao(7)
        self.assertEqual(c.getLvlCarisma(), 8)
        self.assertEqual(c.getLvlNegocios(), 6)
        self.assertEqual(c.getLvlPersuasao(), 7)

    def teste_sacerdote_skills(self):
        s = Sacerdote(nivel_geral=10)
        s.setLvlCriarRitual(5)
        s.setLvlCoragem(6)
        s.setLvlEnsinar(7)
        s.setLvlLancarFeitico(4)
        self.assertEqual(s.getLvlCriarRitual(), 5)
        self.assertEqual(s.getLvlCoragem(), 6)
        self.assertEqual(s.getLvlEnsinar(), 7)
        self.assertEqual(s.getLvlLancarFeitico(), 4)

    def teste_desempregado_skills(self):
        d = Desempregado(nivel_geral=10)
        d.setLvlSobrevivencia(5)
        d.setLvlConsciencia(6)
        self.assertEqual(d.getLvlSobrevivencia(), 5)
        self.assertEqual(d.getLvlConsciencia(), 6)


# =========================================================
#  Mais testes de combate
# =========================================================
class TesteCombateAvancado(unittest.TestCase):

    def teste_jogador_recebe_dano_ao_atacar(self):
        # ataque fraco: o monstro sobrevive e o jogador perde vida
        # monstro xp 20 -> jogador perde 0.5*20 = 10 de hp
        h = Humano("Geralt", 100, 0, 5, 0, 0, 1, 0)
        monstro = Monstro("Forte", 100, 20)
        silencioso(h.atacar, monstro)
        self.assertEqual(h.getHp(), 90)
        self.assertFalse(monstro.estaMorto())

    def teste_monstro_perde_vida_no_ataque(self):
        h = Humano("Geralt", 100, 0, 5, 5, 0, 5, 0)  # dano 10
        monstro = Monstro("Forte", 100, 20)
        silencioso(h.atacar, monstro)
        self.assertEqual(monstro.getHp(), 90)

    def teste_monstro_getters(self):
        m = Monstro("Leshen", 80, 120)
        self.assertEqual(m.getNome(), "Leshen")
        self.assertEqual(m.getXpRecompensa(), 120)


# roda todos os testes se executar este arquivo direto
if __name__ == "__main__":
    unittest.main(verbosity=2)