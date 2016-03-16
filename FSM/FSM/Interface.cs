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
public interface IControl<T, V, W, U>
{
    List<Unit> Speed(T u);
    bool Victorious(bool b, U p, V e);
    void Fight(bool b, T u, W f);
    void Objectstats(T u);
   
}
