using System;

namespace MsgClient
{
    class Program
    {
        static void Main(string[] args)
        {
            
            Program pg = new Program();
            pg.print("start program");

            // サーバーのIPアドレスを受け取る
            Console.Write("Enter the IP address of the server:");
            string ServerIpAddress = Console.ReadLine();

            // サーバーのポート番号を受け取る
            Console.Write("Enter the server port number:");
            string ServerPortNo = Console.ReadLine();

            //サーバーにメッセージを送信する
            pg.SendMsg("Hello Socket communication!", ServerIpAddress, int.Parse(ServerPortNo));
            pg.print("end program");
            Console.ReadLine();
        }
        private void SendMsg(string msg, String ServerIpAddress, int PortNo)
        {
            System.Net.Sockets.TcpClient tcp = new System.Net.Sockets.TcpClient(ServerIpAddress, PortNo);
            print("サーバー({0}:{1})と接続しました({2}:{3})",
                ((System.Net.IPEndPoint)tcp.Client.RemoteEndPoint).Address,
                ((System.Net.IPEndPoint)tcp.Client.RemoteEndPoint).Port,
                ((System.Net.IPEndPoint)tcp.Client.LocalEndPoint).Address,
                ((System.Net.IPEndPoint)tcp.Client.LocalEndPoint).Port);

            // Streamを取得する
            System.Net.Sockets.NetworkStream ns = tcp.GetStream();

            // タイムアウトを設定する
            ns.ReadTimeout = 10000;
            ns.WriteTimeout = 10000;

            // エンコードを指定する
            System.Text.Encoding enc = System.Text.Encoding.UTF8;

            // 送信する文字列をbyte配列に変換する
            byte[] sendBytes = enc.GetBytes(msg + '\n');

            // 文字列をサーバーに送信する
            ns.Write(sendBytes, 0, sendBytes.Length);

            // サーバーから文字列を取得する
            System.IO.MemoryStream ms = new System.IO.MemoryStream();
            byte[] resBytes = new byte[256];
            int resSize = 0;

            do
            {
                resSize = ns.Read(resBytes, 0, resBytes.Length);
                if (resSize == 0)
                {
                    print("サーバーが切断されました");
                    break;
                }

                ms.Write(resBytes, 0, resSize);

            } while (ns.DataAvailable || resBytes[resSize - 1] != '\n');

            // サーバーから受け取ったByte文字列を文字列に変換する
            string resMsg = enc.GetString(ms.GetBuffer(), 0, (int)ms.Length);

            // Streamを切断する
            ms.Close();

            // サーバーから受け取った文字列を表示する
            resMsg = resMsg.TrimEnd('\n');
            print(resMsg);

            ns.Close();
            tcp.Close();
            print("切断しました");
        }
        private void print(string msg)
        {
            Console.WriteLine(msg);
        }
        private void print(string format, params object[] args)
        {
            Console.WriteLine(format, args);
        }
    }
}
