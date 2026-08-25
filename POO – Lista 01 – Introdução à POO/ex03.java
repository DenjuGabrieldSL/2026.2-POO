import java.util.Scanner;

class ContaBancaria {
    private String titular;
    private int numero;
    private double saldo;

    public ContaBancaria(String titular, int numero, double saldo) {
        this.titular = titular;
        this.numero = numero;
        this.saldo = saldo;
    }

    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
            System.out.println("Deposito realizado.");
        }
    }

    public void sacar(double valor) {
        if (valor <= 0) {
            System.out.println("Valor invalido.");
        } else if (valor > saldo) {
            System.out.println("Saldo insuficiente.");
        } else {
            saldo -= valor;
            System.out.println("Saque realizado.");
        }
    }

    public double verificarSaldo() {
        return saldo;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Nome do titular: ");
        String titular = entrada.nextLine();

        System.out.print("Numero da conta: ");
        int numero = entrada.nextInt();

        System.out.print("Saldo inicial: ");
        double saldo = entrada.nextDouble();

        ContaBancaria conta =
            new ContaBancaria(titular, numero, saldo);

        System.out.println(
            "Saldo atual: R$ " +
            conta.verificarSaldo()
        );

        System.out.print("Valor para depositar: ");
        double valor = entrada.nextDouble();
        conta.depositar(valor);

        System.out.println(
            "Saldo atual: R$ " +
            conta.verificarSaldo()
        );

        System.out.print("Valor para sacar: ");
        valor = entrada.nextDouble();
        conta.sacar(valor);

        System.out.println(
            "Saldo final: R$ " +
            conta.verificarSaldo()
        );

        entrada.close();
    }
}