import socket
import json


host = '192.168.1.14'
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = raw_input(">> ")
    command = command.split(" ")
    try:
        if command[0] == 'exit':
            s.close()
            exit()
        elif command[0] == 'gamepin':
            s.sendall(command[1])
        elif command[0] == 'start':
            s.sendall(command[0])
    except Exception:
        result = '[-[ error during command execution'
        print(result)

