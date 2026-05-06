/* Descrição: refatore a classe Jogador com todos os atributos 
privados e validados 
Implemente propriedades para hp (não pode exceder 
hp máximo) 
□Criar método receber_dano( ) com validação 
□Criar método curar( ) com validação 
□Garantir que nível nunca seja negativo */

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


    return 0;

}