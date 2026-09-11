public class Circulo {
    private double raio;

    double getRaio() {
        return this.raio;
    }

    void setRaio(double r) {
        this.raio = r;
    }

    double calcularArea() {
        return 3.14 * this.raio * this.raio;
    }

    double calcularCircunferencia() {
        return 2 * 3.14 * this.raio;
    }

    public Circulo(double raio) {
        this.raio = raio
    }
}
