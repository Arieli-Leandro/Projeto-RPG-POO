/* Objetivo: Sistema de progressão baseado em experiência, e 
jogador com múltiplos construtores 
□
□Criar construtores para inicializar jogadores 
adequadamente 
Implementar sistema de experiência (xp) e subir_nivel( ) 
□Gerenciamento de memória: destrutores para liberar 
recursos */

#include <string.h>
#include <iostream>
using namespace std;

class Jogador{

    private:
        string nome;
        int nivel;
        int hp;
        int hp_maximo = 999;
        int lvl_combate;
        int lvl_magia;
        int lvl_alquimia;
        int lvl_habilidade_geral;
        int qtd_pontos_lvl = 0;

        bool valida_atributo_construtor(int valor){

            bool retorno = false;

            if(valor > 0){

                retorno = true;

            }

            return retorno;

        }

        bool valida_dano(int valor_dano){

            int vida_total = hp - valor_dano;

            bool retorno = false;

            if(vida_total >= 0){

                retorno = true;

            }

            return retorno;

        }

        bool valida_cura(int valor_cura){

            int vida_total = hp + valor_cura;

            bool retorno = false;

            if(vida_total <= hp_maximo){

                retorno = true;

            }

            return retorno;

        }

        void valida_experiencia(){

            while(nivel >= 100){
                nivel = nivel -100;
                qtd_pontos_lvl += 1;
            }

        }

    public:

        Jogador(string nm, int lvl, int hp_user, int lvl_comb, int lvl_mag, int lvl_al, int lvl_ge){

            nome = nm;

            if(valida_atributo_construtor(lvl)== true){

                nivel = lvl;

            }else {

                nivel = 0;
            }

            if(valida_atributo_construtor(hp_user) == true){

                hp = hp_user;

            }else{

                hp = 10;

            }


            if(valida_atributo_construtor(lvl_comb) == true){

                lvl_combate = lvl_comb;

            }else{

                lvl_combate = 0;

            }

            if(valida_atributo_construtor(lvl_al) == true){

                lvl_alquimia = lvl_al;

            }else{

                lvl_alquimia = 0;

            }

            if(valida_atributo_construtor(lvl_mag) == true){

                lvl_magia = lvl_mag;

            }else{

                lvl_magia = 0;

            }

            if(valida_atributo_construtor(lvl_ge) == true){

                lvl_habilidade_geral = lvl_ge;

            }else{

                lvl_habilidade_geral = 0;
            }

        }

        ~Jogador(){
            cout << "Removendo os dados do jogador:" << nome << endl;
        }

        void recebe_dano(int valor){

            if(valida_dano(valor) == true){

                hp = hp - valor;

            }else{

                cout << "Dano invalido" << endl;

            }


        }

        void recebe_cura(int valor){

            if(valida_cura(valor) == true){

                hp = hp + valor;

            }else{

                cout << "Cura invalida" << endl;

            }


        }

        void subir_nivel(){

            //chama a função
            valida_experiencia();

            // faz um menuzinho com swicth case 

            int opcao;
            if(qtd_pontos_lvl > 0){

                while(true){

                    cout << nome << endl;
                    cout << "1 - Upar Combate" << endl;
                    cout << "2 - Upar Magia" << endl;
                    cout << "3 - Upar Alquimia" << endl;
                    cout << "4 - Upar Habilidades Gerais" << endl;
                    cout << "Escolha uma opcao:" << endl;
                    cin >> opcao;

                    if(opcao >= 1 and opcao <= 4){
                        break;
                    }else{
                        cout<< "Digite uma opcao valida" << endl;
                    }

                }

                switch(opcao){
                   case 1: //Combate
                        qtd_pontos_lvl -= 1;
                        lvl_combate += 1;
                        cout << nome << "subiu de nivel em Combate!" << endl;
                        break;

                   case 2: //Magia
                        qtd_pontos_lvl-= 1;
                        lvl_magia += 1;
                        cout << nome << "subiu de nivel em Magia!" << endl;
                        break;

                   case 3: // Alquimia
                        qtd_pontos_lvl -= 1;
                        lvl_alquimia +=1;
                        cout << nome << "subiu de nivel em Alquimia!" << endl;
                        break;

                   case 4: //Habilidades Gerais
                        qtd_pontos_lvl -= 1;
                        lvl_habilidade_geral +=1;
                        cout << nome << "subiu de nivel em habilidades gerais!" << endl;
                        break;
                }
                
            }else{

                cout << nome << "Nao tem pontos para subir de nivel" << endl;
            }


        }

        void exibe_jogador(){

            cout << "| " << nome
            <<"|LVL| " << nivel
            << "HP | " << hp
            << "Lvl Alquimia | " << lvl_alquimia
            << "Lvl Combate  | " << lvl_combate
            << "Lvl HabGeral |" << lvl_habilidade_geral
            << "Lvl Magia    |" << lvl_magia
            << endl;

        }

};

int main(){

    Jogador jogador3("Ciri", 120, 450, 90, 40, 30, 80);
    jogador3.exibe_jogador();

    jogador3.recebe_cura(1000); 
    jogador3.exibe_jogador();

    Jogador jogador4("Dandelion", -10, -50, -5, -3, -2, -1);
    jogador4.exibe_jogador();


    //upando os jogadores
    jogador3.subir_nivel();
    jogador4.subir_nivel();

    //exibindo a nova pontuação do jogador
    jogador4.exibe_jogador();

    return 0;

}