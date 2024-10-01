import socket


def start_tcp_client(host='127.0.0.1', port=12345, message="Привет, сервер!"):
    # Создаем TCP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключаемся к серверу
    client_socket.connect((host, port))
    print(f"Подключились к серверу {host}:{port}")

    # Отправляем сообщение серверу
    client_socket.sendall(message.encode())

    # Получаем ответ от сервера
    data = client_socket.recv(1024)
    print(f"Ответ от сервера: {data.decode()}")

    # Закрываем соединение
    client_socket.close()


if __name__ == "__main__":
    start_tcp_client()
