import java.util.Scanner;

public class ex02 {

    public static void main(String[] args) {
        Scanner Scanner = new Scanner(System.in);
        Viagem viagem = new Viagem(Scanner.nextInt(), Scanner.nextInt(), Scanner.nextInt());
        System.out.println("Velocidade Média: " + viagem.velocidade_media() + " Km/h");
    }
}