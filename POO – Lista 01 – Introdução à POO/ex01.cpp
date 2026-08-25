#include <iostream>
#include <cmath>
using namespace std;

class Circulo {
private:
    double raio;

public:
    Circulo(double r) {
        raio = r;
    }

    double area() {
        return M_PI * raio * raio;
    }

    double circunferencia() {
        return 2 * M_PI * raio;
    }
};

int main() {
    double raio;

    cout << "Digite o raio do circulo: ";
    cin >> raio;

    Circulo c(raio);

    cout << "Area: " << c.area() << endl;
    cout << "Circunferencia: " << c.circunferencia() << endl;

    return 0;
}