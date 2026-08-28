#include <iostream>
#include <cmath>
using namespace std;

class Circulo {
public:
    double raio;
    double area() {
        return M_PI * raio * raio;  
    }
    double circunferencia() {
        return 2 * M_PI * raio;  
    }
};

int main() { 
    Circulo x;
    Circulo y;
    x.raio = 5;
    y.raio = 3;
    Circulo z = x;   // z é um objeto  - é feito aqui uma cópia do objeto
    Circulo& t = x;  // t é uma referência para o objeto x
    Circulo& n = *(new Circulo());  // n é uma referência para um novo objeto
                                    // n = Circulo()
    n.raio = 8; 
    t.raio = 10;
    z.raio = 20;
    cout << x.raio << " " << x.area() << " " << x.circunferencia() << endl;
    cout << y.raio << " " << y.area() << " " << y.circunferencia() << endl;
    cout << n.raio << " " << n.area() << " " << n.circunferencia() << endl;
    return 0;
}

// g++ ex01.cpp -o ex01
// ./ex01
