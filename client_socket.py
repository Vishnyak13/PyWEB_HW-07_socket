import socket

PORT = 5500


def run_client():
    ip = socket.gethostbyname(socket.gethostname())
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((ip, PORT))
    message = input('->>: ').casefold().strip()
    try:
        while True:
            if message == 'exit' or message == '':
                break
            client_sock.send(message.encode('utf-8'))
            message_from_server = client_sock.recv(128)
            print(f'Received a message from a server: {message_from_server.decode("utf-8")}')
            message = input('->>: ').casefold().strip()
    except KeyboardInterrupt as e:
        print(f'KeyboardInterrupt: {e}')
    finally:
        client_sock.close()


if __name__ == '__main__':
    run_client()

