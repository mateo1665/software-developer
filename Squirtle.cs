using System;

public class Squirtle : Pokemon
{
    public Squirtle(string nickname)
        : base(nickname, "Water", "Grass") { }

    public override string Battlecry()
    {
        return Nickname + " uses Water Gun!";
    }
}
