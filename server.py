from threading import Thread
import socket
import time

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        print("Successfully binded address {} and port {}".format(self.host, self.port))

    def run(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(30)
            Thread(target=self.client_handler, args=(client, address)).start()

    def client_handler(self, client, address):
        packet_size = 1024
        while True:
            try:
                data = client.recv(packet_size)
                if data:
                    # Wait for user to responde
                    client.send(resp.encode())
                else:
                    raise error("Something went wrong")
            except:
                client.close()
                return False

if __name__ == '__main__':
    Server("127.0.0.1", 12345).run()
