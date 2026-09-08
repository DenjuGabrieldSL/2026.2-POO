using System;

class EntradaCinema
{
    private string dia;
    private int horario;

    public EntradaCinema(string dia, int horario)
    {
        this.dia = dia.ToLower();
        this.horario = horario;
    }

    public double ValorInteira()
    {
        double valor;

        if (dia == "segunda" ||
            dia == "terca" ||
            dia == "quinta")
        {
            valor = 16.0;
        }
        else if (dia == "quarta")
        {
            return 8.0;
        }
        else
        {
            valor = 20.0;
        }

        if (horario >= 17)
        {
            valor *= 1.5;
        }

        return valor;
    }

    public double ValorMeia()
    {
        if (dia == "quarta")
        {
            return 8.0;
        }

        return ValorInteira() / 2.0;
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Digite o dia: ");
        string dia = Console.ReadLine();

        Console.Write("Digite o horario (0-23): ");
        int horario = int.Parse(Console.ReadLine());

        EntradaCinema entrada =
            new EntradaCinema(dia, horario);

        Console.WriteLine(
            "Valor da inteira: R$ " +
            entrada.ValorInteira()
        );

        Console.WriteLine(
            "Valor da meia-entrada: R$ " +
            entrada.ValorMeia()
        );
    }
}