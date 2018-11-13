import socket

class Client:
    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = (self.server, self.port)

    def connect_to_server(self):
        self.socket.connect(self.connection)
        self.message_handler()

    def message_handler(self):
        while True:
            self.message = input("Message: ")
            try:
                self.socket.send(self.message.encode())
                self.answer = self.socket.recv(1024)
                print("Answer: {}".format(self.answer))
            except Exception as e:
                self.socket.close()
                print(e)
                return False


if __name__ == '__main__':
    Client('127.0.0.1', 12345).connect_to_server()
