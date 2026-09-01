public class Cinema {
    private String dia;
    private int horario;

    void set_dia(String dia) {
        this.dia = dia;
    }

    void set_horario(int horario) {
        this.horario = horario;
    } 

    String get_dia() {
        return this.dia;
    }

    int get_horario() {
        return this.horario;
    }

    double entradaInteira(){
        double valor = 0;
        if (dia.equals("Segunda") || dia.equals("Terça") || dia.equals("Quinta")) valor = 16;
        else if (dia.equals("Quarta")) return 8;
        else valor = 20;
        if (horario >= 1700 && dia.equals("Quarta")) valor = valor * 1.5;
        return valor;
    }

    double meiaEntrada() {
        double valor = 0;
        if (dia.equals("Segunda") || dia.equals("Terça") || dia.equals("Quinta")) valor = 16;
        else if (dia.equals("Quarta")) return 8;
        else valor = 20;
        if (horario >= 1700 && dia.equals("Quarta")) valor = valor * 1.5;
        return valor / 2;
    }

    public Cinema(String dia, int horario) {
        this.dia = dia;
        this.horario = horario;
    }
}