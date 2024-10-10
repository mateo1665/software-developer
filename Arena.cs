using System;

public class Arena
{
    public static int TotalRounds { get; private set; }
    public static int TotalBattles { get; private set; }

    public void StartBattle(Trainer trainer1, Trainer trainer2)
    {
        Battle battle = new Battle(trainer1, trainer2);
        TotalBattles++;

        for (int i = 0; i < 6; i++)
        {
            TotalRounds++;
            Pokemon pokemon1 = trainer1.OpenPokeball(i).ContainedPokemon;
            Pokemon pokemon2 = trainer2.OpenPokeball(i).ContainedPokemon;

            string result = battle.FightRound(pokemon1, pokemon2);
            Console.WriteLine(result);
        }

        Console.WriteLine("Battle finished!");
        Console.WriteLine($"Total Battles: {TotalBattles}, Total Rounds: {TotalRounds}");
    }
}
