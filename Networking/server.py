import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(0)                 # Now wait for client connection.
print 'listening on port %s' % port

c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr

while True:
    from_client = c.recv(1024)
    c.send('Server >> %s' % from_client)
    # if from_client == "move_right":
    #     m = LargeMotor('B')
    #     m.moveRight()


c.close()                # Close the connection


