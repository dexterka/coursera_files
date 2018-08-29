import socket

# Define the connection
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()  # a request encoded to UTF-8
my_socket.send(cmd)  # sending a request

while True:
    data = my_socket.recv(512)  # receive 512 characters
    if (len(data)) < 1:
        break
    print(data.decode())  # returning the characters in internal unicode
my_socket.close()

# Returns only 400 Bad request - but in the discussion forum I found the updated Python script, now it works
# update: \r\n\r\n instead of \n\n because \r\n is the newline representation on Windows machines
# Using Google Chrome console / Network tab instead
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "1d3-54f6609240717"
# Content-Length: 467
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Content-Type: text/plain