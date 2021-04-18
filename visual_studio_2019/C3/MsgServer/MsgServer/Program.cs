using System;

namespace MsgServer
{
    class Program
    {
        static void Main(string[] args)
        {
            Program pg = new Program();
            pg.print("start server");
            Console.Write("Enter the server port number:");
            String PortNo = Console.ReadLine();
            pg.server(int.Parse(PortNo));
            pg.print("end server");
            Console.ReadLine();
        }
        private void server(int PortNo)
        {
            // サーバー用IPAddresを作成
            System.Net.IPAddress ipAdd = System.Net.IPAddress.Parse("127.0.0.1");

            // ソケット通信を開始する
            System.Net.Sockets.TcpListener listener = new System.Net.Sockets.TcpListener(ipAdd, PortNo);
            listener.Start();
            System.Net.IPEndPoint LocalEndPoint = (System.Net.IPEndPoint)listener.LocalEndpoint;
            pring("Listenを開始しました({0}:{1})。", LocalEndPoint.Address, LocalEndPoint.Port);

            // 接続要求があったら受け入れる
            System.Net.Sockets.TcpClient client = listener.AcceptTcpClient();
            System.Net.IPEndPoint RemoteEndPoint = (System.Net.IPEndPoint)client.Client.RemoteEndPoint;
            pring("クライアント({0}:{1})と接続しました。", RemoteEndPoint.Address, RemoteEndPoint.Port);

            // NetworkStreamを取得データの流れ
            System.Net.Sockets.NetworkStream ns = client.GetStream();
            ns.ReadTimeout = 10000;
            ns.WriteTimeout = 10000;

            System.Text.Encoding enc = System.Text.Encoding.UTF8;
            bool disconnected = false;
            System.IO.MemoryStream ms = new System.IO.MemoryStream();

            byte[] resBytes = new byte[256];
            int resSize = 0;

            do
            {
                //データの一部を受信する
                resSize = ns.Read(resBytes, 0, resBytes.Length);
                //Readが0を返した時はクライアントが切断したと判断
                if (resSize == 0)
                {
                    disconnected = true;
                    print("クライアントが切断しました。");
                    break;
                }
                //受信したデータを蓄積する
                ms.Write(resBytes, 0, resSize);
                //まだ読み取れるデータがあるか、データの最後が\nでない時は、
                // 受信を続ける

            } while (ns.DataAvailable || resBytes[resSize - 1] != '\n');

            //受信したデータを文字列に変換
            string resMsg = enc.GetString(ms.GetBuffer(), 0, (int)ms.Length);
            ms.Close();

            resMsg = resMsg.TrimEnd('\n');
            print(resMsg);

            if (!disconnected)
            {
                //クライアントにデータを送信する
                //クライアントに送信する文字列を作成
                string sendMsg = resMsg.Length.ToString();

                //文字列をByte型配列に変換
                byte[] sendBytes = enc.GetBytes(sendMsg + '\n');

                //データを送信する
                ns.Write(sendBytes, 0, sendBytes.Length);
                print(sendMsg);
            }

            ns.Close();
            client.Close();
            print("クライアントとの接続を閉じました。");

            listener.Stop();
            print("Listenerを閉じました。");
        }
        private void print(String msg)
        {
            Console.WriteLine(msg);
        }
        private void pring(string format, params object[] arg)
        {
            Console.WriteLine(format, arg);
        }
    }
}
