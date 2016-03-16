using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


public sealed class ControlPanel : IControl<List<Unit>, List<Player>, List<Enemy>, FSMac<i_STATES>>
{
    ControlPanel() { }

    static private ControlPanel _instance;

    static public ControlPanel instance
    {
        get
        {
            if (_instance == null)
            {
                _instance = new ControlPanel();
            }
            return _instance;
        }
    }
    public List<Unit> Speed(List<Unit> List)
    {
        Player listp = new Player();
        Enemy liste = new Enemy();
        List<Unit> sortedlist = new List<Unit>();
        sortedlist = List.OrderByDescending(u => u.Spd).ToList<Unit>();

        foreach (Unit i in sortedlist)
        {
            if(i.Type == "Player")
            {
                listp.Party.Add((Player)i);
            }
            if(i.Type == "Enemy")
            {
                liste.EP.Add((Enemy)i);
            }
        }
        Console.WriteLine(sortedlist.ElementAt(0).Name + "I'll draw first\n");

        return sortedlist;
    }
    public void Fight(bool b, List<Unit> uList, FSMac<i_STATES> FSM)
    {
        char input;
        Player listp = new Player();
        Enemy liste = new Enemy();
        Unit a = new Unit();

        for(int i = 0; i < uList.Count; i++)
        {
            if(uList.ElementAt(i).Type == "Player")
            {
                Console.Write("Press 1 to Attack");
                input = (char)Console.Read();

                if(input == '1')
                {
                    if(uList.ElementAt(i).Combat(a.Indicator(liste.EP)) == true)
                    {
                        break;
                    }
                }
            }
            else if (uList.ElementAt(i).Type == "Enemy")
            {

            }
        }
    }
    public void Objectstats(List<Unit> ulist)
    {
        Console.WriteLine("\nPlayer Info");

        for(int i = 0; i < ulist.Count; i++)
        {
            Console.WriteLine(ulist.ElementAt(i).Name + "Stats : \n");
            Console.WriteLine();
        }
    }
    public void Victorious(bool b, List<Player> listp, List<Enemy> liste)
    {

    }
}

