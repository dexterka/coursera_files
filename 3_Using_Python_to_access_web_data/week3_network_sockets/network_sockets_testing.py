import socket

# Define the connection
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()  # a request encoded to UTF-8
my_socket.send(cmd)  # sending a request

while True:
    data = my_socket.recv(512)  # receive 512 characters
    if (len(data)) < 1:
        break
    print(data.decode())  # returning the characters in internal unicode
my_socket.close()