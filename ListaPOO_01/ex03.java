import java.util.Scanner;

public class ex03 {
    public static void main(String[] args) {
        Scanner Scanner = new Scanner(System.in);
        int opt = 0;
        Conta conta = new Conta(Scanner.next(), Scanner.nextInt(), Scanner.nextDouble());
        while (opt != 4) {
            System.out.println("1 - Depositar");
            System.out.println("2 - Sacar");
            System.out.println("3 - Consultar Saldo");
            System.out.println("4 - Sair");
            opt = Scanner.nextInt();
            switch (opt) {
                case 1:
                    System.out.println("Digite o valor a ser depositado: ");
                    conta.depositar(Scanner.nextDouble());
                    break;
                case 2:
                    System.out.println("Digite o valor a ser sacado: ");
                    conta.sacar(Scanner.nextDouble());
                    break;  
                case 3:
                    System.out.println("Saldo: " + conta.consultarSaldo());
                    break;  
                case 4: 
                    System.out.println("Saindo...");
                    break;
        }
    }
}
}