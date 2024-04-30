#20301125
#S.M.ABRAR MUSTAKIM TAKI
import socket
import threading
port = 5060
data=16
hostname = socket.gethostname()
host_addr = socket.gethostbyname(hostname)
disconnected_msg = "End"
format = 'utf-8'
server_socket_address = (host_addr, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_address)

server.listen()
print("Server is Listening...") 


def handler(conn, addr):
 
    print("Connected to", addr)

    connected = True 
    while connected:
        initial = conn.recv(data).decode(format)
        print("Length of the message to be sent", initial)
        if initial:
            msg_length = int(initial)
            msg = conn.recv(msg_length).decode(format)

            if msg == disconnected_msg:
                print("Terminating Connection with ",addr)
                conn.send("Nice to meet you".encode(format)) 
                connected=False

            else: 
                msg = int(msg)
                salary = 0
                if msg <= 40:
                     salary = msg * 200 
                elif msg > 40:
                     salary = (msg-40) * 300 + 8000
                     
                conn.send(f"Salary: {salary}".encode(format))

    conn.close()

while True:
       
       conn, addr = server.accept()
       thread = threading.Thread(target=handler,args=(conn,addr))
       thread.start()
