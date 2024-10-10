using System;

public abstract class Pokemon
{
    public string Nickname { get; set; }
    public string Strength { get; set; }
    public string Weakness { get; set; }

    public Pokemon(string nickname, string strength, string weakness)
    {
        Nickname = nickname;
        Strength = strength;
        Weakness = weakness;
    }

    public abstract string Battlecry();
}
