from socket import *
import jwt
import datetime

# init
client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8001))

# Clinet login with username and password
username = 'RossUserName'
password = 'RossPassword'
JWT = '' # will recv from server after login

while True:
    print("[CLIENT]menu : [1] send username&password,[2] send right JWT,[3] send wrong JWT")
    menuNum = input(">>")
    # frist login with username&password,then store then token sent by server
    if menuNum == "1":
        msg = username+password
        client.send(msg.encode())
        data = client.recv(1024)
        print('[CLIENT]server send a JWT token, client store the token：\n', data.decode())
        JWT = data.decode()
    # after frist login, request with right token, verify by server
    elif menuNum == "2":
        client.send(JWT.encode())
        data = client.recv(1024)
        print('[CLIENT]server say：', data.decode())
    # after frist login, request with wrong token, verify by server
    elif menuNum == "3":
        JWTWrong = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ'
        client.send(JWTWrong.encode())
        data = client.recv(1024)
        print('[CLIENT]server say：', data.decode())
client.close
