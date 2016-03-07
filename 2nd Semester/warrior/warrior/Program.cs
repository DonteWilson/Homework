using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tutorial
{

    public class Warrior
    {
        public string name;
        public int health;
        public Warrior(string n)
        {
            name = n;
        }
        public virtual void Fight(Warrior w)
        {
            Console.WriteLine("ARGHHHGHGHGHHGGGGGHGGHGH");
            w.health -= 5;
        }
        public virtual void SayName()
        {
            Console.WriteLine("My name is: " + name.ToString() + " Just a Happy Little Accident\n");
        }
    }
    class Ninja : Warrior
    {

        public int health;
        public Ninja(int hp, string n): base(n)
        {
            health = hp;
        }
       
        public override void Fight(Warrior w)
        {
            base.Fight(w);
            Console.WriteLine("주사위 주사");
        }
       //// public override void SayName()
       // {
       //     base.SayName();
       //     Console.WriteLine("My name is" + this.name);
       // }
    }
    class Duck : Warrior
    {
        public int health;
        public Duck(int hp, string n): base(n)
        {
            health = hp;
        }
        public override void Fight(Warrior w)
        {
            base.Fight(w);
            Console.WriteLine("D CANE PUT IT DOWN");
        }
        //public override void SayName()
        //{
        //    base.SayName();
        //    Console.WriteLine("My name is: " + this.name);
        //}
    }
    class Program
    {
        static void Main(string[] args)
        {
            List<Warrior> warriors = new List<Warrior>();

            for(int i = 0; i < 100; i++)
            {
                Ninja ninja = new Ninja(i + 5, "Ninja" + i.ToString());
                Duck duck = new Duck(i + 3, "Ducky" + i.ToString());
                warriors.Add(ninja);
                warriors.Add(duck);
            }
            foreach (Warrior w in warriors)
            {
                w.SayName();
                
            }
            int count = warriors.Count;

            for(int fi = 0; count > 1; fi++)
            {
                if (fi >= count)
                {
                    fi = 0;
                }
                if (fi == count -1)
                {
                    warriors[fi].Fight(warriors[0]);
                }
                if (warriors[0].health <= 0)
                {
                    warriors.Remove(warriors[0]);
                    count -= 1;
                }
                else
                {
                    warriors[fi].Fight(warriors[fi + 1]);
                    if (warriors[fi + 1].health <= 0)
                    {
                        warriors.Remove(warriors[fi + 1]);
                        count -= 1;
                    }
                }
            }
            Console.WriteLine(warriors[0].name + " IS VICTORIOUS ");
            Console.ReadLine();

        }
    }
}

