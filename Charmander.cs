using System;

public class Charmander : Pokemon
{
    public Charmander(string nickname)
        : base(nickname, "Fire", "Grass") { }

    public override string Battlecry()
    {
        return Nickname + " uses Flamethrower!";
    }
}
