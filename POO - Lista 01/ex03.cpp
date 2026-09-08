#include <iostream>
#include <string>
using namespace std;

class ContaBancaria {
private:
    string titular;
    int numero;
    double saldo;

public:
    ContaBancaria(string t, int n, double s) {
        titular = t;
        numero = n;
        saldo = s;
    }

    void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
            cout << "Deposito realizado." << endl;
        }
    }

    void sacar(double valor) {
        if (valor <= 0) {
            cout << "Valor invalido." << endl;
        } else if (valor > saldo) {
            cout << "Saldo insuficiente." << endl;
        } else {
            saldo -= valor;
            cout << "Saque realizado." << endl;
        }
    }

    double verificarSaldo() {
        return saldo;
    }
};

int main() {
    string titular;
    int numero;
    double saldoInicial;

    cout << "Nome do titular: ";
    getline(cin, titular);

    cout << "Numero da conta: ";
    cin >> numero;

    cout << "Saldo inicial: ";
    cin >> saldoInicial;

    ContaBancaria conta(titular, numero, saldoInicial);

    cout << "Saldo atual: R$ "
         << conta.verificarSaldo() << endl;

    double valor;

    cout << "Valor para depositar: ";
    cin >> valor;
    conta.depositar(valor);

    cout << "Saldo atual: R$ "
         << conta.verificarSaldo() << endl;

    cout << "Valor para sacar: ";
    cin >> valor;
    conta.sacar(valor);

    cout << "Saldo final: R$ "
         << conta.verificarSaldo() << endl;

    return 0;
}