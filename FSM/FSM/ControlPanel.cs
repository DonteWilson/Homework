using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


public sealed class ControlPanel : IControl<Player,Enemy, FSMac<i_STATES>>
{
    ControlPanel() { }

    static private ControlPanel _instance;

    static public ControlPanel instance
    {
        get
        {
            if (_instance == null)
                _instance = new ControlPanel();
            return _instance;
        }
    }
    public void Fight(bool b, Player p, Enemy e, FSMac<i_STATES> FSM)
    {
        if (b == false)
        {
            
        }
    }
}

