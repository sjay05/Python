import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))

while True:
    s.send(raw_input())
    print 'Received >> %s' % s.recv(1024)

s.close()

