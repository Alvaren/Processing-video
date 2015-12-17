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
            int number_of_videos = 0;
            if (Int32.TryParse(textBox1.Text, out number_of_videos))
            {
                if (number_of_videos > 18 || number_of_videos < 1)
                {
                    ErrorForm error_form = new ErrorForm("'Number of videos' must be between 1 and 18");
                    error_form.ShowDialog();
                    return;
                }
            }
            else
            {
                ErrorForm error_form = new ErrorForm("'Number of videos' must be a number");
                error_form.ShowDialog();
                return;
            }

            run_shell_script();
            connect_with_python(number_of_videos);
            modify_current_frame();

            FinalWindow settingsForm = new FinalWindow();
            this.Hide();
            settingsForm.ShowDialog();
            this.Close();
        }

        private void connect_with_python(int number_of_videos)
        {
            send_video_path(comboBox1.SelectedItem.ToString());
            send_video_path(number_of_videos.ToString());
            send_video_path("stop");
        }

        private void modify_current_frame()
        {
            comboBox1.Enabled = false;
            textBox1.Enabled = false;
            button2.Enabled = false;
            label3.Visible = true;
            pictureBox1.Visible = true;
            label4.Visible = true;
        }

        private static void run_shell_script()
        {
            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            proc.EnableRaisingEvents = false;
            proc.StartInfo.FileName = "run.sh";
            proc.Start();
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
