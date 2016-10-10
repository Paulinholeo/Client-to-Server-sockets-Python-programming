# Sockets are the fundamental "things" behind any kind of network communications done by your computer.
# For example when you type www.google.com in your web browser,
# it opens a socket and connects to google.com to fetch the page and show it to you.
# Same with any chat client like skype. Any network communication goes through a socket.



# Pseudocode
# 1. Create a socket
# 2. Connect to remote server
# 3. Send some data
# 4. Receive a reply



import socket
import sys


# 1. Creating Socket

try:

# AF_INET & SOCK_STREAM are properties of the socket created
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# error thrown in by python to catch exception called socket.error
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

print "Socket Created"


# 2. Connecting to Server

# Require 2 things in order to connect to a server
# 1. IP address
# 2. Port NUmber
# First declare the IP address of the server that you are going to connect to
host = "www.google.com"
port = 80

try:
# python method to get the IP address
    remote_ip = socket.gethostbyname( host )

except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

print 'Ip address of ' + host + ' is ' + remote_ip

# Now use the connect function to connect to the server, passing in the IP and the port as paramenters
s.connect((remote_ip , port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

# 3. Sending Data to the Server
# Message is actually a http command to fetch the mainpage of a website
message = "GET / HTTP/1.1\r\n\r\n"

try :
    #send.all python frunction to send the entire string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
print 'Message send successfully'


# 4. Receive a reply from the server
# Function .recv used to receive data on a socket
# Buffer size of incoming request is what is passed in as a parameter
reply = s.recv(4096)

print reply

# close the socket
s.close()
