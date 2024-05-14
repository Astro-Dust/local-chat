import socket

HOST = 'localhost'
PORT = 7_000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(2)

conn, ip_addr = s.accept()

while True:
  msg = conn.recv(512).decode('ascii')
  
  if not msg:
    break

  print(msg)
