using System;
using System.Windows.Forms;


namespace claculator.Csharp
{
    public partial class Form1 : Form
    {
        int num1 = 0;
        int num2 = 0;
        int res;
        char operators;
        public Form1()
        {
            InitializeComponent();
        }

        private void Converter(int res)
        {
            textNum.Text = res.ToString();
        }

        private void btnEqual_Click(object sender, EventArgs e)
        {
            if (operators == '+' && textNum.Text != "")
            {
                num2 = int.Parse(textNum.Text);
                res = num1 + num2;
                Converter(res);
            }

            else if (operators == '-' && textNum.Text != "")
            {
                num2 = int.Parse(textNum.Text);
                res = num1 - num2;
                Converter(res);
            }

            else if (operators == '*' && textNum.Text != "")
            {
                num2 = int.Parse(textNum.Text);
                res = num1 * num2;
                Converter(res);
            }

            else if (operators == '/' && textNum.Text != "")
            {
                num2 = int.Parse(textNum.Text);
                try
                {
                   res = num1 / num2;
                   Converter(res);
                }
                   
                catch(DivideByZeroException)
                {
                    MessageBox.Show("num2 have not to be a Zero");
                }
            }

            else
            {
                res = 0;
                Converter(res);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            num1 = int.Parse(textNum.Text);
            textNum.Clear();
            operators = '+';
        }

        private void btnSubtract_Click(object sender, EventArgs e)
        {
            num1 = int.Parse(textNum.Text);
            textNum.Clear();
            operators = '-';
        }

        private void btnMultiply_Click(object sender, EventArgs e)
        {
            num1 = int.Parse(textNum.Text);
            textNum.Clear();
            operators = '*';
        }

        private void btndiv_Click(object sender, EventArgs e)
        {
            num1 = int.Parse(textNum.Text);
            textNum.Clear();
            operators = '/';
        }
    }
}
