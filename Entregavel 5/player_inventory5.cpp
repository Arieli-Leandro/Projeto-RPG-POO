#include <string>
#include <iostream>
using namespace std;

class Profissao {

    protected:
        int qtd_pontos_profissao = 0;
        int nivel_geral_profissao;

        bool valida_atributo_construtor(int valor) {
            bool retorno = false;
            if (valor > 0) {
                retorno = true;
            }
            return retorno;
        }

    public:
        
        Profissao(int nivel_geral_profissao_user) {
            if (valida_atributo_construtor(nivel_geral_profissao_user) == true) {
                this->nivel_geral_profissao = nivel_geral_profissao_user;
            } else {
                this->nivel_geral_profissao = 0;
            }
        }

        
        Profissao() {
            this->nivel_geral_profissao = 0;
        }

        
        virtual ~Profissao() {
            cout << "Profissao deletada" << endl;
        }

        virtual void inicializa_profissao() = 0;

        void transforma_pontos_experiencia() {
            while (nivel_geral_profissao >= 10) {
                nivel_geral_profissao = nivel_geral_profissao - 10;
                qtd_pontos_profissao += 1;
            }
            return;
        }

        bool verifica_aumenta_lvl_habilidade(int valor) {
            bool retorno = true;
            valor = valor + 1;
            if (valor > 13) {
                retorno = false;
            }
            return retorno;
        }
};

class Mago : public Profissao {

    private:
        int lvl_criar_ritual;
        int lvl_lancar_feitico;
        int lvl_educacao;
        int lvl_resistir_magia;

    public:
        
        Mago(int lvl_criar_ritual_user, int lvl_lancar_feitico_user, int lvl_educacao_user, int lvl_resistir_magia_user, int nivel_geral_user) : Profissao(nivel_geral_user) {
            if (valida_atributo_construtor(lvl_criar_ritual_user) == true) {
                this->lvl_criar_ritual = lvl_criar_ritual_user;
            } else { this->lvl_criar_ritual = 0; }

            if (valida_atributo_construtor(lvl_lancar_feitico_user) == true) {
                this->lvl_lancar_feitico = lvl_lancar_feitico_user;
            } else { this->lvl_lancar_feitico = 0; }

            if (valida_atributo_construtor(lvl_educacao_user) == true) {
                this->lvl_educacao = lvl_educacao_user;
            } else { this->lvl_educacao = 0; }

            if (valida_atributo_construtor(lvl_resistir_magia_user) == true) {
                this->lvl_resistir_magia = lvl_resistir_magia_user;
            } else { this->lvl_resistir_magia = 0; }
        }

        
        Mago() : Profissao() {
            this->lvl_criar_ritual = 0;
            this->lvl_educacao = 0;
            this->lvl_lancar_feitico = 0;
            this->lvl_resistir_magia = 0;
        }

        
        void inicializa_profissao() override {
            return;
        }

        void aumenta_nivel_habilidade_profissao() {
            int opcao = 0;

            if (qtd_pontos_profissao > 0) {
                while (true) {
                    cout << "1 - Upar Habilidade de: Criar Ritual" << endl;
                    cout << "2 - Upar Habilidade de: Educacao" << endl;
                    cout << "3 - Upar Habilidade de: Lancar Feitico" << endl;
                    cout << "4 - Upar Habilidade de: Resistir Magia" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 1 and opcao <= 4) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 1:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_criar_ritual) == true) {
                            lvl_criar_ritual += 1;
                            cout << "Subiu de nivel em Criar Ritual!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 2:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_educacao) == true) {
                            lvl_educacao += 1;
                            cout << "Subiu de nivel em Educacao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 3:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_lancar_feitico) == true) {
                            lvl_lancar_feitico += 1;
                            cout << "Subiu de nivel em Lancar Feitico!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 4:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_resistir_magia) == true) {
                            lvl_resistir_magia += 1;
                            cout << "Subiu de nivel em Resistir a Magia!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                }
            } else {
                cout << "Voce nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Bardo : public Profissao {

    private:
        int lvl_etiqueta_social;
        int lvl_ludibriar;
        int lvl_sabedoria_das_ruas;

    public:
        
        Bardo(int lvl_etiqueta_social_user, int lvl_ludibriar_user, int lvl_sabedoria_das_ruas_user, int nivel_geral_user) : Profissao(nivel_geral_user) {
            if (valida_atributo_construtor(lvl_etiqueta_social_user) == true) {
                this->lvl_etiqueta_social = lvl_etiqueta_social_user;
            } else { this->lvl_etiqueta_social = 0; }

            if (valida_atributo_construtor(lvl_ludibriar_user) == true) {
                this->lvl_ludibriar = lvl_ludibriar_user;
            } else { this->lvl_ludibriar = 0; }

            if (valida_atributo_construtor(lvl_sabedoria_das_ruas_user) == true) {
                this->lvl_sabedoria_das_ruas = lvl_sabedoria_das_ruas_user;
            } else { this->lvl_sabedoria_das_ruas = 0; }
        }

        
        Bardo() : Profissao() {
            this->lvl_etiqueta_social = 0;
            this->lvl_ludibriar = 0;
            this->lvl_sabedoria_das_ruas = 0;
        }

        
        void inicializa_profissao() override {
            return;
        }

        void aumenta_nivel_habilidade_profissao() {
            int opcao = 0;

            if (qtd_pontos_profissao > 0) {
                while (true) {
                    cout << "1 - Upar Habilidade de: Etiqueta Social" << endl;
                    cout << "2 - Upar Habilidade de: Ludibriar" << endl;
                    cout << "3 - Upar Habilidade de: Sabedoria das Ruas" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 1 and opcao <= 3) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 1:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_etiqueta_social) == true) {
                            lvl_etiqueta_social += 1;
                            cout << "Subiu de nivel em Etiqueta Social!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 2:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_ludibriar) == true) {
                            lvl_ludibriar += 1;
                            cout << "Subiu de nivel em Ludibriar!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 3:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_sabedoria_das_ruas) == true) {
                            lvl_sabedoria_das_ruas += 1;
                            cout << "Subiu de nivel em Sabedoria das Ruas!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                }
            } else {
                cout << "Voce nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Artesao : public Profissao {

    private:
        int lvl_educacao;
        int lvl_criacao;
        int lvl_negociacao;
        int lvl_fisico;

    public:
        
        Artesao(int lvl_educacao_user, int lvl_criacao_user, int lvl_negociacao_user, int lvl_fisico_user, int nivel_geral_user) : Profissao(nivel_geral_user) {
            if (valida_atributo_construtor(lvl_educacao_user) == true) {
                this->lvl_educacao = lvl_educacao_user;
            } else { this->lvl_educacao = 0; }

            if (valida_atributo_construtor(lvl_criacao_user) == true) {
                this->lvl_criacao = lvl_criacao_user;
            } else { this->lvl_criacao = 0; }

            if (valida_atributo_construtor(lvl_negociacao_user) == true) {
                this->lvl_negociacao = lvl_negociacao_user;
            } else { this->lvl_negociacao = 0; }

            if (valida_atributo_construtor(lvl_fisico_user) == true) {
                this->lvl_fisico = lvl_fisico_user;
            } else { this->lvl_fisico = 0; }
        }

        
        Artesao() : Profissao() {
            this->lvl_educacao = 0;
            this->lvl_criacao = 0;
            this->lvl_negociacao = 0;
            this->lvl_fisico = 0;
        }

        
        void inicializa_profissao() override {
            return;
        }

        void aumenta_nivel_habilidade_profissao() {
            int opcao = 0;

            if (qtd_pontos_profissao > 0) {
                while (true) {
                    cout << "1 - Upar Habilidade de: Educacao" << endl;
                    cout << "2 - Upar Habilidade de: Criacao" << endl;
                    cout << "3 - Upar Habilidade de: Negociacao" << endl;
                    cout << "4 - Upar Habilidade de: Fisico" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 1 and opcao <= 4) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 1:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_educacao) == true) {
                            lvl_educacao += 1;
                            cout << "Subiu de nivel em Educacao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 2:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_criacao) == true) {
                            lvl_criacao += 1;
                            cout << "Subiu de nivel em Criacao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 3:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_negociacao) == true) {
                            lvl_negociacao += 1;
                            cout << "Subiu de nivel em Negociacao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 4:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_fisico) == true) {
                            lvl_fisico += 1;
                            cout << "Subiu de nivel em Fisico!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                }
            } else {
                cout << "Voce nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Criminoso : public Profissao {

    private:
        int lvl_arrombar_fechaduras;
        int lvl_falsificacao;
        int lvl_atletismo;
        int lvl_sabedoria_das_ruas;

    public:
        
        Criminoso(int lvl_arrombar_fechaduras_user, int lvl_falsificacao_user, int lvl_atletismo_user, int lvl_sabedoria_das_ruas_user, int nivel_geral_user) : Profissao(nivel_geral_user) {
            if (valida_atributo_construtor(lvl_arrombar_fechaduras_user) == true) {
                this->lvl_arrombar_fechaduras = lvl_arrombar_fechaduras_user;
            } else { this->lvl_arrombar_fechaduras = 0; }

            if (valida_atributo_construtor(lvl_falsificacao_user) == true) {
                this->lvl_falsificacao = lvl_falsificacao_user;
            } else { this->lvl_falsificacao = 0; }

            if (valida_atributo_construtor(lvl_atletismo_user) == true) {
                this->lvl_atletismo = lvl_atletismo_user;
            } else { this->lvl_atletismo = 0; }

            if (valida_atributo_construtor(lvl_sabedoria_das_ruas_user) == true) {
                this->lvl_sabedoria_das_ruas = lvl_sabedoria_das_ruas_user;
            } else { this->lvl_sabedoria_das_ruas = 0; }
        }

        
        Criminoso() : Profissao() {
            this->lvl_arrombar_fechaduras = 0;
            this->lvl_falsificacao = 0;
            this->lvl_atletismo = 0;
            this->lvl_sabedoria_das_ruas = 0;
        }

        
        void inicializa_profissao() override {
            return;
        }

        void aumenta_nivel_habilidade_profissao() {
            int opcao = 0;

            if (qtd_pontos_profissao > 0) {
                while (true) {
                    cout << "1 - Upar Habilidade de: Arrombar Fechadura" << endl;
                    cout << "2 - Upar Habilidade de: Falsificacao" << endl;
                    cout << "3 - Upar Habilidade de: Atletismo" << endl;
                    cout << "4 - Upar Habilidade de: Sabedoria das Ruas" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 1 and opcao <= 4) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 1:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_arrombar_fechaduras) == true) {
                            lvl_arrombar_fechaduras += 1;
                            cout << "Subiu de nivel em Arrombar Fechaduras!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 2:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_falsificacao) == true) {
                            lvl_falsificacao += 1;
                            cout << "Subiu de nivel em Falsificacao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 3:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_atletismo) == true) {
                            lvl_atletismo += 1;
                            cout << "Subiu de nivel em Atletismo!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 4:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_sabedoria_das_ruas) == true) {
                            lvl_sabedoria_das_ruas += 1;
                            cout << "Subiu de nivel em Sabedoria das Ruas!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                }
            } else {
                cout << "Voce nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Doutor : public Profissao {

    private:
        int lvl_carisma;
        int lvl_educacao;
        int lvl_coragem;
        int lvl_alquimia;

    public:
        
        Doutor(int lvl_carisma_user, int lvl_educacao_user, int lvl_coragem_user, int lvl_alquimia_user, int nivel_geral_user) : Profissao(nivel_geral_user) {
            if (valida_atributo_construtor(lvl_carisma_user) == true) {
                this->lvl_carisma = lvl_carisma_user;
            } else { this->lvl_carisma = 0; }

            if (valida_atributo_construtor(lvl_educacao_user) == true) {
                this->lvl_educacao = lvl_educacao_user;
            } else { this->lvl_educacao = 0; }

            if (valida_atributo_construtor(lvl_coragem_user) == true) {
                this->lvl_coragem = lvl_coragem_user;
            } else { this->lvl_coragem = 0; }

            if (valida_atributo_construtor(lvl_alquimia_user) == true) {
                this->lvl_alquimia = lvl_alquimia_user;
            } else { this->lvl_alquimia = 0; }
        }

        
        Doutor() : Profissao() {
            this->lvl_carisma = 0;
            this->lvl_educacao = 0;
            this->lvl_coragem = 0;
            this->lvl_alquimia = 0;
        }

        
        void inicializa_profissao() override {
            return;
        }

        void aumenta_nivel_habilidade_profissao() {
            int opcao = 0;

            if (qtd_pontos_profissao > 0) {
                while (true) {
                    cout << "1 - Upar Habilidade de: Educacao" << endl;
                    cout << "2 - Upar Habilidade de: Coragem" << endl;
                    cout << "3 - Upar Habilidade de: Alquimia" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 1 and opcao <= 3) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 1:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_educacao) == true) {
                            lvl_educacao += 1;
                            cout << "Subiu de nivel em Educacao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 2:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_coragem) == true) {
                            lvl_coragem += 1;
                            cout << "Subiu de nivel em Coragem!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 3:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_alquimia) == true) {
                            lvl_alquimia += 1;
                            cout << "Subiu de nivel em Alquimia!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                }
            } else {
                cout << "Voce nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Cavaleiro : public Profissao {

    private:
        int lvl_coragem;
        int lvl_intimidacao;
        int lvl_sobrevivencia;
        int lvl_esquivar;

    public:
        
        Cavaleiro(int lvl_coragem_user, int lvl_intimidacao_user, int lvl_sobrevivencia_user, int lvl_esquivar_user, int nivel_geral_user) : Profissao(nivel_geral_user) {
            if (valida_atributo_construtor(lvl_coragem_user) == true) {
                this->lvl_coragem = lvl_coragem_user;
            } else { this->lvl_coragem = 0; }

            if (valida_atributo_construtor(lvl_intimidacao_user) == true) {
                this->lvl_intimidacao = lvl_intimidacao_user;
            } else { this->lvl_intimidacao = 0; }

            if (valida_atributo_construtor(lvl_sobrevivencia_user) == true) {
                this->lvl_sobrevivencia = lvl_sobrevivencia_user;
            } else { this->lvl_sobrevivencia = 0; }

            if (valida_atributo_construtor(lvl_esquivar_user) == true) {
                this->lvl_esquivar = lvl_esquivar_user;
            } else { this->lvl_esquivar = 0; }
        }

        
        Cavaleiro() : Profissao() {
            this->lvl_coragem = 0;
            this->lvl_intimidacao = 0;
            this->lvl_sobrevivencia = 0;
            this->lvl_esquivar = 0;
        }

        
        void inicializa_profissao() override {
            return;
        }

        void aumenta_nivel_habilidade_profissao() {
            int opcao = 0;

            if (qtd_pontos_profissao > 0) {
                while (true) {
                    cout << "1 - Upar Habilidade de: Coragem" << endl;
                    cout << "2 - Upar Habilidade de: Intimidacao" << endl;
                    cout << "3 - Upar Habilidade de: Sobrevivencia" << endl;
                    cout << "4 - Upar Habilidade de: Esquivar" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 1 and opcao <= 4) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 1:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_coragem) == true) {
                            lvl_coragem += 1;
                            cout << "Subiu de nivel em Coragem!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 2:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_intimidacao) == true) {
                            lvl_intimidacao += 1;
                            cout << "Subiu de nivel em Intimidacao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 3:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_sobrevivencia) == true) {
                            lvl_sobrevivencia += 1;
                            cout << "Subiu de nivel em Sobrevivencia!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 4:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_esquivar) == true) {
                            lvl_esquivar += 1;
                            cout << "Subiu de nivel em Esquivar!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                }
            } else {
                cout << "Voce nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Comerciante : public Profissao {

    private:
        int lvl_carisma;
        int lvl_educacao;
        int lvl_negocios;
        int lvl_persuasao;

    public:
        
        Comerciante(int lvl_carisma_user, int lvl_educacao_user, int lvl_negocios_user, int lvl_persuasao_user, int nivel_geral_user) : Profissao(nivel_geral_user) {
            if (valida_atributo_construtor(lvl_carisma_user) == true) {
                this->lvl_carisma = lvl_carisma_user;
            } else { this->lvl_carisma = 0; }

            if (valida_atributo_construtor(lvl_educacao_user) == true) {
                this->lvl_educacao = lvl_educacao_user;
            } else { this->lvl_educacao = 0; }

            if (valida_atributo_construtor(lvl_negocios_user) == true) {
                this->lvl_negocios = lvl_negocios_user;
            } else { this->lvl_negocios = 0; }

            if (valida_atributo_construtor(lvl_persuasao_user) == true) {
                this->lvl_persuasao = lvl_persuasao_user;
            } else { this->lvl_persuasao = 0; }
        }

        
        Comerciante() : Profissao() {
            this->lvl_carisma = 0;
            this->lvl_educacao = 0;
            this->lvl_negocios = 0;
            this->lvl_persuasao = 0;
        }

        
        void inicializa_profissao() override {
            return;
        }

        void aumenta_nivel_habilidade_profissao() {
            int opcao = 0;

            if (qtd_pontos_profissao > 0) {
                while (true) {
                    cout << "1 - Upar Habilidade de: Carisma" << endl;
                    cout << "2 - Upar Habilidade de: Educacao" << endl;
                    cout << "3 - Upar Habilidade de: Negocios" << endl;
                    cout << "4 - Upar Habilidade de: Persuasao" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 1 and opcao <= 4) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 1:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_carisma) == true) {
                            lvl_carisma += 1;
                            cout << "Subiu de nivel em Carisma!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 2:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_educacao) == true) {
                            lvl_educacao += 1;
                            cout << "Subiu de nivel em Educacao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 3:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_negocios) == true) {
                            lvl_negocios += 1;
                            cout << "Subiu de nivel em Negocios!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 4:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_persuasao) == true) {
                            lvl_persuasao += 1;
                            cout << "Subiu de nivel em Persuasao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                }
            } else {
                cout << "Voce nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Sacerdote : public Profissao {

    private:
        int lvl_criar_ritual;
        int lvl_coragem;
        int lvl_ensinar;
        int lvl_lancar_feitico;

    public:
        
        Sacerdote(int lvl_criar_ritual_user, int lvl_coragem_user, int lvl_ensinar_user, int lvl_lancar_feitico_user, int nivel_geral_user) : Profissao(nivel_geral_user) {
            if (valida_atributo_construtor(lvl_criar_ritual_user) == true) {
                this->lvl_criar_ritual = lvl_criar_ritual_user;
            } else { this->lvl_criar_ritual = 0; }

            if (valida_atributo_construtor(lvl_coragem_user) == true) {
                this->lvl_coragem = lvl_coragem_user;
            } else { this->lvl_coragem = 0; }

            if (valida_atributo_construtor(lvl_ensinar_user) == true) {
                this->lvl_ensinar = lvl_ensinar_user;
            } else { this->lvl_ensinar = 0; }

            if (valida_atributo_construtor(lvl_lancar_feitico_user) == true) {
                this->lvl_lancar_feitico = lvl_lancar_feitico_user;
            } else { this->lvl_lancar_feitico = 0; }
        }

        
        Sacerdote() : Profissao() {
            this->lvl_criar_ritual = 0;
            this->lvl_coragem = 0;
            this->lvl_ensinar = 0;
            this->lvl_lancar_feitico = 0;
        }

        
        void inicializa_profissao() override {
            return;
        }

        void aumenta_nivel_habilidade_profissao() {
            int opcao = 0;

            if (qtd_pontos_profissao > 0) {
                while (true) {
                    cout << "1 - Upar Habilidade de: Criar Ritual" << endl;
                    cout << "2 - Upar Habilidade de: Coragem" << endl;
                    cout << "3 - Upar Habilidade de: Ensinar" << endl;
                    cout << "4 - Upar Habilidade de: Lancar Feitico" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 1 and opcao <= 4) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 1:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_criar_ritual) == true) {
                            lvl_criar_ritual += 1;
                            cout << "Subiu de nivel em Criar Ritual!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 2:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_coragem) == true) {
                            lvl_coragem += 1;
                            cout << "Subiu de nivel em Coragem!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 3:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_ensinar) == true) {
                            lvl_ensinar += 1;
                            cout << "Subiu de nivel em Ensinar!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 4:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_lancar_feitico) == true) {
                            lvl_lancar_feitico += 1;
                            cout << "Subiu de nivel em Lancar Feitico!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                }
            } else {
                cout << "Voce nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Desempregado : public Profissao {

    private:
        int lvl_sobrevivencia;
        int lvl_consciencia;

    public:
        
        Desempregado(int lvl_sobrevivencia_user, int lvl_consciencia_user, int nivel_geral_user) : Profissao(nivel_geral_user) {
            if (valida_atributo_construtor(lvl_sobrevivencia_user) == true) {
                this->lvl_sobrevivencia = lvl_sobrevivencia_user;
            } else { this->lvl_sobrevivencia = 0; }

            if (valida_atributo_construtor(lvl_consciencia_user) == true) {
                this->lvl_consciencia = lvl_consciencia_user;
            } else { this->lvl_consciencia = 0; }
        }

        
        Desempregado() : Profissao() {
            this->lvl_sobrevivencia = 0;
            this->lvl_consciencia = 0;
        }

        
        void inicializa_profissao() override {
            return;
        }

        void aumenta_nivel_habilidade_profissao() {
            int opcao = 0;

            if (qtd_pontos_profissao > 0) {
                while (true) {
                    cout << "1 - Upar Habilidade de: Sobrevivencia" << endl;
                    cout << "2 - Upar Habilidade de: Consciencia" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 1 and opcao <= 2) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 1:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_sobrevivencia) == true) {
                            lvl_sobrevivencia += 1;
                            cout << "Subiu de nivel em Sobrevivencia!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 2:
                        qtd_pontos_profissao -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_consciencia) == true) {
                            lvl_consciencia += 1;
                            cout << "Subiu de nivel em Consciencia!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                }
            } else {
                cout << "Voce nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Jogador {

    protected:
        Profissao *profissao_jogador;
        string nome;
        int hp;
        int hp_maximo = 100;
        int nivel_geral;
        int qtd_pontos = 0;
        int lvl_brigar;
        int lvl_apostar;
        int lvl_forca;
        int lvl_coragem;
        int lvl_inteligencia;

        bool valida_atributo_construtor(int valor) {
            bool retorno = false;
            if (valor > 0) {
                retorno = true;
            }
            return retorno;
        }

        void transforma_pontos_experiencia() {
            while (nivel_geral >= 10) {
                nivel_geral = nivel_geral - 10;
                qtd_pontos += 1;
            }
            return;
        }

    public:
        
        Jogador(string nome_user, int hp_user, int nivel_geral_user, int lvl_brigar_user, int lvl_apostar_user, int lvl_forca_user, int lvl_coragem_user, int lvl_inteligencia_user) {
            this->profissao_jogador = nullptr;
            this->nome = nome_user;

            if (valida_atributo_construtor(hp_user) == true) {
                this->hp = hp_user;
            } else { this->hp = 0; }

            if (valida_atributo_construtor(nivel_geral_user) == true) {
                this->nivel_geral = nivel_geral_user;
            } else { this->nivel_geral = 0; }

            if (valida_atributo_construtor(lvl_brigar_user) == true) {
                this->lvl_brigar = lvl_brigar_user;
            } else { this->lvl_brigar = 0; }

            if (valida_atributo_construtor(lvl_apostar_user) == true) {
                this->lvl_apostar = lvl_apostar_user;
            } else { this->lvl_apostar = 0; }

            if (valida_atributo_construtor(lvl_forca_user) == true) {
                this->lvl_forca = lvl_forca_user;
            } else { this->lvl_forca = 0; }

            if (valida_atributo_construtor(lvl_coragem_user) == true) {
                this->lvl_coragem = lvl_coragem_user;
            } else { this->lvl_coragem = 0; }

            if (valida_atributo_construtor(lvl_inteligencia_user) == true) {
                this->lvl_inteligencia = lvl_inteligencia_user;
            } else { this->lvl_inteligencia = 0; }
        }

        
        Jogador() {
            this->profissao_jogador = nullptr;
            this->nome = "Guest";
            this->hp = 100;
            this->nivel_geral = 0;
            this->lvl_apostar = 0;
            this->lvl_brigar = 0;
            this->lvl_coragem = 0;
            this->lvl_forca = 0;
            this->lvl_inteligencia = 0;
        }

        
        virtual ~Jogador() {
            cout << "Removendo os dados do jogador: " << nome << endl;
        }

        void set_profissao(Profissao* p) {
            this->profissao_jogador = p;
        }

        string get_nome() {
            return this->nome;
        }

        bool verifica_aumenta_lvl_habilidade(int valor) {
            bool retorno = true;
            valor = valor + 1;
            if (valor > 13) {
                retorno = false;
            }
            return retorno;
        }

        virtual void aumenta_nivel_habilidade() {
            transforma_pontos_experiencia();

            int opcao = 0;

            if (qtd_pontos > 0) {
                while (true) {
                    cout << "1 - Upar Habilidade de: Aposta" << endl;
                    cout << "2 - Upar Habilidade de: Brigar" << endl;
                    cout << "3 - Upar Habilidade de: Coragem" << endl;
                    cout << "4 - Upar Habilidade de: Forca" << endl;
                    cout << "5 - Upar Habilidade de: Inteligencia" << endl;
                    cout << "6 - Nao Upar Habilidade Basica" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 1 and opcao <= 6) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 1:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_apostar) == true) {
                            lvl_apostar += 1;
                            cout << nome << " subiu de nivel em Aposta!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 2:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_brigar) == true) {
                            lvl_brigar += 1;
                            cout << nome << " subiu de nivel em Brigar!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 3:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_coragem) == true) {
                            lvl_coragem += 1;
                            cout << nome << " subiu de nivel em Coragem!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 4:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_forca) == true) {
                            lvl_forca += 1;
                            cout << nome << " subiu de nivel em Forca!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 5:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_inteligencia) == true) {
                            lvl_inteligencia += 1;
                            cout << nome << " subiu de nivel em Inteligencia!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 6:
                        break;
                }
            } else {
                cout << nome << " nao tem pontos suficientes para subir de nivel" << endl;
            }
        }

        virtual void inicializa_jogador() = 0;
};

class Humano : public Jogador {

    private:
        int imunidade;
        int lvl_seducao;
        int lvl_persuasao;
        int lvl_teimosia;

    public:
        
        Humano(string nome_user, int hp_user, int nivel_geral_user, int lvl_brigar_user, int lvl_apostar_user, int lvl_forca_user, int lvl_coragem_user, int lvl_inteligencia_user, int imunidade_user, int lvl_seducao_user, int lvl_persuasao_user, int teimosia_user) : Jogador(nome_user, hp_user, nivel_geral_user, lvl_brigar_user, lvl_apostar_user, lvl_forca_user, lvl_coragem_user, lvl_inteligencia_user) {
            if (valida_atributo_construtor(imunidade_user) == true) {
                this->imunidade = imunidade_user;
            } else { this->imunidade = 0; }

            if (valida_atributo_construtor(lvl_seducao_user) == true) {
                this->lvl_seducao = lvl_seducao_user;
            } else { this->lvl_seducao = 0; }

            if (valida_atributo_construtor(lvl_persuasao_user) == true) {
                this->lvl_persuasao = lvl_persuasao_user;
            } else { this->lvl_persuasao = 0; }

            if (valida_atributo_construtor(teimosia_user) == true) {
                this->lvl_teimosia = teimosia_user;
            } else { this->lvl_teimosia = 0; }
        }

        
        Humano() : Jogador() {
            this->imunidade = 0;
            this->lvl_seducao = 0;
            this->lvl_persuasao = 0;
            this->lvl_teimosia = 0;
        }

        
        void inicializa_jogador() override {
            return;
        }

        
        void aumenta_nivel_habilidade() override {
            
            Jogador::aumenta_nivel_habilidade();

            int opcao = 0;

            if (qtd_pontos > 0) {
                while (true) {
                    cout << "6 - Upar Habilidade de: Seducao" << endl;
                    cout << "7 - Upar Habilidade de: Persuasao" << endl;
                    cout << "8 - Upar Habilidade de: Teimosia" << endl;
                    cout << "9 - Nao Upar Habilidade Especifica" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 6 and opcao <= 9) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 6:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_seducao) == true) {
                            lvl_seducao += 1;
                            cout << nome << " subiu de nivel em Seducao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 7:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_persuasao) == true) {
                            lvl_persuasao += 1;
                            cout << nome << " subiu de nivel em Persuasao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 8:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_teimosia) == true) {
                            lvl_teimosia += 1;
                            cout << nome << " subiu de nivel em Teimosia!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 9:
                        break;
                }
            } else {
                cout << nome << " nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Bruxo : public Jogador {

    private:
        int imunidade = 13;
        int lvl_carisma = 0;
        int lvl_reflexos_relampagos;

    public:
        
        Bruxo(string nome_user, int hp_user, int nivel_geral_user, int lvl_brigar_user, int lvl_apostar_user, int lvl_forca_user, int lvl_coragem_user, int lvl_inteligencia_user, int lvl_reflexos_relampagos_user) : Jogador(nome_user, hp_user, nivel_geral_user, lvl_brigar_user, lvl_apostar_user, lvl_forca_user, lvl_coragem_user, lvl_inteligencia_user) {
            if (valida_atributo_construtor(lvl_reflexos_relampagos_user) == true) {
                this->lvl_reflexos_relampagos = lvl_reflexos_relampagos_user;
            } else { this->lvl_reflexos_relampagos = 0; }
        }

        
        Bruxo() : Jogador() {
            this->lvl_reflexos_relampagos = 0;
        }

        
        void inicializa_jogador() override {
            return;
        }

        
        void aumenta_nivel_habilidade() override {
            
            Jogador::aumenta_nivel_habilidade();

            int opcao = 0;

            if (qtd_pontos > 0) {
                while (true) {
                    cout << "6 - Upar Habilidade de: Reflexos Relampagos" << endl;
                    cout << "7 - Nao Upar Habilidade Especifica" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 6 and opcao <= 7) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 6:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_reflexos_relampagos) == true) {
                            lvl_reflexos_relampagos += 1;
                            cout << nome << " subiu de nivel em Reflexos Relampagos!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 7:
                        break;
                }
            } else {
                cout << nome << " nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Anao : public Jogador {

    private:
        int imunidade;
        int lvl_armadura;
        int lvl_deducao;

    public:
        
        Anao(string nome_user, int hp_user, int nivel_geral_user, int lvl_brigar_user, int lvl_apostar_user, int lvl_forca_user, int lvl_coragem_user, int lvl_inteligencia_user, int imunidade_user, int lvl_armadura_user, int lvl_deducao_user) : Jogador(nome_user, hp_user, nivel_geral_user, lvl_brigar_user, lvl_apostar_user, lvl_forca_user, lvl_coragem_user, lvl_inteligencia_user) {
            if (valida_atributo_construtor(imunidade_user) == true) {
                this->imunidade = imunidade_user;
            } else { this->imunidade = 0; }

            if (valida_atributo_construtor(lvl_armadura_user) == true) {
                this->lvl_armadura = lvl_armadura_user;
            } else { this->lvl_armadura = 0; }

            if (valida_atributo_construtor(lvl_deducao_user) == true) {
                this->lvl_deducao = lvl_deducao_user;
            } else { this->lvl_deducao = 0; }
        }

        
        Anao() : Jogador() {
            this->imunidade = 0;
            this->lvl_armadura = 0;
            this->lvl_deducao = 0;
        }

        
        void inicializa_jogador() override {
            return;
        }

        
        void aumenta_nivel_habilidade() override {
            
            Jogador::aumenta_nivel_habilidade();

            int opcao = 0;

            if (qtd_pontos > 0) {
                while (true) {
                    cout << "6 - Upar Habilidade de: Armaduras" << endl;
                    cout << "7 - Upar Habilidade de: Deducao" << endl;
                    cout << "8 - Nao Upar Habilidade Especifica" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 6 and opcao <= 8) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 6:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_armadura) == true) {
                            lvl_armadura += 1;
                            cout << nome << " subiu de nivel em Armadura!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 7:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_deducao) == true) {
                            lvl_deducao += 1;
                            cout << nome << " subiu de nivel em Deducao!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 8:
                        break;
                }
            } else {
                cout << nome << " nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Elfo : public Jogador {

    private:
        int imunidade;
        int lvl_artesanato;
        int lvl_arcos;
        int lvl_sintonia_natureza;

    public:
        
        Elfo(string nome_user, int hp_user, int nivel_geral_user, int lvl_brigar_user, int lvl_apostar_user, int lvl_forca_user, int lvl_coragem_user, int lvl_inteligencia_user, int imunidade_user, int lvl_artesanato_user, int lvl_arcos_user, int lvl_sintonia_natureza_user) : Jogador(nome_user, hp_user, nivel_geral_user, lvl_brigar_user, lvl_apostar_user, lvl_forca_user, lvl_coragem_user, lvl_inteligencia_user) {
            if (valida_atributo_construtor(imunidade_user) == true) {
                this->imunidade = imunidade_user;
            } else { this->imunidade = 0; }

            if (valida_atributo_construtor(lvl_artesanato_user) == true) {
                this->lvl_artesanato = lvl_artesanato_user;
            } else { this->lvl_artesanato = 0; }

            if (valida_atributo_construtor(lvl_arcos_user) == true) {
                this->lvl_arcos = lvl_arcos_user;
            } else { this->lvl_arcos = 0; }

            if (valida_atributo_construtor(lvl_sintonia_natureza_user) == true) {
                this->lvl_sintonia_natureza = lvl_sintonia_natureza_user;
            } else { this->lvl_sintonia_natureza = 0; }
        }

        
        Elfo() : Jogador() {
            this->imunidade = 0;
            this->lvl_artesanato = 0;
            this->lvl_arcos = 0;
            this->lvl_sintonia_natureza = 0;
        }

        
        void inicializa_jogador() override {
            return;
        }

        
        void aumenta_nivel_habilidade() override {
            
            Jogador::aumenta_nivel_habilidade();

            int opcao = 0;

            if (qtd_pontos > 0) {
                while (true) {
                    cout << "6 - Upar Habilidade de: Artesanato" << endl;
                    cout << "7 - Upar Habilidade de: Artilharia de Arcos" << endl;
                    cout << "8 - Upar Habilidade de: Sintonia da Natureza" << endl;
                    cout << "9 - Nao Upar Habilidade Especifica" << endl;
                    cout << "Digite uma opcao: ";
                    cin >> opcao;

                    if (opcao >= 6 and opcao <= 9) {
                        break;
                    } else { cout << "Digite uma opcao valida!" << endl; }
                }

                switch (opcao) {
                    case 6:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_artesanato) == true) {
                            lvl_artesanato += 1;
                            cout << nome << " subiu de nivel em Artesanato!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 7:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_arcos) == true) {
                            lvl_arcos += 1;
                            cout << nome << " subiu de nivel em Artilharia de Arcos!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 8:
                        qtd_pontos -= 1;
                        if (verifica_aumenta_lvl_habilidade(lvl_sintonia_natureza) == true) {
                            lvl_sintonia_natureza += 1;
                            cout << nome << " subiu de nivel em Sintonia da Natureza!" << endl;
                        } else { cout << "Voce ja esta no nivel maximo!" << endl; }
                        break;
                    case 9:
                        break;
                }
            } else {
                cout << nome << " nao tem pontos suficientes para subir de nivel" << endl;
            }
        }
};

class Item {

    protected:
        string nome;
        int valor;

        bool valida_atributo_construtor(int valor_user) {
            bool retorno = false;
            if (valor_user > 0) {
                retorno = true;
            }
            return retorno;
        }

    public:
        
        Item(string nome_user, int valor_user) {
            this->nome = nome_user;
            if (valida_atributo_construtor(valor_user) == true) {
                this->valor = valor_user;
            } else { this->valor = 0; }
        }

        
        Item() {
            this->nome = "Item";
            this->valor = 0;
        }

        
        virtual ~Item() {
            cout << "Item deletado" << endl;
        }

        virtual void usar() = 0;
};

class Arma : public Item {

    protected:
        int dano;

    public:
        
        Arma(string nome_user, int valor_user, int dano_user) : Item(nome_user, valor_user) {
            if (valida_atributo_construtor(dano_user) == true) {
                this->dano = dano_user;
            } else { this->dano = 0; }
        }

        
        Arma() : Item() {
            this->dano = 0;
        }

        
        virtual ~Arma() {
            cout << "Arma deletada" << endl;
        }

        
        virtual void usar() = 0;
};

class EspadaDeLaco : public Arma {

    public:
        
        EspadaDeLaco(string nome_user, int valor_user, int dano_user) : Arma(nome_user, valor_user, dano_user) {}

        
        EspadaDeLaco() : Arma() {
            this->nome = "Espada de Laco";
            this->valor = 150;
            this->dano = 10;
        }

        virtual ~EspadaDeLaco() {
            cout << "EspadaDeLaco deletada" << endl;
        }

        
        void usar() override {
            cout << "Usando " << nome << " - Dano: " << dano << endl;
        }
};

class Adaga : public Arma {

    public:
        
        Adaga(string nome_user, int valor_user, int dano_user) : Arma(nome_user, valor_user, dano_user) {}

        
        Adaga() : Arma() {
            this->nome = "Adaga";
            this->valor = 80;
            this->dano = 6;
        }

        virtual ~Adaga() {
            cout << "Adaga deletada" << endl;
        }

        
        void usar() override {
            cout << "Usando " << nome << " - Dano: " << dano << endl;
        }
};

class Machado : public Arma {

    public:
        
        Machado(string nome_user, int valor_user, int dano_user) : Arma(nome_user, valor_user, dano_user) {}

        
        Machado() : Arma() {
            this->nome = "Machado";
            this->valor = 120;
            this->dano = 14;
        }

        virtual ~Machado() {
            cout << "Machado deletado" << endl;
        }

        
        void usar() override {
            cout << "Usando " << nome << " - Dano: " << dano << endl;
        }
};

class Armadura : public Item {

    protected:
        int defesa;

    public:
        
        Armadura(string nome_user, int valor_user, int defesa_user) : Item(nome_user, valor_user) {
            if (valida_atributo_construtor(defesa_user) == true) {
                this->defesa = defesa_user;
            } else { this->defesa = 0; }
        }

        
        Armadura() : Item() {
            this->defesa = 0;
        }

        
        virtual ~Armadura() {
            cout << "Armadura deletada" << endl;
        }

        
        virtual void usar() = 0;
};

class ArmaduraDeMalha : public Armadura {

    public:
        
        ArmaduraDeMalha(string nome_user, int valor_user, int defesa_user) : Armadura(nome_user, valor_user, defesa_user) {}

        
        ArmaduraDeMalha() : Armadura() {
            this->nome = "Armadura de Malha";
            this->valor = 200;
            this->defesa = 8;
        }

        virtual ~ArmaduraDeMalha() {
            cout << "ArmaduraDeMalha deletada" << endl;
        }

        
        void usar() override {
            cout << "Equipando " << nome << " - Defesa: " << defesa << endl;
        }
};

class ColeteDeCouros : public Armadura {

    public:
        
        ColeteDeCouros(string nome_user, int valor_user, int defesa_user) : Armadura(nome_user, valor_user, defesa_user) {}

        
        ColeteDeCouros() : Armadura() {
            this->nome = "Colete de Couros";
            this->valor = 100;
            this->defesa = 4;
        }

        virtual ~ColeteDeCouros() {
            cout << "ColeteDeCouros deletado" << endl;
        }

        
        void usar() override {
            cout << "Equipando " << nome << " - Defesa: " << defesa << endl;
        }
};

class PlacaDeAco : public Armadura {

    public:
        
        PlacaDeAco(string nome_user, int valor_user, int defesa_user) : Armadura(nome_user, valor_user, defesa_user) {}

        
        PlacaDeAco() : Armadura() {
            this->nome = "Placa de Aco";
            this->valor = 350;
            this->defesa = 15;
        }

        virtual ~PlacaDeAco() {
            cout << "PlacaDeAco deletada" << endl;
        }

        
        void usar() override {
            cout << "Equipando " << nome << " - Defesa: " << defesa << endl;
        }
};

class Pocao : public Item {

    protected:
        int efeito;

    public:
        
        Pocao(string nome_user, int valor_user, int efeito_user) : Item(nome_user, valor_user) {
            this->efeito = efeito_user;
        }

        
        Pocao() : Item() {
            this->efeito = 0;
        }

        
        virtual ~Pocao() {
            cout << "Pocao deletada" << endl;
        }

        
        virtual void usar() = 0;
};

class PocaoDeCura : public Pocao {

    public:
        
        PocaoDeCura(string nome_user, int valor_user, int efeito_user) : Pocao(nome_user, valor_user, efeito_user) {}

        
        PocaoDeCura() : Pocao() {
            this->nome = "Pocao de Cura";
            this->valor = 50;
            this->efeito = 30;
        }

        virtual ~PocaoDeCura() {
            cout << "PocaoDeCura deletada" << endl;
        }

        
        void usar() override {
            cout << "Bebendo " << nome << " - Efeito: +" << efeito << " HP" << endl;
        }
};

class PocaoDeVeneno : public Pocao {

    public:
        
        PocaoDeVeneno(string nome_user, int valor_user, int efeito_user) : Pocao(nome_user, valor_user, efeito_user) {}

        
        PocaoDeVeneno() : Pocao() {
            this->nome = "Pocao de Veneno";
            this->valor = 70;
            this->efeito = -20;
        }

        virtual ~PocaoDeVeneno() {
            cout << "PocaoDeVeneno deletada" << endl;
        }

        
        void usar() override {
            cout << "Bebendo " << nome << " - Efeito: " << efeito << " HP" << endl;
        }
};

class PocaoDeFortaleza : public Pocao {

    public:
        
        PocaoDeFortaleza(string nome_user, int valor_user, int efeito_user) : Pocao(nome_user, valor_user, efeito_user) {}

        
        PocaoDeFortaleza() : Pocao() {
            this->nome = "Pocao de Fortaleza";
            this->valor = 90;
            this->efeito = 15;
        }

        virtual ~PocaoDeFortaleza() {
            cout << "PocaoDeFortaleza deletada" << endl;
        }

        
        void usar() override {
            cout << "Bebendo " << nome << " - Efeito: +" << efeito << " Forca temporaria" << endl;
        }
};

class ClasseRPG {

    protected:
        string nome;
        string raca;
        int hp;
        int ataque;
        int defesa;

        bool valida_atributo_construtor(int valor_user) {
            bool retorno = false;
            if (valor_user > 0) {
                retorno = true;
            }
            return retorno;
        }

    public:
        
        ClasseRPG(string nome_user, string raca_user, int hp_user, int ataque_user, int defesa_user) {
            this->nome = nome_user;
            this->raca = raca_user;

            if (valida_atributo_construtor(hp_user) == true) {
                this->hp = hp_user;
            } else { this->hp = 0; }

            if (valida_atributo_construtor(ataque_user) == true) {
                this->ataque = ataque_user;
            } else { this->ataque = 0; }

            if (valida_atributo_construtor(defesa_user) == true) {
                this->defesa = defesa_user;
            } else { this->defesa = 0; }
        }

        
        ClasseRPG() {
            this->nome = "Personagem";
            this->raca = "Desconhecida";
            this->hp = 100;
            this->ataque = 10;
            this->defesa = 5;
        }

        
        virtual ~ClasseRPG() {
            cout << "ClasseRPG deletada" << endl;
        }

        virtual void apresentar() = 0;
};

class Guerreiro : public ClasseRPG {

    private:
        int forca;

    public:
        
        Guerreiro(string nome_user, string raca_user, int hp_user, int ataque_user, int defesa_user, int forca_user) : ClasseRPG(nome_user, raca_user, hp_user, ataque_user, defesa_user) {
            if (valida_atributo_construtor(forca_user) == true) {
                this->forca = forca_user;
            } else { this->forca = 0; }
        }

        
        Guerreiro() : ClasseRPG() {
            this->forca = 18;
        }

        virtual ~Guerreiro() {
            cout << "Guerreiro deletado" << endl;
        }

        
        void apresentar() override {
            cout << "=== Guerreiro ===" << endl;
            cout << "Nome:   " << nome << endl;
            cout << "Raca:   " << raca << endl;
            cout << "HP:     " << hp << endl;
            cout << "Ataque: " << ataque << endl;
            cout << "Defesa: " << defesa << endl;
            cout << "Forca:  " << forca << endl;
        }
};

class MagoClasse : public ClasseRPG {

    private:
        int inteligencia;

    public:
        
        MagoClasse(string nome_user, string raca_user, int hp_user, int ataque_user, int defesa_user, int inteligencia_user) : ClasseRPG(nome_user, raca_user, hp_user, ataque_user, defesa_user) {
            if (valida_atributo_construtor(inteligencia_user) == true) {
                this->inteligencia = inteligencia_user;
            } else { this->inteligencia = 0; }
        }

        
        MagoClasse() : ClasseRPG() {
            this->hp = 80;
            this->ataque = 20;
            this->defesa = 5;
            this->inteligencia = 22;
        }

        virtual ~MagoClasse() {
            cout << "MagoClasse deletado" << endl;
        }

        
        void apresentar() override {
            cout << "=== Mago ===" << endl;
            cout << "Nome:         " << nome << endl;
            cout << "Raca:         " << raca << endl;
            cout << "HP:           " << hp << endl;
            cout << "Ataque:       " << ataque << endl;
            cout << "Defesa:       " << defesa << endl;
            cout << "Inteligencia: " << inteligencia << endl;
        }
};

class Ladrao : public ClasseRPG {

    private:
        int agilidade;

    public:
        
        Ladrao(string nome_user, string raca_user, int hp_user, int ataque_user, int defesa_user, int agilidade_user) : ClasseRPG(nome_user, raca_user, hp_user, ataque_user, defesa_user) {
            if (valida_atributo_construtor(agilidade_user) == true) {
                this->agilidade = agilidade_user;
            } else { this->agilidade = 0; }
        }

        
        Ladrao() : ClasseRPG() {
            this->hp = 100;
            this->ataque = 13;
            this->defesa = 8;
            this->agilidade = 20;
        }

        virtual ~Ladrao() {
            cout << "Ladrao deletado" << endl;
        }

        
        void apresentar() override {
            cout << "=== Ladrao ===" << endl;
            cout << "Nome:      " << nome << endl;
            cout << "Raca:      " << raca << endl;
            cout << "HP:        " << hp << endl;
            cout << "Ataque:    " << ataque << endl;
            cout << "Defesa:    " << defesa << endl;
            cout << "Agilidade: " << agilidade << endl;
        }
};

class ItemFactory {

    public:
        static Arma* criar_arma(int tipo) {
            Arma* arma = nullptr;

            switch (tipo) {
                case 1:
                    arma = new EspadaDeLaco();
                    break;
                case 2:
                    arma = new Adaga();
                    break;
                case 3:
                    arma = new Machado();
                    break;
                default:
                    arma = new EspadaDeLaco();
                    break;
            }

            return arma;
        }

        static Armadura* criar_armadura(int tipo) {
            Armadura* armadura = nullptr;

            switch (tipo) {
                case 1:
                    armadura = new ArmaduraDeMalha();
                    break;
                case 2:
                    armadura = new ColeteDeCouros();
                    break;
                case 3:
                    armadura = new PlacaDeAco();
                    break;
                default:
                    armadura = new ArmaduraDeMalha();
                    break;
            }

            return armadura;
        }

        static Pocao* criar_pocao(int tipo) {
            Pocao* pocao = nullptr;

            switch (tipo) {
                case 1:
                    pocao = new PocaoDeCura();
                    break;
                case 2:
                    pocao = new PocaoDeVeneno();
                    break;
                case 3:
                    pocao = new PocaoDeFortaleza();
                    break;
                default:
                    pocao = new PocaoDeCura();
                    break;
            }

            return pocao;
        }
};

class JogadorFactory {

    public:
        static ClasseRPG* criar_guerreiro(string nome_user, string raca_user) {
            ClasseRPG* personagem = nullptr;
            personagem = new Guerreiro(nome_user, raca_user, 150, 15, 12, 18);
            return personagem;
        }

        static ClasseRPG* criar_mago(string nome_user, string raca_user) {
            ClasseRPG* personagem = nullptr;
            personagem = new MagoClasse(nome_user, raca_user, 80, 20, 5, 22);
            return personagem;
        }

        static ClasseRPG* criar_ladrao(string nome_user, string raca_user) {
            ClasseRPG* personagem = nullptr;
            personagem = new Ladrao(nome_user, raca_user, 100, 13, 8, 20);
            return personagem;
        }
};

class RacaFactory {

    public:
        static Jogador* criar_jogador(int tipo, string nome_user) {
            Jogador* jogador = nullptr;

            switch (tipo) {
                case 1:
                    jogador = new Humano(nome_user, 100, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0);
                    break;
                case 2:
                    jogador = new Bruxo(nome_user, 100, 200, 0, 0, 0, 0, 0, 0);
                    break;
                case 3:
                    jogador = new Anao(nome_user, 100, 200, 0, 0, 0, 0, 0, 0, 0, 0);
                    break;
                case 4:
                    jogador = new Elfo(nome_user, 100, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0);
                    break;
                default:
                    jogador = new Humano(nome_user, 100, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0);
                    break;
            }

            return jogador;
        }
};

class ProfissaoFactory {

    public:
        static Profissao* criar_profissao(int tipo) {
            Profissao* profissao = nullptr;

            switch (tipo) {
                case 1:
                    profissao = new Mago();
                    break;
                case 2:
                    profissao = new Bardo();
                    break;
                case 3:
                    profissao = new Artesao();
                    break;
                case 4:
                    profissao = new Criminoso();
                    break;
                case 5:
                    profissao = new Doutor();
                    break;
                case 6:
                    profissao = new Cavaleiro();
                    break;
                case 7:
                    profissao = new Comerciante();
                    break;
                case 8:
                    profissao = new Sacerdote();
                    break;
                case 9:
                    profissao = new Desempregado();
                    break;
                default:
                    profissao = new Desempregado();
                    break;
            }

            return profissao;
        }
};

int menu_raca() {
    int opcao = 0;

    while (true) {
        cout << "========================================" << endl;
        cout << "       Escolha a raca do personagem     " << endl;
        cout << "========================================" << endl;
        cout << "1 - Humano" << endl;
        cout << "2 - Bruxo" << endl;
        cout << "3 - Anao" << endl;
        cout << "4 - Elfo" << endl;
        cout << "Digite uma opcao: ";
        cin >> opcao;

        if (opcao >= 1 and opcao <= 4) {
            break;
        } else { cout << "Digite uma opcao valida!" << endl; }
    }

    return opcao;
}

int menu_profissao() {
    int opcao = 0;

    while (true) {
        cout << "========================================" << endl;
        cout << "     Escolha a profissao do personagem  " << endl;
        cout << "========================================" << endl;
        cout << "1 - Mago" << endl;
        cout << "2 - Bardo" << endl;
        cout << "3 - Artesao" << endl;
        cout << "4 - Criminoso" << endl;
        cout << "5 - Doutor" << endl;
        cout << "6 - Cavaleiro" << endl;
        cout << "7 - Comerciante" << endl;
        cout << "8 - Sacerdote" << endl;
        cout << "9 - Desempregado" << endl;
        cout << "Digite uma opcao: ";
        cin >> opcao;

        if (opcao >= 1 and opcao <= 9) {
            break;
        } else { cout << "Digite uma opcao valida!" << endl; }
    }

    return opcao;
}

int menu_classe_rpg() {
    int opcao = 0;

    while (true) {
        cout << "========================================" << endl;
        cout << "     Escolha a classe RPG (arquetipo)   " << endl;
        cout << "========================================" << endl;
        cout << "1 - Guerreiro" << endl;
        cout << "2 - Mago" << endl;
        cout << "3 - Ladrao" << endl;
        cout << "Digite uma opcao: ";
        cin >> opcao;

        if (opcao >= 1 and opcao <= 3) {
            break;
        } else { cout << "Digite uma opcao valida!" << endl; }
    }

    return opcao;
}

int menu_criar_arma() {
    int opcao = 0;

    while (true) {
        cout << "========================================" << endl;
        cout << "          Escolha uma arma              " << endl;
        cout << "========================================" << endl;
        cout << "1 - Espada de Laco  (Dano: 10)" << endl;
        cout << "2 - Adaga           (Dano:  6)" << endl;
        cout << "3 - Machado         (Dano: 14)" << endl;
        cout << "Digite uma opcao: ";
        cin >> opcao;

        if (opcao >= 1 and opcao <= 3) {
            break;
        } else { cout << "Digite uma opcao valida!" << endl; }
    }

    return opcao;
}

int menu_criar_armadura() {
    int opcao = 0;

    while (true) {
        cout << "========================================" << endl;
        cout << "          Escolha uma armadura          " << endl;
        cout << "========================================" << endl;
        cout << "1 - Armadura de Malha  (Defesa:  8)" << endl;
        cout << "2 - Colete de Couros   (Defesa:  4)" << endl;
        cout << "3 - Placa de Aco       (Defesa: 15)" << endl;
        cout << "Digite uma opcao: ";
        cin >> opcao;

        if (opcao >= 1 and opcao <= 3) {
            break;
        } else { cout << "Digite uma opcao valida!" << endl; }
    }

    return opcao;
}

int menu_criar_pocao() {
    int opcao = 0;

    while (true) {
        cout << "========================================" << endl;
        cout << "           Escolha uma pocao            " << endl;
        cout << "========================================" << endl;
        cout << "1 - Pocao de Cura       (Efeito: +30 HP)" << endl;
        cout << "2 - Pocao de Veneno     (Efeito: -20 HP)" << endl;
        cout << "3 - Pocao de Fortaleza  (Efeito: +15 Forca)" << endl;
        cout << "Digite uma opcao: ";
        cin >> opcao;

        if (opcao >= 1 and opcao <= 3) {
            break;
        } else { cout << "Digite uma opcao valida!" << endl; }
    }

    return opcao;
}

string get_nome_raca(int tipo) {
    string nome_raca = "";

    switch (tipo) {
        case 1:
            nome_raca = "Humano";
            break;
        case 2:
            nome_raca = "Bruxo";
            break;
        case 3:
            nome_raca = "Anao";
            break;
        case 4:
            nome_raca = "Elfo";
            break;
        default:
            nome_raca = "Desconhecida";
            break;
    }

    return nome_raca;
}

int main() {

    cout << "========================================" << endl;
    cout << "     RPG - The Witcher: Entregavel 08   " << endl;
    cout << "========================================" << endl;
    cout << "Digite o nome do personagem: ";
    string nome;
    cin >> nome;

    
    int opcao_raca = menu_raca();
    Jogador* jogador = RacaFactory::criar_jogador(opcao_raca, nome);

    
    int opcao_profissao = menu_profissao();
    Profissao* profissao = ProfissaoFactory::criar_profissao(opcao_profissao);
    jogador->set_profissao(profissao);

    
    jogador->aumenta_nivel_habilidade();

    
    int opcao_classe = menu_classe_rpg();
    string nome_raca = get_nome_raca(opcao_raca);
    ClasseRPG* classe_rpg = nullptr;

    switch (opcao_classe) {
        case 1:
            classe_rpg = JogadorFactory::criar_guerreiro(nome, nome_raca);
            break;
        case 2:
            classe_rpg = JogadorFactory::criar_mago(nome, nome_raca);
            break;
        case 3:
            classe_rpg = JogadorFactory::criar_ladrao(nome, nome_raca);
            break;
    }

    
    int opcao_arma = menu_criar_arma();
    Arma* arma = ItemFactory::criar_arma(opcao_arma);

    int opcao_armadura = menu_criar_armadura();
    Armadura* armadura = ItemFactory::criar_armadura(opcao_armadura);

    int opcao_pocao = menu_criar_pocao();
    Pocao* pocao = ItemFactory::criar_pocao(opcao_pocao);

    
    cout << endl;
    cout << "========================================" << endl;
    cout << "        Personagem Criado com Sucesso!  " << endl;
    cout << "========================================" << endl;
    classe_rpg->apresentar();

    cout << endl;
    cout << "--- Equipamentos e Itens ---" << endl;
    arma->usar();
    armadura->usar();
    pocao->usar();

    
    cout << endl;
    cout << "========================================" << endl;
    cout << "         Encerrando o programa...       " << endl;
    cout << "========================================" << endl;

    delete pocao;
    delete armadura;
    delete arma;
    delete classe_rpg;
    delete profissao;
    delete jogador;

    return 0;
}
