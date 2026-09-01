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
        return this.numero.
    }

    /*
    void set_saldo(double saldo) {
        this.saldo = saldo;
    }
    */

    public void depositar(double valor) {
        saldo += valor;
    }

    public void sacar(double valor) {
        saldo -= valor;
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