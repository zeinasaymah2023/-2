import socket
import threading

Q = {
    "Does pipelining decrease the efficiency of transmission?": "f",
    "Is 'Time to Live' in IPv4 replaced with 'Hop Limit' in IPv6?": "t",
    "Is there no pipelining in the Go-Back-N protocols?": "t",
    "In Slotted ALOHA, can a station transmit frames at any time?": "f",
    "Is the vulnerable time in Pure ALOHA equal to the double of frame transmission time?": "t",
    " In Slotted ALOHA, can a station transmit frames at any time?": "f",
    "Is the broadcast address of the network containing this IP (192.168.5.69/26) equal to 192.168.2.127/26?": "t",
    "Is the address of the network containing this IP (192.168.5.99/27) equal to 192.168.5.64/27?": "f",
    "Does the network 192.162.85.64/27 have 30 usable host addresses?": "t",
    "Is there a partial collision in Pure ALOHA?": "t",
    "In Slotted ALOHA, can a station transmit frames at any time? ": "f",
    "Does the network address 192.168.0.0/23 have 510 usable host addresses?": "t",
    "Does the ALOHA protocol sense the medium before sending frames?": "f",
    " In Slotted ALOHA, can a station transmit frames at any time?": "f",
    " Is the throughput of Pure ALOHA higher than the throughput when offered load rate G=0.5?": "f",
    "Is the throughput of Slotted ALOHA higher than the throughput when offered load rate G=0.5?": "t",
    " Is the probability of collision in P-persistent Based Protocols higher than 1-persistent Based protocols?": "f",
    " Is the vulnerable time in Pure ALOHA equal to the double of frame transmission time?": "t",
    " Does the IP address 205.16.197.79/17 belong to the network 205.16.128.0/17?": "t",
    " Is the broadcast of network 192.168.5.73/28 equal to 192.168.5.79?": "t",
    "Is the broadcast of network 192.168.5.73/28 equal to 192.168.5.79?": "t"
}

scores = {}

def handle_client(client_socket, address):
    for question in Q.keys():
        client_socket.send(question.encode())
        answer = client_socket.recv(1024).decode()

        if answer == Q[question]:
            scores[address] = scores.get(address, 0) + 1

    if address in scores:
        score_message = '{}/{}'.format(scores[address], len(Q))
        client_socket.send(score_message.encode())

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 6523))
    server_socket.listen(5)
    print('The server has been started.')
    while True:
        client_socket, address = server_socket.accept()
        print('New connection:', address)

        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

start_server()
