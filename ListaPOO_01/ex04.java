import java.util.Scanner;

public class ex04 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Cinema entrada = new Cinema(scanner.nextLine(), scanner.nextInt());
        System.out.println("Entrada inteira: " + entrada.entradaInteira());
        System.out.println("Meia Entrada: " + entrada.meiaEntrada());
        
    }
}