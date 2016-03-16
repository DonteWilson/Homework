using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Unit : IStats
{
    private int m_uLvl;
    private int m_uArmor;
    private int m_uXP;
    private string m_uType;
    private Unit m_uTarget;
    private bool m_uLife;
    private int m_uHP;
    private int m_uSpd;
    public string m_uName;


    public string Name
    {
        get
        {
            return m_uName;
        }
        set
        {
            m_uName = value;
        }
    }
    public int Spd
    {
        get
        {
            return m_uSpd;
        }
        set
        {
            m_uSpd = value;
        }
    }
    public int Lvl
    {
        get
        {
            return m_uLvl;
        }
        set
        {
            m_uLvl = value;
        }
    }
    public bool Life
    {
        get
        {
            return m_uLife;
        }
        set
        {
            m_uLife = value;
        }
    }


    public Unit Target
    {
        get
        {
            return m_uTarget;
        }
        set
        {
            m_uTarget = value;
        }
    }

    public Unit()
    {

    }
    public int HP
    {
        get
        {
            return m_uHP;
        }
        set
        {
            m_uHP = value;
        }
    }
    public int Upgrade
    {
        get
        {
            return m_uLvl;
        }
        set
        {
            m_uLvl = value;
        }
    }
    public int Armor
    {
        get
        {
            return m_uArmor;
        }
        set
        {
            m_uArmor = value;
        }
    }
    public int XP
    {
        get
        {
            return m_uXP;
        }
        set
        {
            m_uXP = value;
        }
    }
    public string Type
    {
        get
        {
            return m_uType;
        }
        set
        {
            m_uType = value;
        }
    }
    public bool Combat(Unit u)
    {
        if (u.HP > 0)
        {
            float avg = u.Armor * 0.25f;
            u.HP -= this.Armor * (int)avg;
            return true;
        }
        else
        {
            Console.WriteLine(u.Name + "has been defeated");
            this.XP += u.XP;
            return false;
        }

    }
    public Unit Indicator(List<Enemy> EP)
    {
        string Input;

        Console.WriteLine("Chose a target: \n");
        for (int i = 0; i < EP.Count; i ++)
        {
            Console.WriteLine(EP.ElementAt(i).Name);
        }

        Input = Console.ReadLine();
        for (int i = 0; i < EP.Count; i++)
        {
            if (Input == EP.ElementAt(i).Name && EP.ElementAt(i).Life == true)
            {
                Target = EP.ElementAt(i);
            }
            else if (Input == EP.ElementAt(i).Name && EP.ElementAt(i).Life == false)
            {
                Console.WriteLine(EP.ElementAt(i).Name + "Target is Dead\n");
                Indicator(EP);
            }
        }
        return Target;
    }
}
