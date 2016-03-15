using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class FSMac<T>
{
    public class Transition
    {
        public T from;

        public T to;

        public Transition(T f, T t)
        {
            from = f;
            to = t;
                
        }
    }
    private T _currentState;

    private List<T> _states;
    //Dictionary which has multiple transitional values
    private Dictionary<T, List<Transition>> Transitions;

    public T state
    {
        get
        {
            return _currentState;
        }
    }
    public FSMac()
    {
        Transitions = new Dictionary<T, List<Transition>>();

        _states = new List<T>();
    }
    public bool AddState(T i)
    {
        if(_states.Contains(i))
        {
            Console.WriteLine("Unable to add state");
            return false;
        }
        else
        {
            _states.Add(i);
            Transitions.Add(i, new List<Transition>());
            return true;
        }
    }
    public void AddT(T f, T t)
    {
        if(Transitions.ContainsKey(f))
        {
            Transitions[f].Add(new Transition(f, t));        
        }
    }
    public void TState(T i)
    {
        dynamic Tstate = _currentState;

        foreach (Transition t in Transitions[_currentState])
        {
            if(t.to.Equals(i))
            {
                _currentState = i;

                break;
            }
        }
        if (Tstate == _currentState)
        {
            Console.WriteLine("bad transition");
        }
    }
    public void info()
    {
        Console.WriteLine("FSM Contains....\n");
        int count = 1;

        foreach (T s in _states)
        {
            Console.WriteLine("State" + count.ToString() + " : " + s.ToString());
            

            count++;
        }
        Console.WriteLine("\nCurrent State: " + _currentState);
    }

}