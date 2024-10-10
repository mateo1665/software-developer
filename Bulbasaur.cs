using System;

public class Bulbasaur : Pokemon
{
    public Bulbasaur(string nickname)
        : base(nickname, "Grass", "Fire") { }

    public override string Battlecry()
    {
        return Nickname + " uses Vine Whip!";
    }
}
