using System;
using System.Text;
using System.Windows.Forms;
using System.Net.Sockets;
using System.Net;
using System.IO;
using System.Diagnostics;
using System.Threading;
using System.Media;

namespace Launcher
{
    public partial class FinalWindow : Form
    {
        String host = Dns.GetHostName();
        int ip = 1232;

        public FinalWindow()
        {
            InitializeComponent();
            this.ShowInTaskbar = true;

            Thread oThread = new Thread(new ThreadStart(this.listen));
            oThread.Start();

            while (oThread.IsAlive)
            {
                Thread.Sleep(50);
                Application.DoEvents();
            }

            SoundPlayer simpleSound = new SoundPlayer(@"data\sounds\ding.wav");
            simpleSound.Play();

            string[] fileArray = Directory.GetFiles(@"data\graphs", "*.svg");
            foreach (String f in fileArray)
            {
                string filenameWithoutPath = Path.GetFileName(f);
                comboBox1.Items.Add(filenameWithoutPath);
            }
            comboBox1.SelectedIndex = 0;
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Process proc = new Process();
            String path = comboBox1.SelectedItem.ToString();
            proc.StartInfo.FileName = @"data\graphs\" + path;
            proc.StartInfo.UseShellExecute = true;
            proc.Start();
        }

        private void exit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
        private void listen()
        {
            IPAddress ipAddress = Dns.GetHostEntry(host).AddressList[0];
            TcpListener listener = new TcpListener(IPAddress.Any, ip);
            listener.Start();

            while (true)
            {
                TcpClient client = listener.AcceptTcpClient();
                NetworkStream nwStream = client.GetStream();
                byte[] buffer = new byte[client.ReceiveBufferSize];
                int bytesRead = nwStream.Read(buffer, 0, client.ReceiveBufferSize);
                string dataReceived = Encoding.ASCII.GetString(buffer, 0, bytesRead);
                nwStream.Write(buffer, 0, bytesRead);
                if (dataReceived == "stop") break;
                client.Close();
            }
            listener.Stop();
        }
    }
}
