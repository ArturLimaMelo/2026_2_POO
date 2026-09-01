public class Viagem {
    private double distancia;
    private double tempo;
    

    void set_distancia(double d) {
        this.distancia = d;
    }

    void set_tempo(double t) {
        this.tempo = t;
    }

    double get_distancia() {
        return this.distancia;
    }

    double get_tempo() {
        return this.tempo;
    }

    double velocidade_media() {
        return this.distancia / this.tempo;
    }

    public Viagem(double dist, int horas, int minutos) {
        this.distancia = dist;
        this.tempo = horas + minutos / 60.0;
    }
}