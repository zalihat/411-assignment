import socket


# Create a TCP/IP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create server address
server_address = ('localhost',  1998)
print('Server waiting for connection')

# Bind socket to the server_address
socket.bind(server_address)

# the math function
def math(message):
    # split message to remove the comms ','
    message = message.split(',')

    # assign the values of the operation and variables
    operation = message[0]
    first_variable = int(message[1])
    second_variable = int(message[2])

    # perform operation
    if operation == '1':
        return first_variable + second_variable
    elif operation == '2':
        return first_variable - second_variable
    elif operation == '3':
        return first_variable * second_variable
    elif operation == '4':
        return first_variable / second_variable
    elif operation == '5':
        return first_variable % second_variable
    else:
        print('PLEASE USE A VALID OPERARION (add, subtract, multiply, divide or mod)')

# wait for a connection using an infinite loopv
while True:
    print('waiting for a connection...')
    # receive message from client and the client address
    client_message, client_address = socket.recvfrom(1024*3)
    # compute the result
    result = str(math(client_message))
    # send result back to client
    socket.sendto(result, client_address)
