using System;

public class Battle
{
    public Trainer Trainer1 { get; }
    public Trainer Trainer2 { get; }

    public Battle(Trainer trainer1, Trainer trainer2)
    {
        Trainer1 = trainer1;
        Trainer2 = trainer2;
    }

    public string FightRound(Pokemon pokemon1, Pokemon pokemon2)
    {
        if (pokemon1.Strength == pokemon2.Weakness)
        {
            return $"{pokemon1.Nickname} wins the round!";
        }
        else if (pokemon2.Strength == pokemon1.Weakness)
        {
            return $"{pokemon2.Nickname} wins the round!";
        }
        else
        {
            return "It's a draw, both Pokémon return to their Pokéballs!";
        }
    }
}
