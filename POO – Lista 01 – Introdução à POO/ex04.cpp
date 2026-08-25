#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class EntradaCinema {
private:
    string dia;
    int horario;

public:
    EntradaCinema(string d, int h) {
        dia = d;
        horario = h;
    }

    double valorInteira() {
        double valor;

        if (dia == "segunda" || dia == "terca" ||
            dia == "quinta") {
            valor = 16.0;
        }
        else if (dia == "quarta") {
            return 8.0;
        }
        else {
            valor = 20.0;
        }

        if (horario >= 17) {
            valor *= 1.5;
        }

        return valor;
    }

    double valorMeia() {
        if (dia == "quarta") {
            return 8.0;
        }

        return valorInteira() / 2.0;
    }
};

int main() {
    string dia;
    int horario;

    cout << "Digite o dia: ";
    cin >> dia;

    cout << "Digite o horario (0-23): ";
    cin >> horario;

    EntradaCinema entrada(dia, horario);

    cout << "Valor da inteira: R$ "
         << entrada.valorInteira() << endl;

    cout << "Valor da meia-entrada: R$ "
         << entrada.valorMeia() << endl;

    return 0;
}