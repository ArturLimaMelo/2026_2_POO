import java.util.Scanner;

public class ex01 {

    public static void main(String[] args) {
        Scanner Scanner = new Scanner(System.in);
        Circulo circulo = new Circulo(Scanner.nextDouble());
        System.out.println("Área: " + circulo.calcularArea());
        System.out.println("Circunferência: " + circulo.calcularCircunferencia());
    }
}