import socket

if __name__ == '__main__':
    host = '192.168.1.10'
    port = 8080
    #addr = (host, port)
    addr = 'http://' + host + ':' + str(port) + "/"
    #addr = (host, port)

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data = input("enter word:")

        data = data.encode()
        #client.send(data,addr)
        client.sendto(data,addr)

        data, addr = client.recvfrom(1024)
        data = data.decode("utf-8")
        print(f"server: {data}")