using System;
using System.Windows.Forms;
using System.Net.Sockets;
using System.Net;
using System.IO;

namespace Launcher
{
    public partial class MainWindow : Form
    {
        String host = Dns.GetHostName();
        int ip = 1232;

        public MainWindow()
        {
            InitializeComponent();
            this.ShowInTaskbar = true;
            string[] fileArray = Directory.GetFiles(@"data\video", "*.avi");
            foreach (String f in fileArray){
                string filenameWithoutPath = Path.GetFileName(f);
                comboBox1.Items.Add(filenameWithoutPath);
            }
            comboBox1.SelectedIndex = 0;
            textBox1.Text = "18";
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            int x = 0;
            if (Int32.TryParse(textBox1.Text, out x))
            {
                if (x > 18) x = 18;
                if (x < 1) x = 1;
            }
            else
            {
                x = 1;
            }

            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            proc.EnableRaisingEvents = false;
            proc.StartInfo.FileName = "run.sh";
            proc.Start();

            send_video_path(comboBox1.SelectedItem.ToString());
            send_video_path(x.ToString());
            send_video_path("stop");
            comboBox1.Enabled = false;
            textBox1.Enabled = false;
            button2.Enabled = false;
            label3.Visible = true;
            pictureBox1.Visible = true;
            label4.Visible = true;
            FinalWindow settingsForm = new FinalWindow();
            this.Hide();
            settingsForm.ShowDialog();
            this.Close();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void send_video_path(String message)
        {
            try
            {
                TcpClient socket = new TcpClient();
                socket.Connect(host, ip);
                NetworkStream network = socket.GetStream();
                StreamWriter streamWriter = new System.IO.StreamWriter(network);
                streamWriter.Write(message);
                streamWriter.Flush();
                network.Close();
            }
            catch (Exception)
            {
                System.Threading.Thread.Sleep(5000);
                send_video_path(message);
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }
    }
}
