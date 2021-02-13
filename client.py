import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        print('input key. ([q]->exit)')
        message = input()
        if message != 'q':
            len = sock.sendto(message.encode('utf-8'), ('127.0.0.1', 12345))

            # wait response from sercer
            msg, addr = sock.recvfrom(128) # set receive size
            print(f"{msg.decode(encoding='utf-8')}")

        else:
            sock.close()
            break

    except KeyboardInterrupt:
        sock.close()
        break
