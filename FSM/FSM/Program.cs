using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace f
{
    class FSM
    {
        class Transition
        {
            public Transition(Enum from, Enum to)
            {

            }
        }
        Enum _currentState;
        public FSM(Enum initial)
        {
            _states = new List<Enum>();
            _currentState = initial;
        }
        private List<Enum> _states;

        public bool AddState(Enum state)
        {
            if (_states.Contains(state))
            {
                _states.Add(state);
                return true;
            }
            return false;

        }

        public void info()
        {
            Console.WriteLine("Finitie State Machine is comprise of ..");
            int count = 0;
            foreach (Enum s in _states)
            {
                Console.WriteLine("State " + count.ToString() + ": " + s.ToString());

                count++;
            

        }
            //public bool Addtansition(string transition)
            //{
            //    Enum from = null; // the first part before - >
            //    Enum to = null; // the second part after the ->
            //    return true;
            //}
            //Dictionary<Enum, List<Transition>> TransitionTable;
            _currentState.ToString();
     
        }
}
    //finite state machine
    class Program
    {
        enum  PlayerStates
        {
            init,
            idle,
            walk, 
            run,
        }
        static void Main(string[] args)
        {
            FSM fsm = new FSM(PlayerStates.init);
            fsm.AddState(PlayerStates.init);
            fsm.AddState(PlayerStates.idle);
            fsm.AddState(PlayerStates.walk);
            fsm.AddState(PlayerStates.run);
            fsm.AddState(PlayerStates.run);

            fsm.info();
            Console.ReadLine();

        }
      }
    }



