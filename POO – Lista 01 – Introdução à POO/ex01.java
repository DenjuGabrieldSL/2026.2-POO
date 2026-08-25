import java.util.Scanner;

class Circulo {
    private double raio;

    public Circulo(double raio) {
        this.raio = raio;
    }

    public double area() {
        return Math.PI * raio * raio;
    }

    public double circunferencia() {
        return 2 * Math.PI * raio;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Digite o raio do circulo: ");
        double raio = entrada.nextDouble();

        Circulo c = new Circulo(raio);

        System.out.println("Area: " + c.area());
        System.out.println("Circunferencia: " + c.circunferencia());

        entrada.close();
    }
}