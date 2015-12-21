using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Launcher
{
    public partial class ErrorForm : Form
    {
        public ErrorForm()
        {
            InitializeComponent();
        }

        public ErrorForm(String message)
        {
            InitializeComponent();
            label3.Text += message + "!";
        }

        private void exit_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
