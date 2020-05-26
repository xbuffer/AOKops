from django.test import TestCase

# Create your tests here.
import socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello,world!'''
response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun, 18 may 2020 00:28:01 GMT',
    'Content-Type: text/html; charset=utf-8',
    'Content-Length: {}\r\n'.format(len(body.encode())),
    body,
]
response = '\r\n'.join(response_params)


def handle_connection(conn, addr):
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response.encode())
    conn.close()


def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(5)
    print('http://127.0.0.1:8000')
    try:
        while True:
            conn, addr = serversocket.accept()
            handle_connection(conn, addr)
    finally:
        serversocket.close()


if __name__ == '__main__':
    main()
