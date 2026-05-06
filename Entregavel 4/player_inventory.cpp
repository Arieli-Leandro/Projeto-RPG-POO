#include <string.h>
#include <iostream>
using namespace std;

//Fazer a superclasse para upar os níves de profissão e os do personagem

/* Tabela de níveis máximos e mínimos de acordo com o livro */
/* 
1-2 -> Inepto
3-4 -> Trivial
5-6 -> Competente
7-8 -> Heróico
9-10 -> Incrivel
11-12 -> Lendário
13 -> Super heróico
*/

class Profissao{

    protected:
        int qtd_pontos_profissao = 0; // A cada 10 pontos de profissão, vc pode subir de nível em alguma habilidade específica de profissao
        int nivel_geral_profissao;

        bool valida_atributo_construtor(int valor){
            bool retorno = false;

            if(valor > 0){
                retorno = true;
            }

            return retorno;

        };

        bool transforma_pontos_experiencia(){
            while(nivel_geral_profissao >= 10){
                nivel_geral_profissao = nivel_geral_profissao -10;
                qtd_pontos_profissao += 1;
            }

        };

    public:

        //Construtor tipo 1 - Usuário passou todos os Parâmetros
        Profissao(int nivel_geral_profissao_user){
            if(valida_atributo_construtor(nivel_geral_profissao_user) == true){
                this->nivel_geral_profissao = nivel_geral_profissao_user;
            }else{this->nivel_geral_profissao = 0;}
        }

        //Construtor tipo 2 - Usuário não passou nenhum parâmetro
        Profissao(){
            this->nivel_geral_profissao = 0;
        }

        //Destrutor virtual
        virtual ~Profissao(){

            cout << "Profissao deletada" << endl;

        }
        
        virtual void inicializa_profissao() = 0;

};

class Mago: public Profissao{

    private:
        int lvl_criar_ritual;
        int lvl_lancar_feitico;
        int lvl_educacao;
        int lvl_resistir_magia;

    public: 
        //fazer o construtor
        //Construtor tipo 1 - Usuário passou tds os parâmetros
        Mago(int lvl_criar_ritual_user, int lvl_lancar_feitico_user, int lvl_educacao_user, int lvl_resistir_magia_user, int nivel_geral_user):Profissao(nivel_geral_profissao){

            if(valida_atributo_construtor(lvl_criar_ritual_user) == true){
                this->lvl_criar_ritual = lvl_criar_ritual_user;
            }else{this->lvl_criar_ritual = 0;}

            if(valida_atributo_construtor(lvl_lancar_feitico_user) == true){
                this->lvl_lancar_feitico = lvl_lancar_feitico_user;
            }else{this->lvl_lancar_feitico = 0;}

            if(valida_atributo_construtor(lvl_educacao_user) == true){
                this->lvl_educacao = lvl_educacao_user;
            }else{this->lvl_educacao = 0;}

            if(valida_atributo_construtor(lvl_resistir_magia_user) == true){
                this->lvl_resistir_magia = lvl_resistir_magia_user;
            }else{this->lvl_resistir_magia = 0;}

        }

        //Constrtutor tipo 2 - Usuário nn passou nenhum parâmetro
        Mago():Profissao(){
            this->lvl_criar_ritual = 0;
            this->lvl_educacao = 0;
            this->lvl_lancar_feitico = 0;
            this->lvl_resistir_magia = 0;
        }

        //polimorfismo
        void inicializa_profissao() override{
            return;
        }
};

class Bardo: public Profissao{

    private:
        int lvl_etiqueta_social;
        int lvl_ludibriar;
        int lvl_sabedoria_das_ruas;
    public: 
        Bardo(int lvl_etiqueta_social_user, int lvl_ludibriar_user, int lvl_sabedoria_das_ruas_user, int nivel_geral_user):Profissao(nivel_geral_profissao){

            if(valida_atributo_construtor(lvl_etiqueta_social_user) == true){
                this->lvl_etiqueta_social = lvl_etiqueta_social_user;
            }else{this->lvl_etiqueta_social = 0;}

            if(valida_atributo_construtor(lvl_ludibriar_user) == true){
                this->lvl_ludibriar = lvl_ludibriar_user;
            }else{this->lvl_ludibriar = 0;}

            if(valida_atributo_construtor(lvl_sabedoria_das_ruas_user) == true){
                this->lvl_sabedoria_das_ruas = lvl_sabedoria_das_ruas_user;
            }else{this->lvl_sabedoria_das_ruas = 0;}

        }

        //Constrtutor tipo 2 - Usuário nn passou nenhum parâmetro
        Bardo():Profissao(){
            this->lvl_etiqueta_social = 0;
            this->lvl_ludibriar = 0;
            this->lvl_sabedoria_das_ruas = 0;
        }        

        //polimorfismo
        void inicializa_profissao() override{
            return;
        }
};

class Artesao: public Profissao{

    private:
        int lvl_educacao;
        int lvl_criacao;
        int lvl_negociacao;
        int lvl_fisico;

    public: 
        Artesao(int lvl_educacao_user, int lvl_criacao_user, int lvl_negociacao_user, int lvl_fisico_user, int nivel_geral_user):Profissao(nivel_geral_profissao){

            if(valida_atributo_construtor(lvl_educacao_user) == true){
                this->lvl_educacao = lvl_educacao_user;
            }else{this->lvl_educacao = 0;}

            if(valida_atributo_construtor(lvl_criacao_user) == true){
                this->lvl_criacao = lvl_criacao_user;
            }else{this->lvl_criacao = 0;}

            if(valida_atributo_construtor(lvl_negociacao_user) == true){
                this->lvl_negociacao = lvl_negociacao_user;
            }else{this->lvl_negociacao = 0;}

            if(valida_atributo_construtor(lvl_fisico_user) == true){
                this->lvl_fisico = lvl_fisico_user;
            }else{this->lvl_fisico = 0;}

        }

        //Constrtutor tipo 2 - Usuário nn passou nenhum parâmetro
        Artesao():Profissao(){
            this->lvl_educacao = 0;
            this->lvl_criacao = 0;
            this->lvl_negociacao = 0;
            this->lvl_fisico = 0;
        }

        //polimorfismo
        void inicializa_profissao() override{
            return;
        }
};

class Criminoso: public Profissao{

    private:
        int lvl_arrombar_fechaduras;
        int lvl_falsificacao;
        int lvl_atletismo;
        int lvl_sabedoria_das_ruas;

    public: 
        //fazer o construtor
        Criminoso(int lvl_arrombar_fechaduras_user, int lvl_falsificacao_user, int lvl_atletismo_user, int lvl_sabedoria_das_ruas_user, int nivel_geral_user):Profissao(nivel_geral_profissao){

            if(valida_atributo_construtor(lvl_arrombar_fechaduras_user) == true){
                this->lvl_arrombar_fechaduras = lvl_arrombar_fechaduras_user;
            }else{this->lvl_arrombar_fechaduras = 0;}

            if(valida_atributo_construtor(lvl_falsificacao_user) == true){
                this->lvl_falsificacao = lvl_falsificacao_user;
            }else{this->lvl_falsificacao = 0;}

            if(valida_atributo_construtor(lvl_atletismo_user) == true){
                this->lvl_atletismo = lvl_atletismo_user;
            }else{this->lvl_atletismo = 0;}

            if(valida_atributo_construtor(lvl_sabedoria_das_ruas_user) == true){
                this->lvl_sabedoria_das_ruas = lvl_sabedoria_das_ruas_user;
            }else{this->lvl_sabedoria_das_ruas = 0;}

        }

        //Constrtutor tipo 2 - Usuário nn passou nenhum parâmetro
        Criminoso():Profissao(){
            this->lvl_arrombar_fechaduras = 0;
            this->lvl_falsificacao = 0;
            this->lvl_atletismo = 0;
            this->lvl_sabedoria_das_ruas = 0;
        }

        //polimorfismo
        void inicializa_profissao() override{
            return;
        }
};

class Doutor: public Profissao{

    private:
        int lvl_carisma;
        int lvl_educacao;
        int lvl_coragem;
        int lvl_alquimia;

    public: 
        Doutor(int lvl_carisma_user, int lvl_educacao_user, int lvl_coragem_user, int lvl_alquimia_user, int nivel_geral_user):Profissao(nivel_geral_profissao){

            if(valida_atributo_construtor(lvl_carisma_user) == true){
                this->lvl_carisma = lvl_carisma_user;
            }else{this->lvl_carisma = 0;}

            if(valida_atributo_construtor(lvl_educacao_user) == true){
                this->lvl_educacao = lvl_educacao_user;
            }else{this->lvl_educacao = 0;}

            if(valida_atributo_construtor(lvl_coragem_user) == true){
                this->lvl_coragem = lvl_coragem_user;
            }else{this->lvl_coragem = 0;}

            if(valida_atributo_construtor(lvl_alquimia_user) == true){
                this->lvl_alquimia = lvl_alquimia_user;
            }else{this->lvl_alquimia = 0;}

        }

        //Constrtutor tipo 2 - Usuário nn passou nenhum parâmetro
        Doutor():Profissao(){
            this->lvl_educacao = 0;
            this->lvl_coragem = 0;
            this->lvl_coragem = 0;
            this->lvl_alquimia = 0;
        }

        //polimorfismo
        void inicializa_profissao() override{
            return;
        }
};

class Cavaleiro: public Profissao{

    private:
        int lvl_coragem;
        int lvl_intimidacao;
        int lvl_sobrevivencia;
        int lvl_esquivar;

    public: 
        Cavaleiro(int lvl_coragem_user, int lvl_intimidacao_user, int lvl_sobrevivencia_user, int lvl_esquivar_user, int nivel_geral_user):Profissao(nivel_geral_profissao){

            if(valida_atributo_construtor(lvl_coragem_user) == true){
                this->lvl_coragem = lvl_coragem_user;
            }else{this->lvl_coragem = 0;}

            if(valida_atributo_construtor(lvl_intimidacao_user) == true){
                this->lvl_intimidacao = lvl_intimidacao_user;
            }else{this->lvl_intimidacao = 0;}

            if(valida_atributo_construtor(lvl_sobrevivencia_user) == true){
                this->lvl_sobrevivencia = lvl_sobrevivencia_user;
            }else{this->lvl_sobrevivencia = 0;}

            if(valida_atributo_construtor(lvl_esquivar_user) == true){
                this->lvl_esquivar = lvl_esquivar_user;
            }else{this->lvl_esquivar = 0;}
            
        }

        //Constrtutor tipo 2 - Usuário nn passou nenhum parâmetro
        Cavaleiro():Profissao(){
            this->lvl_coragem = 0;
            this->lvl_intimidacao = 0;
            this->lvl_sobrevivencia = 0;
            this->lvl_esquivar = 0;
        }

        //polimorfismo
        void inicializa_profissao() override{
            return;
        }


};

class Comerciante: public Profissao{

    private:
        int lvl_carisma;
        int lvl_educacao;
        int lvl_negocios;
        int lvl_persuasao;

    public: 
        //Construtor tipo 1 - Usuário passou todos os Parâmetros
        Comerciante(int lvl_carisma_user, int lvl_educacao_user, int lvl_negocios_user, int lvl_persuasao_user,int nivel_geral_user):Profissao(nivel_geral_profissao){

            if(valida_atributo_construtor(lvl_carisma_user) == true){
                this->lvl_carisma = lvl_carisma_user;
            }else{this->lvl_carisma = 0;}

            if(valida_atributo_construtor(lvl_educacao_user) == true){
                this->lvl_educacao = lvl_educacao_user;
            }else{this->lvl_educacao = 0;}

            if(valida_atributo_construtor(lvl_negocios_user) == true){
                this->lvl_negocios = lvl_negocios_user;
            }else{this->lvl_negocios = 0;}

            if(valida_atributo_construtor(lvl_persuasao_user) == true){
                this->lvl_persuasao = lvl_persuasao_user;
            }else{this->lvl_persuasao = 0;}

        }

        //Constrtutor tipo 2 - Usuário nn passou nenhum parâmetro
        Comerciante():Profissao(){
            this->lvl_carisma = 0;
            this->lvl_educacao = 0;
            this->lvl_negocios = 0;
            this->lvl_persuasao = 0;
        }

        //polimorfismo
        void inicializa_profissao() override{
            return;
        }
};

class Sacerdote: public Profissao{

    private:
        int lvl_criar_ritual;
        int lvl_coragem;
        int lvl_ensinar;
        int lvl_lancar_feitico;

    public: 
        //Construtor tipo 1 - Usuário passou todos os Parâmetros
        Sacerdote(int lvl_criar_ritual_user, int lvl_coragem_user, int lvl_ensinar_user, int lvl_lancar_feitico_user, int nivel_geral_user):Profissao(nivel_geral_profissao){

            if(valida_atributo_construtor(lvl_criar_ritual_user) == true){
                this->lvl_criar_ritual = lvl_criar_ritual_user;
            }else{this->lvl_criar_ritual = 0;}

            if(valida_atributo_construtor(lvl_coragem_user) == true){
                this->lvl_coragem = lvl_coragem_user;
            }else{this->lvl_coragem = 0;}

            if(valida_atributo_construtor(lvl_ensinar_user) == true){
                this->lvl_ensinar = lvl_ensinar_user;
            }else{this->lvl_ensinar = 0;}

            if(valida_atributo_construtor(lvl_lancar_feitico_user) == true){
                this->lvl_lancar_feitico = lvl_lancar_feitico_user;
            }else{this->lvl_lancar_feitico = 0;}

        }

        //Constrtutor tipo 2 - Usuário nn passou nenhum parâmetro
        Sacerdote():Profissao(){
            this->lvl_criar_ritual = 0;
            this->lvl_coragem = 0;
            this->lvl_ensinar = 0;
            this->lvl_lancar_feitico = 0;
        }

        //polimorfismo
        void inicializa_profissao() override{
            return;
        }


};

class Desempregado: public Profissao{

    private:
        int lvl_artesanato;
        int lvl_sobrevivencia;
        int lvl_consciencia;

    public: 
        //Construtor tipo 1 - Usuário passou todos os Parâmetros
        Desempregado(int lvl_artesanato_user, int lvl_sobrevivencia_user, int lvl_consciencia_user, int nivel_geral_user):Profissao(nivel_geral_profissao){

            if(valida_atributo_construtor(lvl_artesanato_user) == true){
                this->lvl_artesanato = lvl_artesanato_user;
            }else{this->lvl_artesanato = 0;}

            if(valida_atributo_construtor(lvl_sobrevivencia_user) == true){
                this->lvl_sobrevivencia = lvl_sobrevivencia_user;
            }else{this->lvl_sobrevivencia = 0;}

            if(valida_atributo_construtor(lvl_consciencia_user) == true){
                this->lvl_consciencia = lvl_consciencia_user;
            }else{this->lvl_consciencia = 0;}

        }

        //Constrtutor tipo 2 - Usuário nn passou nenhum parâmetro
        Desempregado():Profissao(){
            this->lvl_artesanato = 0;
            this->lvl_sobrevivencia = 0;
            this->lvl_consciencia = 0;
        }

        //polimorfismo
        void inicializa_profissao() override{
            return;
        }
    
};

// Tornar ela abstrata dps
class Jogador{

    protected:
        Profissao *profissao_jogador;
        string nome;
        int hp;
        int hp_maximo = 100;
        int nivel_geral;
        int qtd_pontos = 0; //A cada 10 pontos você pode evoluir uma habilidade do seu personagem
        int lvl_brigar;
        int lvl_apostar;
        int lvl_forca;
        int lvl_coragem;
        int lvl_inteligencia;

        bool valida_atributo_construtor(int valor){
            bool retorno = false;

            if(valor > 0){
                retorno = true;
            }

            return retorno;

        };

        bool transforma_pontos_experiencia(){
            while(nivel_geral >= 10){
                nivel_geral = nivel_geral -10;
                qtd_pontos += 1;
            }

        };

    public:
        //Construtor tipo 1 - Usuário passou todos os Parâmetros
        Jogador(string nome_user, int hp_user, int nivel_geral_user, int lvl_brigar_user, int lvl_apostar_user, int lvl_forca_user, int lvl_coragem_user, int lvl_inteligencia_user){
            this->nome = nome_user;
            
            if(valida_atributo_construtor(hp_user) == true){
                this->hp = hp_user;
            }else{this->hp = 0;}

            if(valida_atributo_construtor(nivel_geral_user) == true){
                this->nivel_geral = nivel_geral_user;
            }else{this->nivel_geral = 0;}

            if(valida_atributo_construtor(lvl_brigar_user) == true){
                this->lvl_brigar = lvl_brigar_user;
            }else{this->lvl_brigar = 0;}

            if(valida_atributo_construtor(lvl_apostar_user) == true){
                this->lvl_apostar = lvl_apostar_user;
            }else{this->lvl_apostar = 0;}

            if(valida_atributo_construtor(lvl_forca_user) == true){
                this->lvl_forca = lvl_forca_user;
            }else{this->lvl_forca = 0;}

            if(valida_atributo_construtor(lvl_coragem_user) == true){
                this->lvl_coragem = lvl_coragem_user;
            }else{this->lvl_coragem = 0;}

            if(valida_atributo_construtor(lvl_inteligencia_user) == true){
                this->lvl_inteligencia = lvl_inteligencia_user;
            }else{this->lvl_inteligencia = 0;}

        }

        //Construtor tipo 2 - Usuário não passou nenhum parâmetro
        Jogador(){
            this->nome = "Guest";
            this->hp = 100;
            this->nivel_geral = 0;
            this->lvl_apostar = 0;
            this->lvl_brigar = 0;
            this->lvl_coragem = 0;
            this->lvl_forca = 0;
            this->lvl_inteligencia = 0;
        }

        //Destrutor virtual
        virtual ~Jogador(){
            cout << "Removendo os dados do jogador:" << nome << endl;
        }

        //Método da classe mãe
        void aumenta_nivel_habilidade(){

            int opcao = 0;

            if(qtd_pontos > 0){

                while(true){

                    cout << "1 - Upar Habilidade dê: Aposta" << endl;
                    cout << "2 - Upar Habilidade dê: Brigar" << endl;
                    cout << "3 - Upar Habilidade dê: Coragem" << endl;
                    cout << "4 - Upar Habilidade dê: Forca" << endl;
                    cout << "5 - Upar Habilidade dê: Inteligencia" << endl;
                    cout << "Digite uma opcao: " << endl;
                    cin >> opcao;

                    if(opcao >=1 and opcao <=5){
                        break;
                    }else{cout << "Digite uma opcao valida!" << endl;}
                }

                switch(opcao){

                    case 1: //Aposta
                        qtd_pontos -= 1;
                        lvl_apostar += 1;
                        cout << nome << "subiu de nivel em Aposta!" << endl;
                        break;

                    case 2: //Brigar
                        qtd_pontos -= 1;
                        lvl_brigar += 1;
                        cout << nome << "subiu de nivel em Brigar!" << endl;
                        break;

                    case 3: //Coragem
                        qtd_pontos -= 1;
                        lvl_coragem += 1;
                        cout << nome << "subiu de nivel em Coragem!" << endl;
                        break;

                    case 4: //Forca
                        qtd_pontos -= 1;
                        lvl_forca += 1;
                        cout << nome << "subiu de nivel em Forca!" << endl;
                        break;

                    case 5: //Inteligencia
                        qtd_pontos -= 1;
                        lvl_inteligencia += 1;
                        cout << nome << "subiu de nivel Inteligencia!" << endl;
                        break;

                }

                
                

            }else{

                cout << nome << "Nao tem pontos suficientes para subir de nivel" << endl;

            }

            

        }

        virtual void inicializa_jogador() = 0;

};

class Humano: public Jogador{

    private:
        int imunidade;
        int lvl_seducao;
        int lvl_persuasao;
        int teimosia;

    public:
        // Construtor tipo 1 - Usuário passou tds os parâmetros
        Humano(string nome_user, int hp_user, int nivel_geral_user, int lvl_brigar_user, int lvl_apostar_user, int lvl_forca_user, int lvl_coragem_user, int lvl_inteligencia_user, int imunidade_user, int lvl_seducao_user, int lvl_persuasao_user, int teimosia_user):Jogador(nome_user, hp_user, nivel_geral_user, lvl_brigar_user, lvl_apostar_user, lvl_forca_user, lvl_coragem_user, lvl_inteligencia_user){
            if(valida_atributo_construtor(imunidade_user) == true){
                this->imunidade = imunidade_user;
            }else{this->imunidade = 0;}

            if(valida_atributo_construtor(lvl_seducao_user) == true){
                this->lvl_seducao = lvl_seducao_user;
            }else{this->lvl_seducao = 0;}

            if(valida_atributo_construtor(lvl_persuasao_user) == true){
                this->lvl_persuasao = lvl_persuasao_user;
            }else{this->lvl_persuasao = 0;}

            if(valida_atributo_construtor(teimosia_user) == true){
                this->teimosia = teimosia_user;
            }else{this->teimosia = 0;}
        }

        // Construtor tipo 2 - Usuário não passou nenhum parâmetro
        Humano():Jogador(){
            this->imunidade = 0;
            this->lvl_seducao = 0;
            this->lvl_persuasao = 0;
            this->teimosia = 0;
        }

        //polimorfismo
        void inicializa_jogador() override{
            return;
        }


};

class Bruxo: public Jogador{

    private:
        int imunidade = 13; //Bruxo vai ter o nível máximo de imunidade
        int lvl_carisma = 0; //De acordo com o livro, os Bruxos tem um carisma 0 que é o nível mais baixo possível
        int lvl_reflexos_relampagos;

    public: 
        // Construtor tipo 1 - Usuário passou tds os parâmetros
        Bruxo(string nome_user, int hp_user, int nivel_geral_user, int lvl_brigar_user, int lvl_apostar_user, int lvl_forca_user, int lvl_coragem_user, int lvl_inteligencia_user, int lvl_reflexos_relampagos_user):Jogador(nome_user, hp_user, nivel_geral_user, lvl_brigar_user, lvl_apostar_user, lvl_forca_user, lvl_coragem_user, lvl_inteligencia_user){
            if(valida_atributo_construtor(lvl_reflexos_relampagos_user) == true){
                this->lvl_reflexos_relampagos = lvl_reflexos_relampagos_user;
            }else{this->lvl_reflexos_relampagos = 0;}
        }

        // Construtor tipo 2 - Usuário não passou nenhum parâmetro
        Bruxo():Jogador(){
            this->lvl_reflexos_relampagos = 0;
        }
        

        //polimorfismo
        void inicializa_jogador() override{
            return;
        }


};

class Anao: public Jogador{

    private:
        int imunidade;
        int lvl_armadura;
        int lvl_deducao;
    public:
        // Construtor tipo 1 - Usuário passou tds os parâmetros
        Anao(string nome_user, int hp_user, int nivel_geral_user, int lvl_brigar_user, int lvl_apostar_user, int lvl_forca_user, int lvl_coragem_user, int lvl_inteligencia_user, int imunidade_user, int lvl_armadura_user, int lvl_deducao_user):Jogador(nome_user, hp_user, nivel_geral_user, lvl_brigar_user, lvl_apostar_user, lvl_forca_user, lvl_coragem_user, lvl_inteligencia_user){
            if(valida_atributo_construtor(imunidade_user) == true){
                this->imunidade = imunidade_user;
            }else{this->imunidade = 0;}

            if(valida_atributo_construtor(lvl_armadura_user) == true){
                this->lvl_armadura = lvl_armadura_user;
            }else{this->lvl_armadura = 0;}

            if(valida_atributo_construtor(lvl_deducao_user) == true){
                this->lvl_deducao = lvl_deducao_user;
            }else{this->lvl_deducao = 0;}
        }

        // Construtor tipo 2 - Usuário não passou nenhum parâmetro
        Anao():Jogador(){
            this->imunidade = 0;
            this->lvl_armadura = 0;
            this->lvl_deducao = 0;
        }

        //polimorfismo
        void inicializa_jogador() override{
            return;
        }



};

class Elfo: public Jogador{

    private:
        int imunidade;
        int lvl_artesanato;
        int lvl_arcos;
        int lvl_sintonia_natureza;

    public:
        // Construtor tipo 1 - Usuário passou tds os parâmetros
        Elfo(string nome_user, int hp_user, int nivel_geral_user, int lvl_brigar_user, int lvl_apostar_user, int lvl_forca_user, int lvl_coragem_user, int lvl_inteligencia_user, int imunidade_user, int lvl_artesanato_user, int lvl_arcos_user, int lvl_sintonia_natureza_user):Jogador(nome_user, hp_user, nivel_geral_user, lvl_brigar_user, lvl_apostar_user, lvl_forca_user, lvl_coragem_user, lvl_inteligencia_user){
            if(valida_atributo_construtor(imunidade_user) == true){
                this->imunidade = imunidade_user;
            }else{this->imunidade = 0;}

            if(valida_atributo_construtor(lvl_artesanato_user) == true){
                this->lvl_artesanato = lvl_artesanato_user;
            }else{this->lvl_artesanato = 0;}

            if(valida_atributo_construtor(lvl_arcos_user) == true){
                this->lvl_arcos = lvl_arcos_user;
            }else{this->lvl_arcos = 0;}

            if(valida_atributo_construtor(lvl_sintonia_natureza_user) == true){
                this->lvl_sintonia_natureza = lvl_sintonia_natureza_user;
            }else{this->lvl_sintonia_natureza = 0;}
        }

        // Construtor tipo 2 - Usuário não passou nenhum parâmetro
        Elfo():Jogador(){
            this->imunidade = 0;
            this->lvl_artesanato = 0;
            this->lvl_arcos = 0;
            this->lvl_sintonia_natureza = 0;
        }

        //polimorfismo
        void inicializa_jogador() override{
            return;
        }

    
};


int main(){


    return 0;

}