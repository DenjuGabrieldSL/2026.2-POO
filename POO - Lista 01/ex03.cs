using System;

class ContaBancaria
{
    private string titular;
    private int numero;
    private double saldo;

    public ContaBancaria(string titular, int numero, double saldo)
    {
        this.titular = titular;
        this.numero = numero;
        this.saldo = saldo;
    }

    public void Depositar(double valor)
    {
        if (valor > 0)
        {
            saldo += valor;
            Console.WriteLine("Deposito realizado.");
        }
    }

    public void Sacar(double valor)
    {
        if (valor <= 0)
        {
            Console.WriteLine("Valor invalido.");
        }
        else if (valor > saldo)
        {
            Console.WriteLine("Saldo insuficiente.");
        }
        else
        {
            saldo -= valor;
            Console.WriteLine("Saque realizado.");
        }
    }

    public double VerificarSaldo()
    {
        return saldo;
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Nome do titular: ");
        string titular = Console.ReadLine();

        Console.Write("Numero da conta: ");
        int numero = int.Parse(Console.ReadLine());

        Console.Write("Saldo inicial: ");
        double saldo = double.Parse(Console.ReadLine());

        ContaBancaria conta =
            new ContaBancaria(titular, numero, saldo);

        Console.WriteLine(
            "Saldo atual: R$ " +
            conta.VerificarSaldo()
        );

        Console.Write("Valor para depositar: ");
        double valor = double.Parse(Console.ReadLine());
        conta.Depositar(valor);

        Console.WriteLine(
            "Saldo atual: R$ " +
            conta.VerificarSaldo()
        );

        Console.Write("Valor para sacar: ");
        valor = double.Parse(Console.ReadLine());
        conta.Sacar(valor);

        Console.WriteLine(
            "Saldo final: R$ " +
            conta.VerificarSaldo()
        );
    }
}