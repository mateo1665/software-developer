using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        int choice;
        do
        {
            Console.WriteLine("(1) Start the Battle simulator");
            Console.WriteLine("(2) Quit the Battle simulator");
            choice = int.Parse(Console.ReadLine());

            if (choice == 1)
            {
                StartBattle();
            }

        } while (choice != 2);
    }

    static void StartBattle()
    {
        Console.WriteLine("Welcome to the Pokémon Battle Simulator!");

        Console.Write("Type the name for your first trainer: ");
        string trainer1Name = Console.ReadLine();

        Console.Write("Type the name for your second trainer: ");
        string trainer2Name = Console.ReadLine();

        // Maak een lijst met beschikbare Pokémon
        List<Pokemon> availablePokemon1 = new List<Pokemon>
        {
            new Charmander("Charmander1"),
            new Squirtle("Squirtle1"),
            new Bulbasaur("Bulbasaur1")
        };

        List<Pokemon> availablePokemon2 = new List<Pokemon>
        {
            new Charmander("Charmander2"),
            new Squirtle("Squirtle2"),
            new Bulbasaur("Bulbasaur2")
        };

        Trainer trainer1 = new Trainer(trainer1Name, availablePokemon1);
        Trainer trainer2 = new Trainer(trainer2Name, availablePokemon2);

        Arena arena = new Arena();
        arena.StartBattle(trainer1, trainer2);
    }
}
