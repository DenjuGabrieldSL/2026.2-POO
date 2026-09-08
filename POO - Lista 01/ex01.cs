using System;

class Circulo
{
    private double raio;

    public Circulo(double raio)
    {
        this.raio = raio;
    }

    public double Area()
    {
        return Math.PI * raio * raio;
    }

    public double Circunferencia()
    {
        return 2 * Math.PI * raio;
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Digite o raio do circulo: ");
        double raio = double.Parse(Console.ReadLine());

        Circulo c = new Circulo(raio);

        Console.WriteLine("Area: " + c.Area());
        Console.WriteLine("Circunferencia: " + c.Circunferencia());
    }
}