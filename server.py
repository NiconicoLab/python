import socket
import time

sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 12345))

while True:
    try :
        msg, addr = sock.recvfrom(128) # set receive size
        msg = msg.decode(encoding='utf-8')
        print(f'message : {msg}')

        time.sleep(1)

        # send response to client
        sock.sendto('response success'.encode(encoding='utf-8'), addr)

    except KeyboardInterrupt:
        sock.close()
        break
