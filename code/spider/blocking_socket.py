import socket

tcp_socket = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM | socket.SOCK_NONBLOCK)

tcp_socket.setblocking(False)
# print(tcp_socket)
# exit(0)

tcp_socket.connect(('www.gnu.org', 80))

url = '/doc/doc.html'
request = 'GET {} HTTP/1.0\r\nHost: www.gnu.org\r\n\r\n'.format(url)

tcp_socket.send(request.encode('ascii'))
response = b''

chunk = tcp_socket.recv(4096)
while chunk:
    response += chunk
    chunk = tcp_socket.recv(4096)

print(response.decode('utf-8'))