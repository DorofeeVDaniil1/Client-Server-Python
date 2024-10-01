import socket


def start_udp_client(host='127.0.0.1', port=12345, message="Привет, UDP-сервер!"):
    # Создаем UDP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Отправляем сообщение на сервер
    client_socket.sendto(message.encode(), (host, port))
    print(f"Сообщение отправлено на {host}:{port}")

    # Получаем ответ от сервера
    data, _ = client_socket.recvfrom(1024)
    print(f"Ответ от сервера: {data.decode()}")

    # Закрываем сокет
    client_socket.close()


if __name__ == "__main__":
    start_udp_client()
