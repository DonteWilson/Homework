using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public enum i_STATES
{
    Init, // Player init state
    Idle, // Player idle state
    Target, // Checks to see who is being target
    Death, // Player Death state
}
namespace FSMachine
{ 
    class Program
    {
        static void Main(string[] args)
        {
            FSMac<i_STATES> FSM = new FSMac<i_STATES>();
            //Adding States
            FSM.AddState(i_STATES.Init);
            FSM.AddState(i_STATES.Idle);
            FSM.AddState(i_STATES.Target);
            FSM.AddState(i_STATES.Death);

            //Adding Transitions
            FSM.AddT(i_STATES.Init, i_STATES.Idle);
            FSM.AddT(i_STATES.Idle, i_STATES.Target);
            FSM.AddT(i_STATES.Target, i_STATES.Death);

            //Graps a list of units 
            List<Unit> uList = new List<Unit>();

           

            FSM.info();
            Console.ReadLine();

        }
      }
}




