
# Pseudocode
# 1. Open a socket
# 2. Bind to a address(and port).
# 3. Listen for incoming connections.
# 4. Accept connections
# 5. Read/Send

import socket
import sys

# 1. Open a Socket
HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8000  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

# 2. Bind It to an address and a Port
try:
# python method .bind is used to bind a socket to a particular address and port
# This ensures that all incoming data that is directed towards this port is received by this application
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

# 3. Listen for incoming connections
# Function socket_listen is used to put the socket in listening mode
# The parameter of the function listen is called backlog- It controls the number of connections that can be kept waiting
# to be processed, then the 11th connection request shall be rejected
s.listen(10)
print 'Socket now listening'

# 4. Accept Connections
# Function socket_accept is used for this.
# Run this in a loop, this will help it keep the connection active
# Since the server closes connections after responding to the client,
# keep the connection active by making it receive incoming connections all the time.

while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    # Send data to the socket of the incoming connection
    # Client should be able to see this data
    data = conn.recv(1024)
    reply = 'OK...' + data
    if not data:
        break

    conn.sendall(reply)

    conn.close()
    s.close()

# connection is closed immediately after that simply because the server program ends after accepting and sending reply.