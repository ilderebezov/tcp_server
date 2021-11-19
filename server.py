import sys
import socketserver
import logging

from schemas import MessageSchema


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(2048).strip()
        message_in = self.data.decode('UTF-8')
        message_in = message_in.split()
        schema = MessageSchema()
        result = schema.dump({
            'number': message_in[0],
            'id': message_in[1],
            'time': message_in[2],
            'group': message_in[3]
        })
        if result['group'][:2].find("00") == -1:
            try:
                open('logout.log', 'r', encoding='utf-8')
            except IOError:
                logging.basicConfig(filename='logout.log', format='%(message)s', level=logging.INFO)
                logging.info(self.data.decode('UTF-8'))
            else:
                logging.basicConfig(filename='logout.log', format='%(message)s', level=logging.INFO)
                logging.info(self.data.decode('UTF-8'))
        else:
            sys.stdout.write('спортсмен, нагрудный номер {0} прошёл отсечку {1} в {2}\n'
                             .format(result['number'], result['id'], result['time'][:5]))


if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
