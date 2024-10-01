import socket


def start_tcp_server(host='127.0.0.1', port=12345):
    # Создаем TCP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сокет к адресу и порту
    server_socket.bind((host, port))

    # Переводим сервер в режим ожидания подключения (ожидаем 1 подключение)
    server_socket.listen(1)
    print(f"Сервер запущен на {host}:{port}, ожидаем подключения...")

    # Ожидаем подключения клиента
    conn, addr = server_socket.accept()
    print(f"Клиент подключен: {addr}")

    # Получаем сообщение от клиента
    data = conn.recv(1024)
    print(f"Сообщение от клиента: {data.decode()}")

    # Отправляем сообщение обратно (echo)
    conn.sendall(data)

    # Закрываем соединение
    conn.close()
    print("Соединение закрыто")


if __name__ == "__main__":
    start_tcp_server()
