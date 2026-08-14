#include <iostream>

using namespace std;

int main()   {
    string nome;
    cout << "Digite seu nome: ";
    cin >> nome;
    cout << "Olá, " << nome << endl;
    return 0;  
}

// COMPILAR: g++ ex.cpp -o ex
// EXECUTAR: ./ex