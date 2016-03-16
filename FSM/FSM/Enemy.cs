using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Enemy: Unit, IStats
{
   
    private int m_eLvl = 1;
    private int m_eXP = 50;

    private List<Enemy> m_EP = new List<Enemy>();

    public Enemy()
    {

    }


    public Enemy(string name, int hp, int Amr, string t)
    {
        Name = name;
        Lvl = m_eLvl;
        HP= hp;
        Armor = Amr;
        m_eXP = XP;
        Life = true;
        Type = t;
    }
    ////Enemy Lvl
    //public int Level
    //{
    //    get
    //    {
    //        return m_eLvl;
    //    }
    //    set
    //    {
    //        m_eLvl = value;
    //    }
    //}
    ////Enemy hp
    //public int hp
    //{
    //    get
    //    {
    //        return m_ehp;
    //    }
    //    set
    //    {
    //        m_ehp = value;
    //    }
    //}
    ////Armor
    //public int Amr
    //{
    //    get
    //    {
    //        return m_eArmor;
    //    }
    //    set
    //    {
    //        m_eArmor = value;
    //    }
    //}
    ////Experienced gained from killing enemy
    //public int Exp
    //{
    //    get
    //    {
    //        return m_eXP;
    //    }
    //    set
    //    {
    //        m_eXP = value;
    //    }
    //}
    ////Enemy name
    //public string Name
    //{
    //    get
    //    {
    //        return m_ename;
    //    }
    //}
    ////checks to see if alive
    //public bool Alive(Player p)
    //{
    //    if (p.hp < 0)
    //    {
    //        //statement here//
    //        return true;
    //    }
    //    else
    //    {
    //        //statement here
    //        return false;
    //    }
    //}

    //public bool Combat(Player p)
    //{
    //    if (p.hp > 0)
    //    {
    //        //statement here
    //        return true;
    //    }
    //    else
    //    {
    //        //statement here
    //        return false;
    //    }

    //}
    public List<Enemy> EP
    {
        get
        {
            return m_EP;
        }
        set
        {
            m_EP = value;
        }
    }
}

