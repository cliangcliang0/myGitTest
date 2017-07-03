import socket
def convert_integer():
    data = 1234
    #32bit
    print "original:%s => Long host byte order:%s,Network byte order:%s"\
            %(data,socket.ntohl(data),socket.htonl(data))
    #16bit
    print "original:%s => Short host byte order:%s,Network byte order:%s"\
            %(data,socket.ntohs(data),socket.htons(data))

if __name__ == '__main__':
    convert_integer()
