using System;

class Viagem
{
    private double distancia;
    private int horas;
    private int minutos;

    public Viagem(double distancia, int horas, int minutos)
    {
        this.distancia = distancia;
        this.horas = horas;
        this.minutos = minutos;
    }

    public double VelocidadeMedia()
    {
        double tempoHoras = horas + minutos / 60.0;
        return distancia / tempoHoras;
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Digite a distancia percorrida (km): ");
        double distancia = double.Parse(Console.ReadLine());

        Console.Write("Digite as horas: ");
        int horas = int.Parse(Console.ReadLine());

        Console.Write("Digite os minutos: ");
        int minutos = int.Parse(Console.ReadLine());

        Viagem v = new Viagem(distancia, horas, minutos);

        Console.WriteLine(
            "Velocidade media: " +
            v.VelocidadeMedia() + " km/h"
        );
    }
}