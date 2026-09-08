import java.util.Scanner;

class Viagem {
    private double distancia;
    private int horas;
    private int minutos;

    public Viagem(double distancia, int horas, int minutos) {
        this.distancia = distancia;
        this.horas = horas;
        this.minutos = minutos;
    }

    public double velocidadeMedia() {
        double tempoHoras = horas + minutos / 60.0;
        return distancia / tempoHoras;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Digite a distancia percorrida (km): ");
        double distancia = entrada.nextDouble();

        System.out.print("Digite as horas: ");
        int horas = entrada.nextInt();

        System.out.print("Digite os minutos: ");
        int minutos = entrada.nextInt();

        Viagem v = new Viagem(distancia, horas, minutos);

        System.out.println(
            "Velocidade media: " +
            v.velocidadeMedia() + " km/h"
        );

        entrada.close();
    }
}