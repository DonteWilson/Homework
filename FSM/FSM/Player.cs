using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Public Player class connected to Unit, Stats, Attack
public class Player: Unit, IStats, IAttack<Enemy>
{
    private string m_name;
    private int m_Lvl = 1;
    private int m_hp;
    private int m_Armor;
    private int m_XP = 0;
    private string m_Type;
    //Player class with stats of the player
    public Player(string name, int hp, int Amr, string t)
    {
        m_name = name;
        m_Lvl = Upgrade1;
        m_hp = hp;
        m_Armor = Amr;
        m_XP = Exp;
        Type = t;
    }
    //Level/Upgrades
    public int Upgrade1
    {
        get
        {
            return m_Lvl;
        }
        set
        {
            m_Lvl = value;
        }
    }
    //Health
    public int hp
    {
        get
        {
            return m_hp;
        }
        set
        {
            m_hp = value;
        }
    }
    //Armor
    public int  Amr
    {
        get
        {
            return m_Armor;
        }
        set
        {
            m_Armor = value;
        }
    }
    //Experience
    public int Exp
    {
        get
        {
            return m_XP;
        }
        set
        {
            m_XP = value;
        }
    }
    //Name of player.
    public string Name
    {
        get
        {
            return m_name;
        }
    }
    public bool Alive(Enemy e)
    {
        if(e.hp < 0)
        {
            //statement here
            return true;
        }
        else
        {
            //statement here
            return false;
        }
    }
    //checks to see if combat is active. Has if to check
    public bool Combat(Enemy e)
    {
        if(e.hp > 0)
        {
            float avg = e.Amr * 0.25f;
            e.hp -= this.Amr * (int)avg;
            return true;
        }
        else
        {
            Console.WriteLine(e.Name + "has been defeated");
            this.Exp += e.Exp;
            return false;
        }

    }
    //Ding Level Up
    public void Ding()
    {
        if (this.Exp == 50)
        {
            Console.Write("Your character stats have updated!\n");
            this.Upgrade1++;
            this.Exp = 0;
            this.hp += 15;
            this.Armor += 5;
        }
    }
}