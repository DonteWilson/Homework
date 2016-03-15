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

    public Unit()
    {

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
}
