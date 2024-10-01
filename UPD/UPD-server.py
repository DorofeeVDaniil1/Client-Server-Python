import socket


def start_udp_server(host='127.0.0.1', port=12345):
    # Создаем UDP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Привязываем сокет к адресу и порту
    server_socket.bind((host, port))
    print(f"UDP сервер запущен на {host}:{port}, ожидаем данных...")

    while True:
        # Ожидаем данные от клиента
        data, addr = server_socket.recvfrom(1024)
        print(f"Получено сообщение от {addr}: {data.decode()}")

        # Отправляем данные обратно клиенту
        server_socket.sendto(data, addr)
        print("Сообщение отправлено обратно клиенту")


if __name__ == "__main__":
    start_udp_server()
