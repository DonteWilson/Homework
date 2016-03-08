using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Senpai
{
    
    public interface IHighSchooler
    {
        int grade();
    }
    public interface IMechPilot
    {
      
        int attack();
        int defence();
    }
    public interface IMonster
    {
        int level();
    }
    class Protaginist : IHighSchooler, IMechPilot
    {
        public int grade()
        {
            Console.WriteLine("I am in ");
     
            return 1;
        }
        public int attack()
        {
            Console.WriteLine("KA-POW");
            return 1;
        }
        public int defence()
        {
            Console.WriteLine("Ha Blocked it.");
            return 1;
        }

    }
    class SadTwist : IHighSchooler, IMonster
    {
        public int grade()
        {
            Console.WriteLine("");
            Console.WriteLine("");
            return 1;
        } 
        public int level()
        {
            Console.WriteLine("My current level is");
            return 1;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            List<IHighSchooler> student = new List<IHighSchooler>();
            List<IMechPilot> s = new List<IMechPilot>();


            for(int i = 0; i <2; i++)
            {
                Protaginist protaginist = new Protaginist();
                SadTwist sadtwist = new SadTwist();
                student.Add(protaginist);
                student.Add(sadtwist);
            }
            for (int i = 0; i < 2; i++)
            {
                Protaginist protaginist = new Protaginist();
                SadTwist sadtwist = new SadTwist();
            }
            for (int a = 0; a < 1; a++)
            foreach (IHighSchooler i in student)
            {
                i.grade();
            }
            foreach (IMechPilot a in s)
            {
                a.attack();
                a.defence();
            }

            Console.ReadLine();
        }
    }
}
