using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    public interface IAttack
    {
        int attack();
        int stats();
    }
    public interface Stats
    {
        int stats();
    }
    class Player : IAttack, Stats
    {
       public int hp = 10;
       public int dmg = 2;
        public int attack()
        {
            Console.WriteLine("My name is Jensen");
            Console.WriteLine("An Eenemy has been slain");
            return 1;
        }
        public int stats()
        {
            Console.WriteLine("Player HP: ", hp);
            Console.WriteLine("Player DMG: ", dmg);
            return 1;
        }
    }
    class Enemy : IAttack, Stats
    {
        public int attack()
        {
            Console.WriteLine("My name is Galvez");
            Console.WriteLine("An Ally has been slain");
            return 1;
        }
        public int stats()
        {
            int hp = 10;
            int dmg = 1;
            Console.WriteLine("Enemy HP: ", hp);
            Console.WriteLine("Enemy DMG: ", dmg);
            return 1;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<IAttack> fighters = new List<IAttack>();
            List<Stats> info = new List<Stats>();

            for (int i = 0; i < 2; i++)
            {
                Player player = new Player();
                Enemy enemy = new Enemy();
                fighters.Add(player);
                fighters.Add(enemy);
            }
            for (int i = 0; i < 2; i++)
            {
                Player player = new Player();
                Enemy enemy = new Enemy();
               
            }
            for (int a = 0; a < 1; a++)
            foreach (IAttack i in fighters)
            {
                i.attack();
            }
            foreach (Stats a in fighters)
            {
                a.stats();
            }
           
            Console.ReadLine();
        }
    }
}
