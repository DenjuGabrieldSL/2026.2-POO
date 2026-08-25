import java.util.Scanner;

class EntradaCinema {
    private String dia;
    private int horario;

    public EntradaCinema(String dia, int horario) {
        this.dia = dia.toLowerCase();
        this.horario = horario;
    }

    public double valorInteira() {
        double valor;

        if (dia.equals("segunda") ||
            dia.equals("terca") ||
            dia.equals("quinta")) {

            valor = 16.0;

        } else if (dia.equals("quarta")) {

            return 8.0;

        } else {

            valor = 20.0;
        }

        if (horario >= 17) {
            valor *= 1.5;
        }

        return valor;
    }

    public double valorMeia() {
        if (dia.equals("quarta")) {
            return 8.0;
        }

        return valorInteira() / 2.0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Digite o dia: ");
        String dia = entrada.nextLine();

        System.out.print("Digite o horario (0-23): ");
        int horario = entrada.nextInt();

        EntradaCinema cinema =
            new EntradaCinema(dia, horario);

        System.out.println(
            "Valor da inteira: R$ " +
            cinema.valorInteira()
        );

        System.out.println(
            "Valor da meia-entrada: R$ " +
            cinema.valorMeia()
        );

        entrada.close();
    }
}