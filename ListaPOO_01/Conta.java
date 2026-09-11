public class Conta {
    private String nome;
    private int numero;
    private double saldo;

    void set_nome(String nome) {
        this.nome = nome;
    }

    String get_nome() {
        return this.nome;
    }

    void set_numero(int numero) {
        this.numero = numero;
    }

    int get_numero() {
        return this.numero;
    }

    /*
    void set_saldo(double saldo) {
        this.saldo = saldo;
    }
    */

    public void depositar(double valor) {
        if (valor < 0) {
            System.out.println("Valor digitado deve ser positivo\nTente novamente");
        } else saldo += valor;
    }

    public void sacar(double valor) {
        if (valor > saldo || valor < 0) {
            System.out.println("Saldo insuficiente ou valor negativo\nTente novamente");
        } else saldo -= valor;
    }

    public double consultarSaldo() {
        return saldo;
    }

    public Conta(String nome, int numero, double saldo) {
        this.nome = nome;
        this.numero = numero;
        this.saldo = saldo;
    }
}