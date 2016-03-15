using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Contains a bool to check the actions of a Player/Enemy
public interface IAttack<T>
{
    bool Combat(T u);
    bool Alive(T u);
    
}
//creates a public interface for stats for Player and Enemy
public interface IStats
{
    int Upgrade { get; set; }
    int Armor { get; set; }
    int XP { get; set; }
    string Type { get; set; }
}
public interface IControl<T, V, W>
{

}
