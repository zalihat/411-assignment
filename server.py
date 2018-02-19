import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost',  5000)
print('Server waiting for connection')

socket.bind(server_address)

def calc(message):
    message = message.split(',')

    operation = message[0]
    firstInput = int(message[1])
    secondInput = int(message[2])

    if operation == '1':
        return firstInput + secondInput
    elif operation == '2':
        return firstInput - secondInput
    elif operation == '3':
        return firstInput * secondInput
    elif operation == '4':
        return firstInput / secondInput
    elif operation == '5':
        return firstInput % secondInput
    else:
        print('Wrong operation. Use another')

while True:
    print('waiting for a connection...')
    message, client_address = socket.recvfrom(1024*4)
    result = str(calc(message))
    socket.sendto(result, client_address)
