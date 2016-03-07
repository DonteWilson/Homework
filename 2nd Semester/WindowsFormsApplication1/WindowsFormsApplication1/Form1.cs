using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace WindowsFormsApplication1
{
   public partial class Form1 : Form
    {
       public Form1()
        {

            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
        private void buttonExport_Click(object sender, EventArgs e)
        {
            Stream myStream;
            SaveFileDialog saveFileDialog1 = new SaveFileDialog();
            saveFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
            saveFileDialog1.FilterIndex = 2;
            saveFileDialog1.RestoreDirectory = true;
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                if ((myStream = saveFileDialog1.OpenFile()) != null)
                {
                    // Code to write the stream goes here.
                    myStream.Close();
                }
            }
        }
        //public class textOutput
        //{
        //    public static string Text { get; internal set; }
        //}

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            
            if(e.GetType() == typeof(MouseEventArgs))
            {
                MouseEventArgs me = e as MouseEventArgs;
                textOutput.Text += me.Location.ToString();
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            MouseEventArgs me = e as MouseEventArgs;
            textOutput.Text = null;
        }
        private void button3_Click(object sener, EventArgs e)
        {
            MessageBox.Show("주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사주사위 주사");
        }
        public void Collect(object sener, EventArgs e)
        {
            MouseEventArgs me = e as MouseEventArgs;
            textOutput.Text += me.Location.ToString();
        }
        private void Collection(object sener, EventArgs e)
        {
                MouseEventArgs me = e as MouseEventArgs;
                MessageBox.Show("Your Collection ");
                // Collect();

               
            
        }

        private void textBox1_TextChanged_1(object sender, EventArgs e)
        {

        }
    public class Data
        {
            public string name;
            public int info;
            public Data(string n)
            {
                name = n;
            }
          
        }
    class Hope 
        {
        
           public void Store(object sender, EventArgs e)
            {
                List<Data> info = new List<Data>();
                
                for(int i = 0; i < 100; i++)
                {
                    MouseEventArgs me = e as MouseEventArgs;
                    Data data = new Data(me.Location.ToString());
                    info.Add(data);

                    
                }
            }

        }
    }

    
}
