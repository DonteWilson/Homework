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
    //checks to see who attacks first.
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
    //void Function for Fight
    public void Fight(bool b, List<Unit> uList, FSMac<i_STATES> FSM)
    {
        char input;
        //Player list
        Player listp = new Player();
        //Enemy list
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
    //Displays the stats of a Player
    public void Objectstats(List<Unit> ulist)
    {
        //header for Player Satts
        Console.WriteLine("\nPlayer Info");

        for(int i = 0; i < ulist.Count; i++)
        {
            //keeps up to date with player stats and updates them accordingly.
            Console.WriteLine(ulist.ElementAt(i).Name + "Stats : \n");
            Console.WriteLine("Level: " + ulist.ElementAt(i).Lvl + "Health: " + ulist.ElementAt(i).HP + "Armor: " + ulist.ElementAt(i).Armor + "Exp: " + ulist.ElementAt(i).XP);
        }
    }
    //Checks to see if the player is victorious in battle.
    public bool Victorious(bool b, List<Player> listp, List<Enemy> liste)
    {
        int count = 0;
        int counts = 0;
        foreach(Player p in listp)
        {
            if(p.Life == false)
            {
                count++;
                if(listp.Count == count)
                {
                    b = true;
                }
            }
        }
        //checks through each enemy in the list and checks to see if they are still alive.
        foreach(Enemy e in liste)
        {
            if(e.Life == false)
            {
                counts++;
                if (liste.Count == count)
                {
                    b = true;
                }
            }
        }
        return b;
    }
}

