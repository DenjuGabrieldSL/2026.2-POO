#include <iostream>
using namespace std;

class Viagem {
private:
    double distancia;
    int horas;
    int minutos;

public:
    Viagem(double d, int h, int m) {
        distancia = d;
        horas = h;
        minutos = m;
    }

    double velocidadeMedia() {
        double tempoHoras = horas + minutos / 60.0;
        return distancia / tempoHoras;
    }
};

int main() {
    double distancia;
    int horas, minutos;

    cout << "Digite a distancia percorrida (km): ";
    cin >> distancia;

    cout << "Digite as horas: ";
    cin >> horas;

    cout << "Digite os minutos: ";
    cin >> minutos;

    Viagem v(distancia, horas, minutos);

    cout << "Velocidade media: "
         << v.velocidadeMedia() << " km/h" << endl;

    return 0;
}