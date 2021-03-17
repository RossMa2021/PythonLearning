from socket import *
import jwt
import datetime

server = socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8001))
server.listen(5)

IsHasJWT = False
while True:
        print("[SERVER]begin listening …")
        conn, addr = server.accept()
        print("[SERVER]client connection address is ",addr)
        while True:
            msg = conn.recv(1024)
            # frist login with username&password,then server create a token by key send to client
            if IsHasJWT == False:
                print('[SERVER]frist login with username&password,Assuming a successful logins.')
                # create token by client information
                payload = {
                    'iss': 'RossUserName',  # client information
                    'iat': datetime.datetime.now(),
                    'exp': datetime.datetime.now() + datetime.timedelta(days=1),
                    "sub": "RossUserName",   # client information
                    "username": "RossUserName",
                }
                token = jwt.encode(payload, 'secretKey', algorithm='HS256')
                print("[SERVER]create token send to client:\n", token)
                conn.send(token.encode())
                IsHasJWT = True
            # after frist login, client request with token, server validate token by decoding with key
            else:
                print("[SERVER]client send token for validating, msg is :\n",msg.decode())
                # validate token by decoding
                try:
                    token = msg.decode()
                    token = jwt.decode(token, 'secretKey', algorithms=['HS256'])
                    print("[SERVER]token is right,decoded token is \n", token)
                    conn.send("token is right".encode())
                except Exception:
                    print("[SERVER]token is wrong")
                    conn.send("token is wrong".encode())
conn.close()
server.close()