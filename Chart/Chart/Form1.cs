using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Chart
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
   
        private void attack_button_click(object sender, EventArgs e)
        {
            Random rand = new Random();


            List<int> DiceData = new List<int> { 3, 5, 6, 1, 6, 6, 4, 1, 2, 1, 1, 5 ,4 ,1 ,5, 1, 3, 2, 1 ,2 }; //List of Data for dice rolls
            DiceData.Sort();

            foreach (int i in DiceData)
            {
               DamageMeter.Series["Damage Roll"].Points.AddY(i);
            }
            
            int total = DiceData.Count;
            int sum = 0;
            for (int i = 0; i < DiceData.Count; ++i)
                sum += DiceData[i];
            float mean = (float)sum / total;
            float variance = 0;
        }
    }
}
