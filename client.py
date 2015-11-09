# client.py
import socket

host = socket.gethostname()
port = 1234

try:
    # while True:
    for x in range(0, 4):
            s = socket.socket()
            s.connect((host, port))
            # Here will be deframing videos
            s.send("hello world")
            print s.recv(4096)
            # End of deframing video
            s.close()
    # Send message to stop the server
    s = socket.socket()
    s.connect((host, port))
    s.send("stop")
    print s.recv(4096)
    s.close()

except socket.error:
    print 'Server is not responding. Shutting down.'
