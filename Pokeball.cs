using System;
using System.Collections.Generic;

internal class Pokeball
{
    public Pokemon ContainedPokemon { get; set; }
    private static Random random = new Random();

    public Pokeball(List<Pokemon> availablePokemon)
    {
        // Verdeel een unieke Pokémon uit de beschikbare lijst
        ContainedPokemon = availablePokemon[random.Next(availablePokemon.Count)];
        availablePokemon.Remove(ContainedPokemon); // Verwijder de gekozen Pokémon uit de lijst
    }
}
