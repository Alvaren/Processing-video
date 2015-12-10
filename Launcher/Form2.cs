using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Sockets;
using System.Net;
using System.IO;
using System.Diagnostics;

namespace Launcher
{
    public partial class Form2 : Form
    {
        String host = Dns.GetHostName();
        int ip = 1232;

        public Form2()
        {
            InitializeComponent();
            this.ShowInTaskbar = true;
            listen();
            string[] fileArray = Directory.GetFiles(@"c:\users\Sedi\Documents\repositories\processing-video\data\graphs", "*.svg");
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
                Console.WriteLine("Primljeno : " + dataReceived);
                Console.WriteLine("Dobijena poruka na serveru : " + dataReceived);
                nwStream.Write(buffer, 0, bytesRead);
                Console.WriteLine("\n");
                if (dataReceived == "stop") break;
                client.Close();
            }
            listener.Stop();
        }
    }
}
