using System;
using System.Collections.Generic;

public class Trainer
{
    public string TrainerName { get; }
    public List<Pokeball> Belt { get; }

    public Trainer(string trainerName, List<Pokemon> availablePokemon)
    {
        TrainerName = trainerName;
        Belt = new List<Pokeball>();

        for (int i = 0; i < 6; i++)
        {
            Belt.Add(new Pokeball(availablePokemon)); // Geef unieke Pokémon mee
        }
    }

    public Pokeball OpenPokeball(int beltNumber)
    {
        if (beltNumber < 0 || beltNumber >= Belt.Count)
        {
            Console.WriteLine("Ongeldig Pokéball-nummer.");
            return null;
        }
        return Belt[beltNumber];
    }
}
